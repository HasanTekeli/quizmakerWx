import os.path

import wx
import sys
import pathlib
import json


def get_datadir() -> pathlib.Path:

    """
    Returns a parent directory path
    where persistent application data can be stored.

    # linux: ~/.local/share
    # macOS: ~/Library/Application Support
    # windows: C:/Users/<USER>/AppData/Roaming
    """

    home = pathlib.Path.home()

    if sys.platform == "win32":
        return home / "AppData/Roaming"
    elif sys.platform.startswith == "linux":
        return home / ".local/share"
    elif sys.platform == "darwin":
        return home / "Library/Application Support"


class NewExam(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: newExam.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("Yeni Sınav")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        grid_sizer_1 = wx.GridSizer(6, 2, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        year_lbl = wx.StaticText(self.panel_1, wx.ID_ANY, u"Öğretim Yılı:")
        grid_sizer_1.Add(year_lbl, 0, wx.ALIGN_RIGHT, 0)

        self.year_input = wx.TextCtrl(self.panel_1, wx.ID_ANY, "2021-2022")
        grid_sizer_1.Add(self.year_input, 0, 0, 0)

        sem_lbl = wx.StaticText(self.panel_1, wx.ID_ANY, u"Dönem:")
        grid_sizer_1.Add(sem_lbl, 0, wx.ALIGN_RIGHT, 0)

        self.sem_choice = wx.Choice(self.panel_1, wx.ID_ANY, choices=[u"Güz", "Bahar"])
        self.sem_choice.SetSelection(0)
        grid_sizer_1.Add(self.sem_choice, 0, 0, 0)

        ydl_lbl = wx.StaticText(self.panel_1, wx.ID_ANY, "YDL:")
        grid_sizer_1.Add(ydl_lbl, 0, wx.ALIGN_RIGHT, 0)

        self.ydl_choice = wx.Choice(self.panel_1, wx.ID_ANY, choices=["183", "184", "185", "186"])
        self.ydl_choice.SetSelection(0)
        grid_sizer_1.Add(self.ydl_choice, 0, 0, 0)

        exam_lbl = wx.StaticText(self.panel_1, wx.ID_ANY, u"Sınav:")
        grid_sizer_1.Add(exam_lbl, 0, wx.ALIGN_RIGHT, 0)

        self.exam_choice = wx.Choice(self.panel_1, wx.ID_ANY, choices=["Vize", "Final", "Mazeret", u"Bütünleme"])
        self.exam_choice.SetSelection(0)
        grid_sizer_1.Add(self.exam_choice, 0, 0, 0)

        self.cancel_btn = wx.Button(self.panel_1, wx.ID_ANY, u"İptal Et ve Çık")
        grid_sizer_1.Add(self.cancel_btn, 0, wx.ALIGN_BOTTOM | wx.EXPAND, 0)

        self.save_btn = wx.Button(self.panel_1, wx.ID_ANY, u"Kaydet ve Oluştur")
        grid_sizer_1.Add(self.save_btn, 0, wx.ALIGN_BOTTOM | wx.EXPAND, 0)
        self.save_btn.Bind(wx.EVT_BUTTON, self.write_json)

        self.panel_1.SetSizer(grid_sizer_1)

        self.Layout()

        # end wxGlade

    def write_json(self, e):
        year = self.year_input.GetValue()
        sem_selection = self.sem_choice.GetSelection()
        ydl_selection = self.ydl_choice.GetSelection()
        exam_selection = self.exam_choice.GetSelection()
        sem_choice = self.sem_choice.GetString(sem_selection)
        ydl_choice = self.ydl_choice.GetString(ydl_selection)
        exam_choice = self.exam_choice.GetString(exam_selection)

        datadir = get_datadir() / "quizmaker"


        # Create datadir:
        try:
            datadir.mkdir(parents=True)
        except FileExistsError:
            pass

        question_dict = {}
        exam_filename = year + sem_choice + ydl_choice + exam_choice + ".json"

        exam_json = json.dumps(question_dict, indent=4)
        if os.path.isfile(os.path.join(datadir, exam_filename)):
            print("Aynı isimde başka sınav bulundu: ", exam_filename)
        else:
            with open(os.path.join(datadir, exam_filename), "w") as outfile:
                outfile.write(exam_json)

# end of class newExam