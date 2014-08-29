#coding:UTF-8

import wx

class notepad:
    def __init__(self):
        self.ID_NEW_FILE = 1
        self.ID_OPEN = 2
        self.ID_SAVE = 3
        self.ID_SAVEAS = 4
        self.ID_QUIT = 5

        self.ID_FONT = 6
        self.ID_BACDGROUND = 7
        
        print "class init !"
        
    #创建一个记事本
    def createNotepad(self):
        self.frame = wx.Frame(None,-1,'记事本'.decode('UTF-8'))
        self.frame.Center()

        self.notepadContent()
        self.notepadMenu()
                
        self.frame.Show()
    #添加文本框
    def notepadContent(self):
        self.textArea = wx.TextCtrl(self.frame,0,"记事本".decode('UTF-8'),style=wx.TE_MULTILINE)

    #添加菜单
    def notepadMenu(self):
        self.menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        
        newfileItem = fileMenu.Append(self.ID_NEW_FILE,'新建...'.decode('UTF-8'))
        openItem = fileMenu.Append(self.ID_OPEN,'打开...'.decode('UTF-8'))
        saveItem = fileMenu.Append(self.ID_SAVE,'保存'.decode('UTF-8'))
        savessItem = fileMenu.Append(self.ID_SAVEAS,'另存为...'.decode('UTF-8'))
        quitItem = fileMenu.Append(self.ID_QUIT,'退出'.decode('UTF-8'))

        settingingMenu = wx.Menu()
        fontItem = settingingMenu.Append(self.ID_FONT,'字体...'.decode('UTF-8'))
        fontItem = settingingMenu.Append(self.ID_BACDGROUND ,'背景色'.decode('UTF-8'))

        copyrightMenu = wx.Menu()
        
        self.menubar.Append(fileMenu,'文件'.decode('UTF-8'))
        self.menubar.Append(settingingMenu,'设置'.decode('UTF-8'))
        self.menubar.Append(copyrightMenu,'版权'.decode('UTF-8'))

        self.frame.Bind(wx.EVT_MENU, self.openFileChooser,openItem)
        self.frame.SetMenuBar(self.menubar)

    #选择文件
    def openFileChooser(self,arg):
        print "hello world !"
        print self
        print arg

    #显示记事本
    def notepadShow(self):
        app = wx.App()
        self.createNotepad()
        app.MainLoop()
         
notepad().notepadShow()
