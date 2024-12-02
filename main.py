import sys
import math
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen




circles = []
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.clicked.clicked.connect(self.generate_circles)

    def generate_circles(self):
        for _ in range(random.randint(1, 1)):
            radius = random.randint(10, 50)
            x = random.randint(radius, self.width() - radius)
            y = random.randint(radius, self.height() - radius)
            circles.append((x, y, radius))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in circles:
            x, y, radius = circle
            brush = QBrush(QColor("yellow"))
            painter.setBrush(brush)
            painter.drawEllipse(x - radius, y - radius, 2 * radius, 2 * radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())