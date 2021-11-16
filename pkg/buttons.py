import wx

def buttons(self, panel, hbox1, hbox2):
    openBtn = wx.Button(panel, wx.ID_ANY, label="Varolan Sınavı Aç", name="openBtn")
    openBtn.SetSize((100,100))
    openBtn.Bind(wx.EVT_BUTTON, self.onOpen)
  
    hbox1.Add(openBtn, 0, wx.CENTER)

    newBtn = wx.Button(panel, wx.ID_ANY, label="Yeni Sınav", name="newBtn")
    newBtn.SetSize((100,100))
    newBtn.Bind(wx.EVT_BUTTON, self.onNew)
  
    hbox2.Add(newBtn, 1, wx.CENTER)