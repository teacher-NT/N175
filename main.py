import os
os.system("cls")
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, QLabel, 
                             QPushButton,
                             QHBoxLayout, QVBoxLayout,
                             QComboBox, QCheckBox)

style1 = "color: white;font-size: 18px;"

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.Vlayout = QVBoxLayout()
        self.setWindowTitle("My Windows")
        self.setStyleSheet("background-color: grey;")
        label = QLabel()
        label.setText("Restoran menyusi")
        label.setStyleSheet("color:white;font-size:28px;")
        self.Vlayout.addWidget(label)
        self.combo_qushish()
        self.choice_label = QLabel()
        self.choice_label.setText("Tanlangan ovqat!")
        self.choice_label.setStyleSheet(style1)
        self.Vlayout.addWidget(self.choice_label)

        self.drink_label = QLabel("Tanlangan ichimliklar!")
        self.drink_label.setStyleSheet(style1)
        self.Vlayout.addWidget(self.drink_label)

        btn2 = QPushButton()
        btn2.setText("Tanlash")
        btn2.setStyleSheet("background-color: yellow;")
        btn2.clicked.connect(self.show_choice)
        self.Vlayout.addWidget(btn2)

        self.add_checkbox()
        
        

        btn3 = QPushButton()
        btn3.setText("Ichimlik tanlash")
        btn3.setStyleSheet("background-color: green;")
        btn3.clicked.connect(self.show_drinks)
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

    def add_checkbox(self):
        self.check1 = QCheckBox("Qora Choy")
        self.check2 = QCheckBox("Ko'k Choy")
        self.check3 = QCheckBox("Limon Choy")
        self.check4 = QCheckBox("Coffee")
        self.check5 = QCheckBox("Cola")
        self.check6 = QCheckBox("Fanta")
        self.Vlayout.addWidget(self.check1)
        self.Vlayout.addWidget(self.check2)
        self.Vlayout.addWidget(self.check3)
        self.Vlayout.addWidget(self.check4)
        self.Vlayout.addWidget(self.check5)
        self.Vlayout.addWidget(self.check6)

    def show_drinks(self):
        res = ""
        if self.check1.isChecked():
            res += f"{self.check1.text()}, "
        if self.check2.isChecked():
            res += f"{self.check2.text()}, "
        if self.check3.isChecked():
            res += f"{self.check3.text()}, "
        if self.check4.isChecked():
            res += f"{self.check4.text()}, "
        if self.check5.isChecked():
            res += f"{self.check5.text()}, "
        if self.check6.isChecked():
            res += f"{self.check6.text()}, "
        self.drink_label.setText(f"Tanlangan ichimliklar: {res}")
        
app = QApplication([])
win = MyWindow()
app.exec_()
