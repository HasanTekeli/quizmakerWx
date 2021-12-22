import wx


def choose_exam(self):
    with wx.FileDialog(self, "Sınavı Seç", wildcard="JSON files (*.json)|*.json",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return  # the user changed their mind

        # Proceed loading the file chosen by the user
        pathname = fileDialog.GetPath()
        try:
            with open(pathname, 'r') as file:
                print("chosen file: ", file)
        except IOError:
            wx.LogError("Cannot open file '%s'." % file)