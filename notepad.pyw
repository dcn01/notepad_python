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
        self.filePath = ''
        self.file = None       
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
        self.textArea = wx.TextCtrl(self.frame,0,''.decode('UTF-8'),style=wx.TE_MULTILINE)
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
        aboutItem = copyrightMenu.Append(wx.ID_ANY,'版权...'.decode('UTF-8'))
        self.menubar.Append(fileMenu,'文件'.decode('UTF-8'))
        self.menubar.Append(settingingMenu,'设置'.decode('UTF-8'))
        self.menubar.Append(copyrightMenu,'关于'.decode('UTF-8'))
        self.frame.SetMenuBar(self.menubar)        

        #菜单绑定事件
        self.frame.Bind(wx.EVT_MENU,self.menuQuit,quitItem)
        self.frame.Bind(wx.EVT_MENU,self.menuOpenfile,openItem)
        self.frame.Bind(wx.EVT_MENU,self.menuSaveAs,savessItem)
        self.frame.Bind(wx.EVT_MENU,self.menuSave,saveItem)
        self.frame.Bind(wx.EVT_MENU,self.newfile,newfileItem)
        self.frame.Bind(wx.EVT_MENU,self.mycopyRight,aboutItem)
        self.frame.Bind(wx.EVT_MENU,self.fontSet,fontItem)
        __menuItems = backgroundMenu.GetMenuItems()
        for i in range(0,len(__menuItems)):
            self.frame.Bind(wx.EVT_MENU, lambda evt, mark=i : self.setbackgroundColor(evt,__menuItems),__menuItems[i])                
        print "finish : notepadMenu"

    #显示记事本
    def notepadShow(self):
        print "do : notepadShow"
        app = wx.App()
        self.createNotepad()
        app.MainLoop()
        print "finish : notepadShow"

    #（菜单）退出方法
    def menuQuit(self,arg):
        self.frame.Close()

    #(菜单)打开文件方法
    def menuOpenfile(self,arg):
        print "do : menuOpenfile"
        self.openDialog =  wx.FileDialog(self.frame,'打开'.decode('UTF-8'),'.')
        self.openDialog.ShowModal()
        filePath = self.openDialog.GetPath()
        if filePath != '':
            #print filePath
            self.textArea.LoadFile(filePath)
            self.filePath = filePath
            #self.notepadText = open(filePath,'r').readlines() 
            #print self.notepadText
        
        print "finish : menuOpenfile"

    #(菜单)打开文件方法
    def menuSaveAs(self,arg):
        print "do : menuSaveAs"
        self.saveDialog =  wx.FileDialog(self.frame,'保存'.decode('UTF-8'),'.',style=wx.FD_SAVE)
        self.saveDialog.ShowModal()
        filePath = self.saveDialog.GetPath()
        self.filePath = filePath
        if filePath != '':
            self.notepadText = self.textArea.GetValue()
            __file = open(filePath, "w")
            __file.write(self.notepadText.encode('UTF-8'))
            __file.close()        
        print "finish : menuSaveAs"

    #保存文件方法
    def menuSave(self,arg):
        print "do : menuSave"
        if self.file != None:
            self.file = open(self.filePath, "w")
        else:
            self.saveDialog =  wx.FileDialog(self.frame,'保存'.decode('UTF-8'),'.',style=wx.FD_SAVE)
            self.saveDialog.ShowModal()
            filePath = self.saveDialog.GetPath()
            if filePath != '':
                self.file = open(filePath, "w")
                self.filePath = filePath
        self.file.write(self.textArea.GetValue().encode('UTF-8'))
        self.file.close()
        print "finish : menuSave"

    #新建文件方法
    def newfile(self,arg):
        print "do : newfile"
        if self.file == None:
            self.saveDialog =  wx.FileDialog(self.frame,'保存'.decode('UTF-8'),'.',style=wx.FD_SAVE)
            self.saveDialog.ShowModal()
            filePath = self.saveDialog.GetPath()
            if filePath != '':
                self.file = open(filePath, "w")
                self.filePath = filePath
                self.file.close()
                self.textArea.SetValue('')
        else:
            self.file = open(self.filePath, "w")   
            self.file.write(self.textArea.GetValue().encode('UTF-8'))
            self.file.close()   
            self.saveDialog =  wx.FileDialog(self.frame,'保存'.decode('UTF-8'),'.',style=wx.FD_SAVE)
            self.saveDialog.ShowModal()
            filePath = self.saveDialog.GetPath()
            if filePath != '':
                self.file = open(filePath, "w")
                self.filePath = filePath
                self.file.close()
                self.textArea.SetValue('')            
        print "finish : newfile"

    #显示版权信息方法
    def mycopyRight(self,arg):
        print "do : copyRight"
        dialog = wx. MessageDialog(self.frame,'Create : 2014/09/08\ncopyright nnc\n'.decode('UTF-8'),'消息'.decode('UTF-8'),wx.OK_DEFAULT)
        dialog.ShowModal()
        print "finish : copyRight"
        
    #设置字体方法
    def fontSet(self,arg):
        print "do : fontSet"
        font =  self.textArea.GetFont()
        color = self.textArea.GetForegroundColour()
        fontData = wx.FontData()
        fontData.SetInitialFont(font)
        fontData.SetColour(color)       
        dialog = wx.FontDialog(self.frame,fontData)       
        dialog.ShowModal()
        fontData = dialog.GetFontData()
        font = fontData.GetChosenFont()
        self.textArea.SetFont(font)
        self.textArea.SetForegroundColour(fontData.GetColour())
        print "finish : fontSet"

    def setbackgroundColor(self,arg,items):
        print "do : setbackgroundColor"
        colorNum = 0
        for i in range(0,len(items)):
            if items[i].IsChecked():
                colorNum = i
                break
        if colorNum == 0:
            self.textArea.SetBackgroundColour('White')
        elif colorNum == 1:
            self.textArea.SetBackgroundColour('Black')         
        elif colorNum == 2:
            self.textArea.SetBackgroundColour('Blue')
        elif colorNum == 3:
            self.textArea.SetBackgroundColour('Pink')
        elif colorNum == 4:
            self.textArea.SetBackgroundColour('Green')
        elif colorNum == 5:
            self.textArea.SetBackgroundColour('Grey')
        elif colorNum == 6:
            self.textArea.SetBackgroundColour('Orange')
        elif colorNum == 7:
            self.textArea.SetBackgroundColour('Yellow')
        self.textArea.Refresh()
        print "finish : setbackgroundColor"
    
notepad().notepadShow()


















