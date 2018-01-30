#PyQt5 箱布局
import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QApplication

class BoxDemo(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        okButton=QPushButton('确定')
        cancelButton=QPushButton('取消')

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('箱子布局')
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    bd=BoxDemo()
    sys.exit(app.exec_())

