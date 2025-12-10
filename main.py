import os
os.system("cls")
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, QLabel, 
                             QPushButton,
                             QHBoxLayout, QVBoxLayout)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("My Windows")
        self.setStyleSheet("background-color: black;")
        label = QLabel()
        label.setText("Bu oynali dastur")
        label.setStyleSheet("color:white;")
        layout.addWidget(label)
        btn = QPushButton()
        btn.setText("Press me!")
        btn.setStyleSheet("background-color: red;")
        layout.addWidget(btn)
        btn2 = QPushButton()
        btn2.setText("Press me!")
        btn2.setStyleSheet("background-color: yellow;")
        layout.addWidget(btn2)

        btn3 = QPushButton()
        btn3.setText("Press me!")
        btn3.setStyleSheet("background-color: green;")
        layout.addWidget(btn3)
        self.setLayout(layout)


        self.show()


app = QApplication([])
win = MyWindow()
app.exec_()
