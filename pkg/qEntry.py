import wx
import wx.lib.scrolledpanel
from .file_io import read_file, write_file


class QuestionEntry(wx.Frame):
    def __init__(self, exam, file):
        wx.Frame.__init__(self, None, 1)
        screen_size = wx.DisplaySize()
        screen_height = screen_size[1] / 8 * 7
        self.SetSize((500, screen_height))
        self.SetTitle("frame_2")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        self.exam_info = exam
        self.file = file
        self.question = {}

        year, semester, ydl, exam_type = self.exam_info["year"], self.exam_info["semester"], self.exam_info["ydl"], self.exam_info["exam"]
        questions = self.exam_info["questions"]

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_1 = wx.GridSizer(8, 2, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        year_sem = wx.StaticText(self.panel_1, wx.ID_ANY, str(year) + " " + str(semester))
        grid_sizer_1.Add(year_sem, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)

        exam_name = wx.StaticText(self.panel_1, wx.ID_ANY, "YDL" + str(ydl) + " "  + str(exam_type))
        grid_sizer_1.Add(exam_name, 0, wx.ALIGN_CENTER_VERTICAL, 0)

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

        qnum_info = wx.StaticText(self.panel_1, wx.ID_ANY, "1/25")
        grid_sizer_1.Add(qnum_info, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.q_input_exit = wx.Button(self.panel_1, wx.ID_ANY, u"Kaydetmeden Çık")
        grid_sizer_1.Add(self.q_input_exit, 0, wx.EXPAND, 0)

        self.save_question = wx.Button(self.panel_1, wx.ID_ANY, u"Kaydet ve İlerle")
        grid_sizer_1.Add(self.save_question, 0, wx.EXPAND, 0)
        self.Bind(wx.EVT_BUTTON, self.onNextPage, self.save_question)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        self.on_load(questions)
        # end wxGlade

    def on_load(self, questions):
        for i in questions:
            if i[1]["question"]:
                self.q_input.SetValue(i[1]["question"])
                self.ca_input.SetValue(i[1]["ca"])
                self.wa1_input.SetValue(i[1]["wa1"])
                self.wa2_input.SetValue(i[1]["wa2"])
                self.wa3_input.SetValue(i[1]["wa3"])

    def onNextPage(self, event):
        q = self.q_input.GetValue()
        ca = self.ca_input.GetValue()
        wa1 = self.wa1_input.GetValue()
        wa2 = self.wa2_input.GetValue()
        wa3 = self.wa3_input.GetValue()
        print(q, ca, wa1, wa2, wa3)
        self.question = {"question": q,
                         "ca": ca,
                         "wa1": wa1,
                         "wa2": wa2,
                         "wa3": wa3}
        write_file(self.file, self.question)
        self.q_input.SetValue("")
        self.ca_input.SetValue("")
        self.wa1_input.SetValue("")
        self.wa2_input.SetValue("")
        self.wa3_input.SetValue("")


# end of class openExam
