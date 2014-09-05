#coding:UTF-8

import wx

class notepad:
    def __init__(self):
        print "do : class init !"
        self.ID_NEW_FILE = 1
        self.ID_OPEN = 2
        self.ID_SAVE = 3
        self.ID_SAVEAS = 4
        self.ID_QUIT = 5
        self.ID_FONT = 6
        self.ID_BACDGROUND = 7
        self.notepadText = ''
        
        print "finish : class init !"
        
    #创建一个记事本
    def createNotepad(self):
        print "do : createNotepad"
        self.frame = wx.Frame(None,-1,'记事本'.decode('UTF-8'))
        self.frame.Center()

        self.notepadContent()
        self.notepadMenu()
                
        self.frame.Show()
        print "finish : createNotepad"
        
    #添加文本框
    def notepadContent(self):
        print "do : notepadContent"
        self.textArea = wx.TextCtrl(self.frame,0,"记事本".decode('UTF-8'),style=wx.TE_MULTILINE)
        print "finish : notepadContent"
        
    #添加菜单
    def notepadMenu(self):
        print "do : notepadMenu"
        self.menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        
        newfileItem = fileMenu.Append(self.ID_NEW_FILE,'新建...'.decode('UTF-8'))
        openItem = fileMenu.Append(self.ID_OPEN,'打开...'.decode('UTF-8'))
        saveItem = fileMenu.Append(self.ID_SAVE,'保存'.decode('UTF-8'))
        savessItem = fileMenu.Append(self.ID_SAVEAS,'另存为...'.decode('UTF-8'))
        quitItem = fileMenu.Append(self.ID_QUIT,'退出'.decode('UTF-8'))

        settingingMenu = wx.Menu()
        fontItem = settingingMenu.Append(self.ID_FONT,'字体...'.decode('UTF-8'))

        backgroundMenu = wx.Menu()        
        settingingMenu.AppendMenu(wx.ID_ANY ,'背景色'.decode('UTF-8'),backgroundMenu)
        backgroundMenu.AppendRadioItem(wx.ID_ANY,'默认'.decode('UTF-8'))
        backgroundMenu.AppendRadioItem(wx.ID_ANY,'黑色'.decode('UTF-8'))
        backgroundMenu.AppendRadioItem(wx.ID_ANY,'蓝色'.decode('UTF-8'))
        backgroundMenu.AppendRadioItem(wx.ID_ANY,'粉红色'.decode('UTF-8'))
        backgroundMenu.AppendRadioItem(wx.ID_ANY,'绿色'.decode('UTF-8'))
        backgroundMenu.AppendRadioItem(wx.ID_ANY,'灰色'.decode('UTF-8'))
        backgroundMenu.AppendRadioItem(wx.ID_ANY,'橙色'.decode('UTF-8'))
        backgroundMenu.AppendRadioItem(wx.ID_ANY,'黄色'.decode('UTF-8'))
        
        copyrightMenu = wx.Menu()
        
        self.menubar.Append(fileMenu,'文件'.decode('UTF-8'))
        self.menubar.Append(settingingMenu,'设置'.decode('UTF-8'))
        self.menubar.Append(copyrightMenu,'版权'.decode('UTF-8'))

        self.frame.Bind(wx.EVT_MENU, self.openFileChooser,openItem)
        self.frame.SetMenuBar(self.menubar)

        print "finish : notepadMenu"

        #菜单绑定事件
        self.frame.Bind(wx.EVT_MENU,self.menuQuit,quitItem)
        self.frame.Bind(wx.EVT_MENU,self.menuOpenfile,openItem)
        self.frame.Bind(wx.EVT_MENU,self.menuSaveAs,savessItem)

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

    #（菜单）退出方法
    def menuQuit(self,arg):
        self.frame.Close()

    #(菜单)打开文件方法
    def menuOpenfile(self,arg):
        print "do : menuOpenfile"
        self.openDialog =  wx.FileDialog(self.frame,'打开'.decode('UTF-8'),'.')
        self.openDialog.ShowModal()
        filePath = self.openDialog.GetPath()
        
        #print filePath
        self.textArea.LoadFile(filePath)
        #self.notepadText = open(filePath,'r').readlines() 
        #print self.notepadText
        print "finish : menuOpenfile"

    #(菜单)打开文件方法
    def menuSaveAs(self,arg):
        print "do : menuSaveAs"
        self.saveDialog =  wx.FileDialog(self.frame,'保存'.decode('UTF-8'),'.',style=wx.FD_SAVE)
        self.saveDialog.ShowModal()

        filePath = self.saveDialog.GetPath()
        self.notepadText = self.textArea.GetLineText(self.textArea.GetNumberOfLines())
        print self.notepadText
     
        __file = open(filePath, "w")
        __file.write(str(self.notepadText))
        __file.close()
        
        print "finish : menuSaveAs"

    def menuSave(self,arg):
        print "do : menuSave"
        
         
notepad().notepadShow()
