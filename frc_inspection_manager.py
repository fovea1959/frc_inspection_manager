import uuid

import wx

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
        self.weighin_reason: WeighinReason = None


TeamStatus = enum.Enum('TeamStatus', 'Absent Present Weighed Partial Inspected')


class Team:
    def __init__(self):
        self.team_number = None
        self.team_name = None
        self.team_status = None
        self.weighins = []


InspectorStatus = enum.Enum('InspectorStatus', 'Available Pit Break Field')


class Inspector:
    def __init__(self):
        self.id = None
        self.name = None
        self.status = None
        self.inspection_team = None
        self.inspection_started = None


class Database:
    def __init__(self):
        teams = []
        inspectors = []


# this is global
database: Database = None


class MainFrame(frc_inspection_manager_wx.MainFrame):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        super().__init__(parent)

    def my_on_close(self, event):
        print(event)
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

        s = wx.GridSizer(8, 8, 2, 2)
        for t in database.teams:
            p = frc_inspection_manager_wx.TeamStatus(self)
            p.team_number.SetLabel(str(t.team_number))
            p.team_status.SetLabel(str(t.team_status))
            s.Add(p, 1, wx.EXPAND | wx.ALL, 2)
        s.SetSizeHints(self)
        self.SetSizer(s, deleteOld=True)
        self.Layout()

    def my_on_close(self, event):
        if event.CanVeto():
            event.Veto()
        else:
            event.Skip()


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    database = frc_inspection_manager_dummy_data.dummy_database()

    app = wx.App()

    frm1 = MainFrame(None)
    frm1.SetStatusText("w1!")
    frm1.Show()
    print(dir(frm1))

    frm2 = Status(frm1)
    frm2.Show()

    app.MainLoop()