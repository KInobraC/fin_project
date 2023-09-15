from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import*

app = QApplication([])

window = QWidget()
text = QLabel('Натипсні щоб дізнатися переможця')
winner = QLabel('?')
button = QPushButton('Згенерувати')

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button)
window.setLayout(line)

def win():
    ran = randint(1, 100)
    winner.setText(str(ran))

button.clicked.connect(win)

window.show()
app.exec_()