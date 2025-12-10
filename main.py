import os
os.system("cls")
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, QLabel, 
                             QPushButton,
                             QHBoxLayout, QVBoxLayout,
                             QComboBox)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.Vlayout = QVBoxLayout()
        self.setWindowTitle("My Windows")
        self.setStyleSheet("background-color: black;")
        label = QLabel()
        label.setText("Restoran menyusi")
        label.setStyleSheet("color:white;font-size:28px;")
        self.Vlayout.addWidget(label)
        self.combo_qushish()
        self.choice_label = QLabel()
        self.choice_label.setText("Tanlangan ovqat!")
        self.choice_label.setStyleSheet("color: white;font-size: 18px;")
        self.Vlayout.addWidget(self.choice_label)
        btn2 = QPushButton()
        btn2.setText("Tanlash")
        btn2.setStyleSheet("background-color: yellow;")
        btn2.clicked.connect(self.show_choice)
        self.Vlayout.addWidget(btn2)

        btn3 = QPushButton()
        btn3.setText("Press me!")
        btn3.setStyleSheet("background-color: green;")
        self.Vlayout.addWidget(btn3)
        

        self.setLayout(self.Vlayout)


        self.show()
    
    def combo_qushish(self):
        self.menyu = QComboBox()
        self.menyu.setStyleSheet("background-color: white;")
        # self.menyu.addItem("Shashlik")
        # self.menyu.addItem("Manti")
        # self.menyu.addItem("Palov")
        # self.menyu.addItem("Halim")
        # self.menyu.addItem("Norin")
        # self.menyu.addItem("Honim")
        # self.menyu.addItem("Qozonkabob")
        # self.menyu.addItem("Sho'rva")
        self.menyu.addItems(['Shashlik', 'Manti', 'Palov', 'Halim', 'Norin'])
        self.Vlayout.addWidget(self.menyu)

    def show_choice(self):
        curr = self.menyu.currentText()
        self.choice_label.setText(f"Tanlangan ovqat: {curr}!")

app = QApplication([])
win = MyWindow()
app.exec_()
