#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.1.0pre on Mon Dec 20 11:28:06 2021
#

import wx
import json
from pkg import NewExam, choose_exam

def read_settings():
    settings_file = open("data/settings.json")
    settings_json = json.load(settings_file)
    settings = settings_json["settings"][0]
    uni_name, school_name, number_of_questions = settings["schoolName"], settings["depName"], settings["numberOfQuestions"]
    return uni_name, school_name, number_of_questions


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: mainFrame.__init__
        uni_name, school_name, number_of_questions = read_settings()
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("QuizMaker")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.GridSizer(5, 1, 0, 0)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

        uni_name = wx.StaticText(self.panel_1, wx.ID_ANY, uni_name)
        sizer_3.Add(uni_name, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        school_name = wx.StaticText(self.panel_1, wx.ID_ANY, school_name)
        sizer_3.Add(school_name, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        qnum = wx.StaticText(self.panel_1, wx.ID_ANY, str(number_of_questions))
        sizer_3.Add(qnum, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.newBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Yeni Sınav Oluştur")
        sizer_1.Add(self.newBtn, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.openBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Sınavı Aç")
        sizer_1.Add(self.openBtn, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        grid_sizer_1 = wx.GridSizer(1, 1, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        self.reportlab = wx.Button(self.panel_1, wx.ID_ANY, u"Sınav Seç ve PDF oluştur")
        self.reportlab.SetMinSize((200, 21))
        grid_sizer_1.Add(self.reportlab, 0, wx.ALIGN_CENTER, 0)

        self.closeBtn = wx.Button(self.panel_1, wx.ID_ANY, "Kapat")
        sizer_1.Add(self.closeBtn, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.newExam, self.newBtn)
        self.Bind(wx.EVT_BUTTON, self.chooseExam, self.openBtn)
        self.closeBtn.Bind(wx.EVT_BUTTON, self.onQuit)


        # end wxGlade

    def onQuit(self, event):
        self.Close()

    def newExam(self, event):  # wxGlade: mainFrame.<event_handler>
        new = NewExam(None, wx.ID_ANY, "")
        # self.Hide()
        new.Show()

    def chooseExam(self, event):  # wxGlade: mainFrame.<event_handler>
        choose_exam(self)

# end of class mainFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
