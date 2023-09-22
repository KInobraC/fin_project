from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel,
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout,
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json
app = QApplication([])
window = QWidget()

field_text = QTextEdit()
lb_notes = QLabel("Список заміток")
lst_notes = QListWidget()
btn_note_create = QPushButton("Стровити замітку")
btn_note_del = QPushButton("Видалити замітку")
btn_note_save = QPushButton("Зберегти замітку")

lb_tags = QLabel("Список заміток")

lst_tags = QListWidget()

field_tag = QLineEdit()
btn_tags_add = QPushButton("Додатиa Тег")
btn_tgs_del = QPushButton("Видалити Тег")
btn_tags_search = QPushButton("Шукати Тег")
row1 = QHBoxLayout()
row1.addWidget(btn_note_create)
row1.addWidget(btn_note_del)
layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col2.addWidget(lst_notes)
layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)

col1.addWidget(field_text)
col2.addLayout(row1)

col2.addWidget(btn_note_save)
def show_notes():
    key = lst_notes.selectedItems()[0].text()
    field_text.setText(notes[key]['текст'])
lst_notes.itemClicked.connect(show_notes)
with open("notes.json", "r", encoding="utf8") as file:
    notes = json.load(file)
lst_notes.addItems(notes)






window.setLayout(layout_notes)
window.show()
app.exec_()