#绝对定位
import sys
from PyQt5.QtWidgets import QWidget,QLabel,QApplication

class Absolute(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lb1=QLabel('第一个',self)
        lb1.move(15,10)

        lb2=QLabel('第二个',self)
        lb2.move(35,40)

        lb3=QLabel('第三个',self)
        lb3.move(55,70)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('绝对定位')
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ab = Absolute()
    sys.exit(app.exec_())

