import os
os.system("cls")
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, QLabel, 
                             QPushButton,
                             QHBoxLayout, QVBoxLayout,
                             QComboBox, QCheckBox,
                             QRadioButton, QMessageBox)

style1 = "color: white;font-size: 18px;"

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.Vlayout = QVBoxLayout()
        self.Hlayout = QHBoxLayout()
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

        self.add_checkbox()
        self.Vlayout.addLayout(self.Hlayout)
        
        btn2 = QPushButton()
        btn2.setText("Ovqat tanlash")
        btn2.setStyleSheet("background-color: yellow;")
        btn2.clicked.connect(self.show_choice)
        self.Vlayout.addWidget(btn2)

        btn3 = QPushButton()
        btn3.setText("Ichimlik tanlash")
        btn3.setStyleSheet("background-color: green;")
        btn3.clicked.connect(self.show_drinks)
        self.Vlayout.addWidget(btn3)
        
        self.show_radio()

        btn4 = QPushButton("Buyurtma berish")
        btn4.setStyleSheet("background-color: blue")
        btn4.clicked.connect(self.buyurtma)
        self.Vlayout.addWidget(btn4)

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
        self.Hlayout.addWidget(self.menyu)

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
        self.Hlayout.addWidget(self.check1)
        self.Hlayout.addWidget(self.check2)
        self.Hlayout.addWidget(self.check3)
        self.Hlayout.addWidget(self.check4)
        self.Hlayout.addWidget(self.check5)
        self.Hlayout.addWidget(self.check6)

    def show_drinks(self):
        self.res = ""
        if self.check1.isChecked():
            self.res += f"{self.check1.text()}, "
        if self.check2.isChecked():
            self.res += f"{self.check2.text()}, "
        if self.check3.isChecked():
            self.res += f"{self.check3.text()}, "
        if self.check4.isChecked():
            self.res += f"{self.check4.text()}, "
        if self.check5.isChecked():
            self.res += f"{self.check5.text()}, "
        if self.check6.isChecked():
            self.res += f"{self.check6.text()}, "
        self.drink_label.setText(f"Tanlangan ichimliklar: {self.res}")
        
    def show_radio(self):
        self.naqd = QRadioButton("Naqd")
        self.terminal = QRadioButton("Terminal")
        self.onlayn = QRadioButton("Onlayn")

        self.Vlayout.addWidget(self.naqd)
        self.Vlayout.addWidget(self.terminal)
        self.Vlayout.addWidget(self.onlayn)
    
    def buyurtma(self):
        pay = None
        if self.naqd.isChecked():
            pay = "Naqd"
        elif self.terminal.isChecked():
            pay = "Terminal"
        elif self.onlayn.isChecked():
            pay = "Onlayn"
        QMessageBox.information(self,"Info", 
                                f"Sizning buyurtmangiz\n{self.choice_label.text()}\nIchimliklar: {self.res}\nTo'lov: {pay}")
app = QApplication([])
win = MyWindow()
app.exec_()
