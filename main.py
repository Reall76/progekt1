from random import randint

from PyQt6.uic import loadUi 

from PyQt6.QtWidgets import QApplication, QMainWindow,  QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("./untitled.ui", self)

        self.knopka1 = self.findChild(QPushButton, "knopka1")
        
        self.knopka1.clicked.connect(self.hello)

        self.label = self.findChild(QLabel, "label")

        self.count = 0


    def hello(self):
        print("ku")
        self.label.setText(str(randint(1,999)))




if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()