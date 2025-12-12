import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)

class SecondWindow(QWidget):
    def __init__(self, num):
        super().__init__()
        self.setFixedSize(900,600)
        label1 = QLabel(self)
        label1.setText(f"Men {num}-oynaman")
        label1.setStyleSheet("font-size:30px;")



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.windows = []
        self.setFixedSize(600,900)
        layout = QVBoxLayout()
        label1 = QLabel("Bu asosiy oyna")
        label1.setStyleSheet("font-size:20px;")
        layout.addWidget(label1)
        btn1 = QPushButton("Keyingi oynani ochish")
        btn1.setStyleSheet("background-color: green; color:white;font-size:12px;")
        btn1.clicked.connect(self.open_other_window)
        layout.addWidget(btn1)
        self.setLayout(layout)
        self.show()
    
    def open_other_window(self):
        num = len(self.windows)+1
        win = MainWindow()
        self.windows.append(win)
        self.windows[-1].show()


app = QApplication([])
win = MainWindow()
app.exec_()