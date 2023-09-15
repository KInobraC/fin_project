from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout

dodatok = QApplication([])

window = QWidget()

text = QLabel('Яка напойпопулярніша гра 2019')
btn1 = QRadioButton("Browl stors")
btn2 = QRadioButton("Maynkrft")
btn3 = QRadioButton("GtU")
btn4 = QRadioButton("tik tik ")
vline = QVBoxLayout()
hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()

hline1.addWidget(text)
hline2.addWidget(btn1)
hline2.addWidget(btn2)
hline3.addWidget(btn3)
hline3.addWidget(btn4)
vline.addLayout(hline1)
vline.addLayout(hline2)
vline.addLayout(hline3)


window.show()

dodatok.exec_()