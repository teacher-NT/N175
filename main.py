import os
os.system("cls")

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
font1 = QFont("Arial", 30)

app = QApplication([])

window = QWidget()
window.setWindowTitle("Mening birinchi oynali dasturim")
window.setGeometry(400,400, 920, 600)
window.setStyleSheet("background-color: #4bfc1e;")

label = QLabel(window)
label.setText("Samandarning qo'li sinibdi")
label.setFont(font1)
label.setFixedWidth(920)
label.move(50, 50)
label.setStyleSheet("color: white;")



edit = QLineEdit(window)
edit.setGeometry(100,150, 200,50)
edit.setPlaceholderText("🔍Qidirish...")
edit.setStyleSheet("background-color: white; font-size:20px;")

def func1():
    global label
    n = edit.text()
    label.setText(f"Salom {n}")

btn1 = QPushButton(window)
btn1.setText("Press me!")
btn1.setGeometry(400,150, 100, 50)
btn1.setStyleSheet("background-color: white; font-size:20px;")
btn1.clicked.connect(func1)

window.show()

app.exec_()