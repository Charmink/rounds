import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import choice
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)
        uic.loadUi('untitled.ui', self)
        self.setWindowTitle('Рисование')
        self.show()
        self.figure = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.figure = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawKrug(qp)
        qp.end()

    def drawKrug(self, qp):
        if self.figure:
            qp.setBrush(QColor(255, 255, 0))
            d = choice(range(10, 50))
            qp.drawEllipse(choice(range(400)), choice(range(400)), d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
