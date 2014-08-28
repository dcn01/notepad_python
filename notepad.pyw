#coding:UTF-8

import wx

class notepad:
    def __init__(self):
        print "class init !"
        
    #创建一个notepad
    def createNotepad(self):
        self.frame = wx.Frame(None,-1,'notepad')
        self.frame.Center()
        
        self.frame.Show()
        
        

    def notepadShow(self):
        app = wx.App()
        self.createNotepad()
        app.MainLoop()
         
notepad().notepadShow()
