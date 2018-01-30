import os,sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QMessageBox,QTextEdit,QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('记事本')
        icon=os.path.dirname(__file__)+'\logo.png'
        #icon=icon.replace('\\','/')
        #print(icon)
        self.setWindowIcon(QIcon(icon))
        '''
        qbtn=QPushButton('测试',self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        '''
        #创建文本编辑地下
        textEdit=QTextEdit()
        self.setCentralWidget(textEdit)     

        saveAction = QAction('保存', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('保存当前内容!')

        exitAction=QAction('退出',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出应用程序!')
        exitAction.triggered.connect(self.close)
        
      
        menubar=self.menuBar()
        #文件
        fileMenu=menubar.addMenu('&文件(F)')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(saveAction)
        #编辑
        editMenu=menubar.addMenu('&编辑(E)')
        #格式
        formatMenu=menubar.addMenu('&格式(O)')
        #查看
        viewMenu=menubar.addMenu('&查看(V)')
        #帮助
        helpMenu=menubar.addMenu('&帮助(H)')
        
        #toobar=self.addToolBar('退出')
        #toobar.addAction(exitAction)
        #显示状态栏
        self.statusBar()
        self.show()
    
    def closeEvent(self,event):
        reply=QMessageBox.question(self,'提示','你确定要退出么?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
