import wx
import frc_inspection_manager_wx


class Team:
    def __init__(self):
        self.team_number = None
        self.team_status = None


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
        for i in range(0, 40):
            p = frc_inspection_manager_wx.TeamStatus(self)
            p.team_number.SetLabel(str(i))
            p.team_status.SetLabel('unknown')
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
    app = wx.App()

    frm1 = MainFrame(None)
    frm1.SetStatusText("w1!")
    frm1.Show()
    print(dir(frm1))

    frm2 = Status(frm1)
    frm2.Show()

    app.MainLoop()