import wx
import wx.lib.scrolledpanel as scrolled
from .file_io import read_file, write_file


class QuestionEntry(wx.Frame):
    def __init__(self, exam, file):
        wx.Frame.__init__(self, None, 1)
        screen_size = wx.DisplaySize()
        screen_height = screen_size[1] / 8 * 7
        self.SetSize((500, screen_height))
        self.SetTitle("frame_2")

        self.panel = wx.Panel(self, wx.ID_ANY)
        self.scrolled_panel = scrolled.ScrolledPanel(self.panel, -1,
                                              style=wx.TAB_TRAVERSAL | wx.SUNKEN_BORDER,
                                              name="panel1")
        self.scrolled_panel.SetAutoLayout(1)
        self.scrolled_panel.SetupScrolling()

        self.exam_info = exam
        self.file = file
        self.question = {}

        year, semester, ydl, exam_type = self.exam_info["year"], self.exam_info["semester"], self.exam_info["ydl"], self.exam_info["exam"]
        questions = self.exam_info["questions"]

        # TopSizer
        top_sizer = wx.GridSizer(1, 2, 0, 0)
        year_sem = wx.StaticText(self.panel, wx.ID_ANY, str(year) + " " + str(semester))
        exam_name = wx.StaticText(self.panel, wx.ID_ANY, "YDL" + str(ydl) + " "  + str(exam_type))
        top_sizer.Add(year_sem, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        top_sizer.Add(exam_name, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        scrollable_sizer = wx.BoxSizer(wx.VERTICAL)

        q_lbl = wx.StaticText(self.panel, wx.ID_ANY, "Soru:")
        self.q_input = wx.TextCtrl(self.panel, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        ca_lbl = wx.StaticText(self.panel, wx.ID_ANY, u"Doğru Cevap:")
        self.ca_input = wx.TextCtrl(self.panel, wx.ID_ANY, "")
        wa1_lbl = wx.StaticText(self.panel, wx.ID_ANY, u"Yanlış Cevap 1:")
        self.wa1_input = wx.TextCtrl(self.panel, wx.ID_ANY, "")
        wa2_lbl = wx.StaticText(self.panel, wx.ID_ANY, u"Yanlış Cevap 2:")
        self.wa2_input = wx.TextCtrl(self.panel, wx.ID_ANY, "")
        wa3_lbl = wx.StaticText(self.panel, wx.ID_ANY, u"Yanlış Cevap 3:")
        self.wa3_input = wx.TextCtrl(self.panel, wx.ID_ANY, "")

        scrollable_sizer.Add(q_lbl, 0, 0, 0)
        scrollable_sizer.Add(self.q_input, 0, wx.EXPAND, 0)
        scrollable_sizer.Add(ca_lbl, 0, 0, 0)
        scrollable_sizer.Add(self.ca_input, 0, wx.EXPAND, 0)
        scrollable_sizer.Add(wa1_lbl, 0, 0, 0)
        scrollable_sizer.Add(self.wa1_input, 0, wx.EXPAND, 0)
        scrollable_sizer.Add(wa2_lbl, 0, 0, 0)
        scrollable_sizer.Add(self.wa2_input, 0, wx.EXPAND, 0)
        scrollable_sizer.Add(wa3_lbl, 0, 0, 0)
        scrollable_sizer.Add(self.wa3_input, 0, wx.EXPAND, 0)

        bottom_sizer = wx.GridSizer(2, 2, 0, 0)

        qnum_lbl = wx.StaticText(self.panel, wx.ID_ANY, u"Soru sayısı:")
        qnum_info = wx.StaticText(self.panel, wx.ID_ANY, "1/25")
        self.q_input_exit = wx.Button(self.panel, wx.ID_ANY, u"Kaydetmeden Çık")
        self.save_question = wx.Button(self.panel, wx.ID_ANY, u"Kaydet ve İlerle")
        self.Bind(wx.EVT_BUTTON, self.onNextPage, self.save_question)

        bottom_sizer.Add(qnum_lbl, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        bottom_sizer.Add(qnum_info, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        bottom_sizer.Add(self.q_input_exit, 0, wx.EXPAND, 0)
        bottom_sizer.Add(self.save_question, 0, wx.EXPAND, 0)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(top_sizer)
        main_sizer.Add(scrollable_sizer, 1, wx.EXPAND)
        main_sizer.Add(bottom_sizer)

        self.panel.SetSizer(main_sizer)

        self.scrolled_panel.Layout()
        self.scrolled_panel.SetupScrolling()
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
