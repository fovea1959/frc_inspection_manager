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
        self.team_grid.AppendRows(len(database.teams)-1)

        self.team_to_row_map = {}
        self.row_to_team_map = {}
        for i, t in enumerate(self.database.teams):
            self.team_to_row_map[t.team_number] = i
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
        self.inspector_grid.AppendRows(len(database.inspectors)-1)

        self.inspector_to_row_map = {}
        self.row_to_inspector_map = {}
        for i, inspector in enumerate(database.inspectors):
            self.inspector_to_row_map[inspector.id] = i
            self.row_to_inspector_map[i] = inspector
            self.update_inspector(inspector)

        self.inspector_grid.SetColLabelValue(0, 'uuid')
        self.inspector_grid.SetColLabelValue(1, 'status')
        # self.inspector_grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        self.inspector_grid.SetRowLabelSize(wx.grid.GRID_AUTOSIZE)
        self.inspector_grid.AutoSize()
        self.inspector_panel.Layout()

    def set_status_frame(self, status_frame):
        self.status_frame = status_frame

    def update_team(self, t: Team):
        row = self.team_to_row_map[t.team_number]

        self.team_grid.SetRowLabelValue(row, str(t.team_number))
        self.team_grid.SetCellValue(row, 0, t.team_name)
        self.team_grid.SetCellValue(row, 1, t.team_status_s())
        self.team_grid.SetCellAlignment(row, 1, wx.ALIGN_CENTER, wx.ALIGN_CENTER)

    def update_inspector(self, inspector: Inspector):
        row = self.inspector_to_row_map[inspector.id]

        self.inspector_grid.SetRowLabelValue(row, inspector.name)
        self.inspector_grid.SetCellValue(row, 0, str(inspector.id))
        self.inspector_grid.SetCellValue(row, 1, inspector.status_s())
        self.inspector_grid.SetCellAlignment(row, 1, wx.ALIGN_CENTER, wx.ALIGN_CENTER)

    def on_team_right_click(self, event):
        print(event.GetEventType(), event.GetEventObject(), event.GetCol(), event.GetRow())
        row = event.GetRow()
        team = self.row_to_team_map[row]
        self.display_team_context_menu(event, team)
        event.Skip()

    def display_team_context_menu(self, event, team):
        self.m_t_team.SetItemLabel(str(team.team_number))
        self.team_for_context_menu = team
        self.team_panelOnContextMenu(event)

    def on_t_context(self, event: wx._core.CommandEvent):
        print(type(event), event.GetId(), self.team_for_context_menu)
        id = event.GetId()
        team = self.team_for_context_menu
        if id == frc_inspection_manager_wx.ID_T_WEIGHIN:
            team.team_status = TeamStatus.Weighed
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
        self.inspector_panelOnContextMenu(event)

    def on_i_context(self, event: wx._core.CommandEvent):
        print(type(event), event.GetId(), self.inspector_for_context_menu)
        id = event.GetId()
        inspector = self.inspector_for_context_menu

        if id == frc_inspection_manager_wx.ID_I_PIT:
            inspector.status = InspectorStatus.Pit
        elif id == frc_inspection_manager_wx.ID_I_FIELD:
            inspector.status = InspectorStatus.Field
        elif id == frc_inspection_manager_wx.ID_I_BREAK:
            inspector.status = InspectorStatus.Break
        elif id == frc_inspection_manager_wx.ID_I_AVAILABLE:
            inspector.status = InspectorStatus.Available
        elif id == frc_inspection_manager_wx.ID_I_OFF:
            inspector.status = InspectorStatus.Off
        elif id == frc_inspection_manager_wx.ID_I_PIT_RETURN:
            # TODO need to record inspection result!
            inspector.status = InspectorStatus.Available
        else:
            self.SetStatusText("Got funny command!")

        self.database.mark_dirty()
        self.update_inspector(inspector)


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
            self.team_to_gui_map[t.team_number] = p
            self.update_team(t)
            s.Add(p, 1, wx.EXPAND | wx.ALL, 2)
        s.SetSizeHints(self)
        self.SetSizer(s, deleteOld=True)
        self.Layout()

    def set_main_frame(self, main_frame):
        self.main_frame = main_frame

    def update_team(self, t: Team):
        p = self.team_to_gui_map[t.team_number]
        p.team_number.SetLabel(str(t.team_number))
        p.team_status.SetLabel(t.team_status_s())

    """
    really not needed; no close button!
    """
    def my_on_close(self, event):
        if event.CanVeto():
            event.Veto()
        else:
            event.Skip()


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

    if database.is_dirty():
        j = database.as_json()
        with open(fn + '.tmp', 'w') as fp:
            fp.write(j)

        if os.path.isfile(fn):
            ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            os.rename (fn, fn + '_' + ts)

        os.rename(fn + '.tmp', fn)
