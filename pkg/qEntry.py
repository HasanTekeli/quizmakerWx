import wx


class QuestionEntry(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: openExam.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("frame_2")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_1 = wx.GridSizer(8, 2, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        year_sem = wx.StaticText(self.panel_1, wx.ID_ANY, u"Yıl / Dönem")
        grid_sizer_1.Add(year_sem, 0, 0, 0)

        exam_name = wx.StaticText(self.panel_1, wx.ID_ANY, u"Sınav Adı")
        grid_sizer_1.Add(exam_name, 0, 0, 0)

        q_lbl = wx.StaticText(self.panel_1, wx.ID_ANY, "Soru:")
        grid_sizer_1.Add(q_lbl, 0, 0, 0)

        self.q_input = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        grid_sizer_1.Add(self.q_input, 0, wx.EXPAND, 0)

        ca_lbl = wx.StaticText(self.panel_1, wx.ID_ANY, u"Doğru Cevap:")
        grid_sizer_1.Add(ca_lbl, 0, 0, 0)

        self.ca_input = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        grid_sizer_1.Add(self.ca_input, 0, wx.EXPAND, 0)

        wa1_lbl = wx.StaticText(self.panel_1, wx.ID_ANY, u"Yanlış Cevap 1:")
        grid_sizer_1.Add(wa1_lbl, 0, 0, 0)

        self.wa1_input = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        grid_sizer_1.Add(self.wa1_input, 0, wx.EXPAND, 0)

        wa2_lbl = wx.StaticText(self.panel_1, wx.ID_ANY, u"Yanlış Cevap 2:")
        grid_sizer_1.Add(wa2_lbl, 0, 0, 0)

        self.wa2_input = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        grid_sizer_1.Add(self.wa2_input, 0, wx.EXPAND, 0)

        wa3_lbl = wx.StaticText(self.panel_1, wx.ID_ANY, u"Yanlış Cevap 3:")
        grid_sizer_1.Add(wa3_lbl, 0, 0, 0)

        self.wa3_input = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        grid_sizer_1.Add(self.wa3_input, 0, wx.EXPAND, 0)

        qnum_lbl = wx.StaticText(self.panel_1, wx.ID_ANY, u"Soru sayısı:")
        grid_sizer_1.Add(qnum_lbl, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)

        qnum_info = wx.StaticText(self.panel_1, wx.ID_ANY, "1")
        grid_sizer_1.Add(qnum_info, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.q_input_exit = wx.Button(self.panel_1, wx.ID_ANY, u"Kaydetmeden Çık")
        grid_sizer_1.Add(self.q_input_exit, 0, wx.EXPAND, 0)

        self.save_question = wx.Button(self.panel_1, wx.ID_ANY, u"Kaydet ve İlerle")
        grid_sizer_1.Add(self.save_question, 0, wx.EXPAND, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        # end wxGlade

# end of class openExam
