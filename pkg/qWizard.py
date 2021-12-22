import wx
from wx.adv import Wizard as wiz
from wx.adv import WizardPageSimple


class TitledPage(WizardPageSimple):
    """"""

    def __init__(self, parent, title):
        """Constructor"""
        WizardPageSimple.__init__(self, parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        title = wx.StaticText(self, -1, title)
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(title, 0, wx.ALIGN_CENTRE | wx.ALL, 5)
        sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND | wx.ALL, 5)


class DynaWiz(object):
    def __init__(self):
        wizard = wiz(None, -1, "Wizard")
        self.pageList = [AddPage(wizard, self)]
        for i in range(len(self.pageList)-1):
            WizardPageSimple.Chain(self.pageList[i], self.pageList[i+1])

        wizard.FitToPage(self.pageList[0])
        wizard.RunWizard(self.pageList[0])
        wizard.Destroy()


class AddPage(WizardPageSimple):
    def __init__(self, parent, dynawiz):
        self.parent = parent
        self.dynawiz = dynawiz
        """Constructor"""
        WizardPageSimple.__init__(self, parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self.numPageAdd = wx.TextCtrl(self, -1, "")
        self.verifyButton = wx.Button(self, id=wx.ID_ANY, label="Confirm", name="confirm")
        self.verifyButton.Bind(wx.EVT_BUTTON, self.append_pages)

        sizer.Add(self.numPageAdd, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(self.verifyButton, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND|wx.ALL, 5)

    def append_pages(self,event):
        n = int(self.numPageAdd.GetValue())
        for i in range(n):
            self.dynawiz.pageList.append(TitledPage(self.parent, "Added Page"))
            WizardPageSimple.Chain(self.dynawiz.pageList[-2], self.dynawiz.pageList[-1])
        self.parent.FindWindowById(wx.ID_FORWARD).SetLabel("Next >")


if __name__ == "__main__":
    app = wx.App(False)
    dWiz = DynaWiz()
    app.MainLoop()
