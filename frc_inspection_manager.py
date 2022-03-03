import os
import datetime

import wx
import wx.grid

import frc_inspection_manager_wx

from frc_inspection_manager_database import *


class MainFrame(frc_inspection_manager_wx.MainFrame):
    # constructor
    def __init__(self, parent, database: Database, status_frame=None):
        # initialize parent class
        super().__init__(parent)

        self.database = database
        self.inspector_for_context_menu = None
        self.team_for_context_menu = None
        self.status_frame = status_frame

        self.grid_table = self.team_grid.GetTable()
        self.team_grid.ClearGrid()
        self.team_grid.AppendRows(len(database.teams))

        self.team_to_row_map = {}
        self.row_to_team_map = {}
        for i, t in enumerate(self.database.teams):
            self.team_to_row_map[t.number] = i
            self.row_to_team_map[i] = t
            self.update_team(t)

        self.team_grid.SetColLabelValue(0, 'Name')
        self.team_grid.SetColLabelValue(1, 'Status')
        # self.inspector_grid.SetColLabelAlignment(1, wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        self.team_grid.SetRowLabelSize(wx.grid.GRID_AUTOSIZE)
        self.team_grid.AutoSize()
        self.team_panel.Layout()

        self.inspector_table = self.inspector_grid.GetTable()
        self.inspector_grid.ClearGrid()
        self.inspector_grid.AppendRows(len(database.inspectors))

        self.inspector_to_row_map = {}
        self.row_to_inspector_map = {}
        for i, inspector in enumerate(database.inspectors):
            self.inspector_to_row_map[inspector.id] = i
            self.row_to_inspector_map[i] = inspector
            self.update_inspector(inspector)

        self.inspector_grid.SetColLabelValue(0, 'status')
        self.inspector_grid.SetColLabelValue(1, 'when left')
        # self.inspector_grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        self.inspector_grid.SetRowLabelSize(wx.grid.GRID_AUTOSIZE)
        self.inspector_grid.AutoSize()
        self.inspector_panel.Layout()

    def set_status_frame(self, status_frame):
        self.status_frame = status_frame

    def update_team(self, t: Team):
        row = self.team_to_row_map[t.number]

        self.team_grid.SetRowLabelValue(row, str(t.number))
        self.team_grid.SetCellValue(row, 0, t.name)
        s = t.status_s
        if len(t.inspectors_in_pit) > 0:
            inspector_names = []
            for inspector_id in t.inspectors_in_pit:
                inspector = self.database.fetch_inspector(inspector_id)
                inspector_names.append(inspector.name)
            s += "; " + ', '.join(inspector_names) + " in pit"
        self.team_grid.SetCellValue(row, 1, s)
        self.team_grid.SetCellAlignment(row, 1, wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        self.team_grid.AutoSize()
        self.team_panel.Layout()

    def update_inspector(self, inspector: Inspector):
        row = self.inspector_to_row_map[inspector.id]

        self.inspector_grid.SetRowLabelValue(row, inspector.name)
        self.inspector_grid.SetCellValue(row, 0, inspector.status_s)
        self.inspector_grid.SetCellAlignment(row, 0, wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        s = str(inspector.time_away_started) if inspector.time_away_started is not None else ""
        self.inspector_grid.SetCellValue(row, 1, s)
        self.update_inspector_out_timer(inspector)
        self.inspector_grid.AutoSize()
        self.inspector_panel.Layout()

    def update_inspector_out_timer(self, inspector: Inspector):
        row = self.inspector_to_row_map[inspector.id]
        s = ""
        if inspector.time_away_started is not None:
            out_time = datetime.datetime.now() - inspector.time_away_started
            s = str(out_time)
        self.inspector_grid.SetCellValue(row, 2, s)

    def on_timer(self, event):
        for inspector in self.row_to_inspector_map.values():
            self.update_inspector_out_timer(inspector)

    def on_team_right_click(self, event):
        print(event.GetEventType(), event.GetEventObject(), event.GetCol(), event.GetRow())
        row = event.GetRow()
        team = self.row_to_team_map[row]
        self.display_team_context_menu(event, team)
        event.Skip()

    def display_team_context_menu(self, event, team):
        self.m_t_team.SetItemLabel(str(team.number))
        self.team_for_context_menu = team

        self.m_t_checkin.Check(team.checked_in)

        self.team_panelOnContextMenu(event)

    def on_t_context(self, event: wx._core.CommandEvent):
        print(type(event), event.GetId(), self.team_for_context_menu)
        event_id = event.GetId()
        team = self.team_for_context_menu
        if event_id == frc_inspection_manager_wx.ID_T_CHECKIN:
            team.checked_in = not team.checked_in
        elif event_id == frc_inspection_manager_wx.ID_T_WEIGHIN:
            weighed_in = self.weighin_dialog_box()
            return
        else:
            self.SetStatusText("Got funny command!")

        self.database.mark_dirty()
        self.update_team(team)
        self.status_frame.update_team(team)

    def on_inspector_right_click(self, event):
        print(event.GetEventType(), event.GetEventObject(), event.GetCol(), event.GetRow())
        row = event.GetRow()
        inspector = self.row_to_inspector_map[row]
        self.display_inspector_context_menu(event, inspector)
        event.Skip()

    def display_inspector_context_menu(self, event, inspector):
        self.m_i_inspector.SetItemLabel(inspector.name)
        self.inspector_for_context_menu = inspector

        enable_all = [
            self.m_i_off, self.m_i_pit, self.m_i_field, self.m_i_pit_return, self.m_i_available, self.m_i_break
        ]
        enable = enable_all.copy()
        enable.remove(self.m_i_pit_return)
        if inspector.status == InspectorStatus.Off:
            enable.remove(self.m_i_off)
        elif inspector.status == InspectorStatus.In_Pit:
            enable = [self.m_i_pit_return]
        elif inspector.status == InspectorStatus.Field:
            enable.remove(self.m_i_field)
        elif inspector.status == InspectorStatus.Break:
            enable.remove(self.m_i_break)
        elif inspector.status == InspectorStatus.Available:
            enable.remove(self.m_i_available)
        else:
            raise Exception("unknown inspector status")

        for menuitem in enable_all:
            menuitem.Enable(False)
        for menuitem in enable:
            menuitem.Enable(True)

        self.inspector_panelOnContextMenu(event)

    def on_i_context(self, event: wx._core.CommandEvent):
        print(type(event), event.GetId(), self.inspector_for_context_menu)
        event_id = event.GetId()
        inspector = self.inspector_for_context_menu
        current_status = inspector.status

        new_status = None
        if event_id == frc_inspection_manager_wx.ID_I_PIT:
            # this will take care of setting the new status and updating GUI
            # if inspection was started
            inspection_started = self.inspection_start_dialog_box(inspector=inspector)
        elif event_id == frc_inspection_manager_wx.ID_I_FIELD:
            new_status = InspectorStatus.Field
        elif event_id == frc_inspection_manager_wx.ID_I_BREAK:
            new_status = InspectorStatus.Break
        elif event_id == frc_inspection_manager_wx.ID_I_AVAILABLE:
            new_status = InspectorStatus.Available
        elif event_id == frc_inspection_manager_wx.ID_I_OFF:
            new_status = InspectorStatus.Off
        elif event_id == frc_inspection_manager_wx.ID_I_PIT_RETURN:
            # this will update the inspector status
            self.inspection_end_dialog_box()
        else:
            self.SetStatusText("Got funny command!")

        if new_status != None:
            if new_status != current_status:
                inspector.status = new_status
                self.database.mark_dirty()
                self.update_inspector(inspector)

    def inspection_start_dialog_box(self, inspector: Inspector = None, team: Team = None):
        choices = None
        if team is None:
            choices = [str(t.number) for t in self.database.teams]
            prompt = "Which team is " + inspector.name + " + inspecting?"
        elif inspector is None:
            choices = [i.name for i in self.database.inspectors]
            prompt = "Which inspector is going to team " + str(team.number) + ", " + team.name
        else:
            prompt = "huh, programmer should have filled in either team or inspector"

        inspection_started = False
        if choices is not None:
            # "with" statement will do implicit destroy on dlg
            with wx.SingleChoiceDialog(self, prompt, "Start Inspection", choices, wx.CHOICEDLG_STYLE) as dlg:
                if dlg.ShowModal() == wx.ID_OK:
                    i = dlg.GetSelection()
                    if inspector is None:
                        inspector = self.database.inspectors[i]
                    else:
                        team = self.database.teams[i]

                    inspector.status = InspectorStatus.In_Pit
                    inspector.inspection_team_number = team.number
                    inspector.time_away_started = datetime.datetime.now()
                    team.inspectors_in_pit.add(inspector.id)

                    self.update_team(team)
                    self.status_frame.update_team(team)
                    self.update_inspector(inspector)

                    self.database.mark_dirty()

        return inspection_started

    def inspection_end_dialog_box(self):
        inspector = self.inspector_for_context_menu
        inspection = Inspection()
        inspection.inspection_reason = InspectionReason.Initial
        inspection.when = datetime.datetime.now()
        inspection.inspector_id = inspector.id
        with InspectionDialog(self, inspection, self.database) as dlg:
            # show as modal dialog
            result = dlg.ShowModal()
            print(f"weighin dialog box {result}")
            if result == wx.ID_OK:
                # user has hit OK -> read text control value
                print('OK!', vars(inspection))

                team_id = inspector.inspection_team_number
                team: Team = self.database.fetch_team(team_id)
                team.inspections.append(inspection)
                team.inspectors_in_pit.remove(inspector.id)
                inspector.status = InspectorStatus.Available
                inspector.inspection_team_number = None

                self.database.mark_dirty()

                self.update_team(team)
                self.status_frame.update_team(team)
                self.update_inspector(inspector)


    def weighin_dialog_box(self):
        team = self.team_for_context_menu
        weighin = Inspection()
        weighin.inspection_reason = InspectionReason.Weighin
        weighin.when = datetime.datetime.now()
        with InspectionDialog(self, weighin, self.database) as dlg:
            #dlg.text_ctrl_1.SetValue(self.text_ctrl_1.GetValue())
            # show as modal dialog
            result = dlg.ShowModal()
            print(f"weighin dialog box {result}")
            if result == wx.ID_OK:
                # user has hit OK -> read text control value
                print('OK!', vars(weighin))

                team.inspections.append(weighin)

                self.database.mark_dirty()

                self.update_team(team)
                self.status_frame.update_team(team)

    def my_on_close(self, event):
        print(event.GetEventType(), event.GetEventObject())
        event.Skip()

    """
    this is obsolete, but keeping for reference purposes
    """
    def xx_my_on_close(self, event):
        print(event.GetEventType(), event.GetEventObject())
        if event.CanVeto():
            if wx.MessageBox("The file has not been saved... continue closing?",
                             "Please confirm",
                             wx.ICON_QUESTION | wx.YES_NO) != wx.YES:
                event.Veto()
                return
        event.Skip()


class TeamStatusFrame(frc_inspection_manager_wx.TeamStatusFrame):
    # constructor
    def __init__(self, parent, database: Database, main_frame=None):
        # initialize parent class
        super().__init__(parent)

        self.database = database
        self.main_frame = main_frame
        self.team_to_gui_map = {}

        s = wx.GridSizer(8, 8, 2, 2)
        for t in self.database.teams:
            p = frc_inspection_manager_wx.TeamStatusPanel(self)
            self.team_to_gui_map[t.number] = p
            self.update_team(t)
            s.Add(p, 1, wx.EXPAND | wx.ALL, 2)
        s.SetSizeHints(self)
        self.SetSizer(s, deleteOld=True)
        self.Layout()

    def set_main_frame(self, main_frame):
        self.main_frame = main_frame

    def update_team(self, t: Team):
        p = self.team_to_gui_map[t.number]
        p.team_number.SetLabel(str(t.number))
        s = t.status_s
        if len(t.inspectors_in_pit) > 0:
            s += "; inspector in pit"
        p.team_status.SetLabel(s)

    def my_on_close(self, event):
        """
        really not needed; no close button!
        """
        if event.CanVeto():
            event.Veto()
        else:
            event.Skip()


class InspectionDialog(frc_inspection_manager_wx.InspectionDialog):
    def __init__(self, parent, inspection, db):
        # initialize parent class
        super().__init__(parent)

        self.inspection = inspection
        self.database = db

        self.robot_weight.SetValidator(WeightValidator(data=self.inspection, key='robot_weight', must_have_value=False))
        self.red_bumper_weight.SetValidator(WeightValidator(data=self.inspection, key='red_bumper_weight', must_have_value=False))
        self.blue_bumper_weight.SetValidator(WeightValidator(data=self.inspection, key='blue_bumper_weight', must_have_value=False))
        self.robot_weight_with_red.SetValidator(WeightValidator(data=self.inspection, key='robot_weight_with_red', must_have_value=False))
        self.robot_weight_with_blue.SetValidator(WeightValidator(data=self.inspection, key='robot_weight_with_blue', must_have_value=False))
        self.inspector.SetValidator(InspectorValidator(data=self.inspection, key='inspector_id', inspectors=self.database.inspectors))
        self.passed.SetValidator(PassedInspectionValidator(data=self.inspection, key='passed'))
        self.comments.SetValidator(CommentsValidator(data=self.inspection, key='comments'))

        print(f"inspection reason {inspection.inspection_reason}")

        if inspection.inspection_reason == InspectionReason.Weighin:
            self.robot_weight.GetValidator().must_have_value = True
            self.enable_robot_weight_with_red(False)
            self.enable_robot_weight_with_blue(False)
            self.enable_passed(False)
        elif inspection.inspection_reason == InspectionReason.Initial:
            self.enable_robot_weight(False)
            self.enable_red_bumper_weight(False)
            self.enable_blue_bumper_weight(False)
            self.enable_robot_weight_with_red(False)
            self.enable_robot_weight_with_blue(False)
        elif inspection.inspection_reason == InspectionReason.Reinspect:
            pass
        elif inspection.inspection_reason == InspectionReason.Final:
            pass
        else:
            raise Exception("need to have a reason to inspect!")

    def enable_robot_weight(self, enabled):
        self.robot_weight_label.Enable(enabled)
        self.robot_weight.Enable(enabled)

    def enable_red_bumper_weight(self, enabled):
        self.red_bumper_weight_label.Enable(enabled)
        self.red_bumper_weight.Enable(enabled)

    def enable_blue_bumper_weight(self, enabled):
        self.blue_bumper_weight_label.Enable(enabled)
        self.blue_bumper_weight.Enable(enabled)

    def enable_robot_weight_with_red(self, enabled):
        self.robot_weight_with_red_label.Enable(enabled)
        self.robot_weight_with_red.Enable(enabled)

    def enable_robot_weight_with_blue(self, enabled):
        self.robot_weight_with_blue_label.Enable(enabled)
        self.robot_weight_with_blue.Enable(enabled)

    def enable_inspector(self, enabled):
        print(f"setting inspector enabled = {enabled}")
        self.inspector_label.Enable(enabled)
        self.inspector.Enable(enabled)
        print(f"inspector enabled = {self.inspector.IsEnabled()}")

    def enable_passed(self, enabled):
        self.passed_label.Enable(enabled)
        self.passed.Enable(enabled)

    def on_OK_button(self, event):
        print("Event handler 'on_button_OK' called")
        # don't call Skip if you want to keep the dialog open
        if False:  # maybe also check self.validate_contents()
            print("Checkbox not checked -> don't close the dialog")
            wx.Bell()
        else:
            print("Checkbox checked -> close the dialog")
            event.Skip()


class WeightValidator(wx.Validator):
    def __init__(self, must_have_value=False, data=None, key=None):
        super().__init__()
        if data is None:
            raise Exception("must specify data=")
        if key is None:
            raise Exception("must specify key=")
        self.must_have_value = must_have_value
        self.data = data
        self.key = key
        self.value = None

    def Clone(self):
        return WeightValidator(must_have_value=self.must_have_value, data=self.data, key=self.key)

    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue().strip()
        ok = True
        self.value = None
        if len(text) > 0:
            try:
                self.value = float(text)
            except ValueError:
                pass

        if self.value is None and self.must_have_value:
            # wx.MessageBox("This field must contain some text!", "Error")
            ok = False

        if ok:
            textCtrl.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
        else:
            textCtrl.SetBackgroundColour("pink")
            textCtrl.SetFocus()
            textCtrl.Refresh()

        return ok

    def TransferToWindow(self):
        textCtrl = self.GetWindow()
        self.value = getattr(self.data, self.key)
        if self.value is None:
            textCtrl.SetValue('')
        else:
            textCtrl.SetValue(str(self.value))
        return True

    def TransferFromWindow(self):
        setattr(self.data, self.key, self.value)
        return True


class InspectorValidator(wx.Validator):
    def __init__(self, data=None, key=None, inspectors=None):
        super().__init__()
        if data is None:
            raise Exception("must specify data=")
        if key is None:
            raise Exception("must specify key=")
        if inspectors is None:
            raise Exception("must specify inspectors=")
        self.data = data
        self.key = key
        self.inspectors = inspectors

    def Clone(self):
        return InspectorValidator(data=self.data, key=self.key, inspectors=self.inspectors)

    def Validate(self, win):
        return True

    def TransferToWindow(self):
        inspector_choice: wx.Choice = self.GetWindow()

        current_inspector_id = getattr(self.data, self.key)

        inspector_list = []
        inspector_choice.Clear()

        inspector_index = 0
        inspector_choice.Append('-- none --')
        inspector_list.append(None)

        for i, inspector in enumerate(self.inspectors):
            inspector_choice.Append(inspector.name)
            inspector_list.append(inspector)
            if current_inspector_id is not None:
                if inspector.id == current_inspector_id:
                    inspector_index = i + 1
        inspector_choice.SetSelection(inspector_index)
        print(current_inspector_id, inspector_list, inspector_index)

        return True

    def TransferFromWindow(self):
        choice: wx.Choice = self.GetWindow()
        selection_index = choice.GetSelection()
        print('selection', selection_index, self.inspectors)
        if selection_index == 0:
            inspector_id = None
        else:
            inspector = self.inspectors[selection_index-1]
            print('inspector choice', inspector)
            inspector_id = inspector.id
        setattr(self.data, self.key, inspector_id)
        return True


class PassedInspectionValidator(wx.Validator):
    def __init__(self, data=None, key=None):
        super().__init__()
        if data is None:
            raise Exception("must specify data=")
        if key is None:
            raise Exception("must specify key=")
        self.data = data
        self.key = key

    def Clone(self):
        return PassedInspectionValidator(data=self.data, key=self.key)

    def Validate(self, win):
        return True

    def TransferToWindow(self):
        passed_choice: wx.Choice = self.GetWindow()

        passed_choice.Clear()

        passed_choice.Append('-- no change --')
        passed_choice.Append('Passed')
        passed_choice.Append('Not passed')

        passed_index = 0
        v = getattr(self.data, self.key)
        if v is not None:
            passed_index = 1 if v else 0

        passed_choice.SetSelection(passed_index)

        return True

    def TransferFromWindow(self):
        choice: wx.Choice = self.GetWindow()
        selection_index = choice.GetSelection()
        if selection_index == 0:
            passed = None
        else:
            passed = selection_index == 1
        setattr(self.data, self.key, passed)
        return True


class CommentsValidator(wx.Validator):
    def __init__(self, data=None, key=None):
        super().__init__()
        if data is None:
            raise Exception("must specify data=")
        if key is None:
            raise Exception("must specify key=")
        self.data = data
        self.key = key

    def Clone(self):
        return CommentsValidator(data=self.data, key=self.key)

    def Validate(self, win):
        return True

    def TransferToWindow(self):
        textctrl: wx.TextCtrl = self.GetWindow()

        v = getattr(self.data, self.key)
        if v is None:
            v = ''
        textctrl.SetValue(v)

        return True

    def TransferFromWindow(self):
        textctrl: wx.TextCtrl = self.GetWindow()

        v = textctrl.GetValue()
        v = v.rstrip()
        if len(v) == 0:
            v = None
        setattr(self.data, self.key, v)
        return True


if __name__ == '__main__':
    database = Database()
    fn = 'misjo.imd'
    with open(fn, 'r') as fp:
        j = fp.read()
        database.from_json(j)
        print(database)

    app = wx.App()

    frm1 = MainFrame(None, database)
    frm1.Show()

    frm2 = TeamStatusFrame(frm1, database, main_frame=frm1)
    frm1.set_status_frame(frm2)
    frm2.Iconize(True)
    frm2.Show()

    app.MainLoop()

    if database.is_dirty:
        j = database.as_json()
        with open(fn + '.tmp', 'w') as fp:
            fp.write(j)

        if os.path.isfile(fn):
            ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            os.rename(fn, fn + '_' + ts)

        os.rename(fn + '.tmp', fn)
