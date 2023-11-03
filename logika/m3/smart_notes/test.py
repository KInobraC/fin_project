# Import required libraries
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel,
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout,
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

# Create the PyQt5 application
app = QApplication([])
layout_notes = QHBoxLayout()
# Create the main window
window = QWidget()
window.setStyleSheet("background-color: #DBD582;")  # Set a slightly darker yellow background color

# Rest of your code...

# Display the window
window.setLayout(layout_notes)
window.show()
app.exec_()
