import uuid

import wx
import wx.grid

import frc_inspection_manager_dummy_data
import frc_inspection_manager_wx
import enum


WeighinReason = enum.Enum('WeighinReason', 'Initial Reinspect Final')


class Weighin:
    def __init__(self):
        self.when = None
        self.inspector_id: uuid = None
        self.robot_weight = None
        self.red_bumper_weight = None
        self.blue_bumper_weight = None
        self.robot_weight_with_red = None
        self.robot_weight_with_blue = None
        self.weighin_reason: WeighinReason = None
        self.success = False


TeamStatus = enum.Enum('TeamStatus', 'Absent Present Weighed Partial Inspected Final_completed')


class Team:
    def __init__(self):
        self.team_number = None
        self.team_name = None
        self.team_status = None
        self.weighins = []


InspectorStatus = enum.Enum('InspectorStatus', 'Off Available Pit Break Field')


class Inspector:
    def __init__(self):
        self.id = None
        self.name = None
        self.status = None
        self.inspection_team = None
        self.inspection_started = None
        self.break_started = None


class Database:
    def __init__(self):
        self.teams = []
        self.inspectors = []
        self.team_map = {}
        self.inspector_map = {}

    def make_indices(self):
        self.team_map.clear()
        for t in self.teams:
            self.team_map[t.team_number] = t
        self.inspector_map.clear()
        for i in self.inspectors:
            self.inspector_map[i.id] = i

    def fetch_team(self, team_number):
        return self.team_map[team_number]

    def fetch_inspector(self, inspector_id):
        return self.inspector_map[inspector_id]


# this is global
database: Database = None


class MainFrame(frc_inspection_manager_wx.MainFrame):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        super().__init__(parent)

        self.grid_table = self.team_grid.GetTable()
        self.team_grid.ClearGrid()
        self.team_grid.AppendRows(len(database.teams)-1)

        self.team_to_row_map = {}
        for i, t in enumerate(database.teams):
            self.team_to_row_map[t.team_number] = i
            self.team_grid.SetRowLabelValue(i, str(t.team_number))
            self.team_grid.SetCellValue(i, 0, str(t.team_name))
            self.team_grid.SetCellValue(i, 1, str(t.team_status))

        self.team_grid.SetRowLabelSize(wx.grid.GRID_AUTOSIZE)
        self.team_grid.AutoSize()
        self.m_panel1.Layout()

    def update_team(self, t: Team):
        row = self.team_to_map[t.team_number]

        self.team_grid.SetRowLabelValue(row, str(t.team_number))
        self.team_grid.SetCellValue(row, 0, str(t.team_name))
        self.team_grid.SetCellValue(row, 1, str(t.team_status))

    def my_on_close(self, event):
        if event.CanVeto():
            if wx.MessageBox("The file has not been saved... continue closing?",
                             "Please confirm",
                             wx.ICON_QUESTION | wx.YES_NO) != wx.YES:
                event.Veto()
                return
        event.Skip()


class Status(frc_inspection_manager_wx.Status):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        super().__init__(parent)

        self.team_to_gui_map = {}

        s = wx.GridSizer(8, 8, 2, 2)
        for t in database.teams:
            p = frc_inspection_manager_wx.TeamStatus(self)
            self.team_to_gui_map[t.team_number] = p
            self.update_team_status(t)
            s.Add(p, 1, wx.EXPAND | wx.ALL, 2)
        s.SetSizeHints(self)
        self.SetSizer(s, deleteOld=True)
        self.Layout()

    def update_team_status (self, t: Team):
        p = self.team_to_gui_map[t.team_number]
        p.team_number.SetLabel(str(t.team_number))
        p.team_status.SetLabel(str(t.team_status))

    def my_on_close(self, event):
        if event.CanVeto():
            event.Veto()
        else:
            event.Skip()


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    database = frc_inspection_manager_dummy_data.dummy_database()
    database.make_indices()

    app = wx.App()

    frm1 = MainFrame(None)
    frm1.SetStatusText("w1!")
    frm1.Show()

    frm2 = Status(frm1)
    frm2.Show()

    app.MainLoop()