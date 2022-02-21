import wx
import frc_inspection_manager_wx


class MainFrame(frc_inspection_manager_wx.MainFrame):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        super().__init__(parent)

        self.Bind(wx.EVT_CLOSE, self.myclose)

    def myclose(self, event):
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