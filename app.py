from pkg.buttons import buttons
import wx
import os
import json
from pkg.entry import entry

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        f = open('./settings.json')
        data = json.load(f)
        self.numberOfQuestions = data['settings'][0]['numberOfQuestions']
        
        self.InitUI()
    
    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()
        
        #Quit Button:
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, 'Quit')
        fileMenu.Append(qmi)
        self.Bind(wx.EVT_MENU, self.onQuit, qmi)
        
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((400,600))
        self.SetTitle('QuizMaker')
        self.Centre()

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        #entry(panel, vbox)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        buttons(self, panel, hbox1, hbox2)

        vbox.Add((0,0), 1, wx.EXPAND)
        vbox.Add(hbox1, 0, wx.CENTER)
        vbox.Add(hbox2, 0, wx.CENTER)
        vbox.Add((0,0), 1, wx.EXPAND)
        vbox.Add((-1, 25))
        
        vbox.AddStretchSpacer()
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox6.Add(btn1)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox6.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox6, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        panel.SetSizer(vbox)
    
    def onQuit(self, e):
        self.Close()

    def onOpen(self, e):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, '', '*.*', wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def onNew(self, e):
        print("hellooooo")

def main():
    app = wx.App()
    frame = MainWindow(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()