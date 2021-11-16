import wx

def entry(panel, vbox):
    #Soru giriş bölümü
    font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

    font.SetPointSize(9)

    hbox1 = wx.BoxSizer(wx.HORIZONTAL)
    st1 = wx.StaticText(panel, label='Question: ')
    st1.SetFont(font)
    hbox1.Add(st1, flag=wx.RIGHT, border=8)
    tc = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
    hbox1.Add(tc, proportion=1)
    vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

    vbox.Add((-1, 10))

    hbox2 = wx.BoxSizer(wx.HORIZONTAL)
    st2 = wx.StaticText(panel, label='Doğru Cevap: ')
    st2.SetFont(font)
    hbox2.Add(st2)
    tc2 = wx.TextCtrl(panel)
    hbox2.Add(tc2, proportion=1)
    vbox.Add(hbox2, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10)

    vbox.Add((-1, 10))

    hbox3 = wx.BoxSizer(wx.HORIZONTAL)
    st3 = wx.StaticText(panel, label='Yanlış Cevap 1: ')
    st3.SetFont(font)
    hbox3.Add(st3)
    tc3 = wx.TextCtrl(panel)
    hbox3.Add(tc3, proportion=1)
    vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10)

    vbox.Add((-1, 10))

    hbox4 = wx.BoxSizer(wx.HORIZONTAL)
    st4 = wx.StaticText(panel, label='Yanlış Cevap 2: ')
    st4.SetFont(font)
    hbox4.Add(st4)
    tc4 = wx.TextCtrl(panel)
    hbox4.Add(tc4, proportion=1)
    vbox.Add(hbox4, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10)

    vbox.Add((-1, 10))
        
    hbox5 = wx.BoxSizer(wx.HORIZONTAL)
    st5 = wx.StaticText(panel, label='Yanlış Cevap 3: ')
    st5.SetFont(font)
    hbox5.Add(st5)
    tc5 = wx.TextCtrl(panel)
    hbox5.Add(tc5, proportion=1)
    vbox.Add(hbox5, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10)

    vbox.Add((-1, 25))