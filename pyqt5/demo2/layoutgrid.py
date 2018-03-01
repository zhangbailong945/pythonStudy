import sys
from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QTextEdit,QGridLayout,QApplication

class Reg(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        title=QLabel('标题:')
        author=QLabel('作者:')
        review=QLabel('内容:')

        titleEdit=QLineEdit()
        authorEdit=QLineEdit()
        reviewEdit=QTextEdit()

        #创建网格布局
        grid=QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)

        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)

        self.setLayout(grid)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('网格布局')
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    reg=Reg()
    sys.exit(app.exec_())
