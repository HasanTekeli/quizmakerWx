import os.path
import wx
import sys
import pathlib
import json
from .qEntry import QuestionEntry


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
        return home / "Library/ApplicationSupport"


class NewExam(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: NewExam.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((500, 400))
        self.SetTitle("Yeni Sınav")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        grid_sizer_1 = wx.GridSizer(8, 2, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        #grid_sizer_1.Add((0, 0), 0, 0, 0)

        sizer_h = wx.BoxSizer(wx.VERTICAL)
        self.warning_lbl = wx.StaticText(self.panel_1, wx.ID_ANY, u"Bu sınav zaten var! Sınavı yüklemeyi deneyin!")
        self.warning_lbl.SetBackgroundColour((255, 0, 0))
        sizer_h.Add(self.warning_lbl, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(sizer_h, 1, wx.EXPAND, 0)
        self.warning_lbl.Hide()

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

        answerkey_lbl = wx.StaticText(self.panel_1, wx.ID_ANY, u"Cevap Anahtarı:\nMax:25")
        grid_sizer_1.Add(answerkey_lbl, 0, wx.ALIGN_RIGHT, 0)
        self.answerkey = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.answerkey.SetMaxLength(25)
        grid_sizer_1.Add(self.answerkey, 0, wx.EXPAND, 0)

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
        answerkey = self.answerkey.GetValue()
        questions = []
        for i in range(25):
            q_id = i+1
            question = []
            q = {"question": "", "ca": "", "wa1": "", "wa2": "", "wa3": ""}
            question.append(q_id)
            question.append(q)
            questions.append(question)

        datadir = get_datadir() / "quizmaker"

        # Create datadir:
        try:
            datadir.mkdir(parents=True)
        except FileExistsError:
            pass

        question_dict = {'exam': []}
        question_dict['exam'].append({
            "year": year,
            "semester": sem_choice,
            "ydl": ydl_choice,
            "exam": exam_choice,
            "answerkey": answerkey,
            "questions": questions
        })
        exam_filename = year + sem_choice + ydl_choice + exam_choice + ".json"
        full_path = os.path.join(datadir, exam_filename)
        exam_json = json.dumps(question_dict, indent=4, ensure_ascii=False)
        if os.path.isfile(full_path):
            self.warning_lbl.Show()
            print("Aynı isimde başka sınav bulundu: ", exam_filename)
        else:
            with open(full_path, "w") as outfile:
                outfile.write(exam_json)
            self.Close()

# end of class NewExam