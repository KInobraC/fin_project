import os

# потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog, QLabel,
    QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
)

from PIL import Image, ImageFilter
# from PIL.ImageQt import ImageQt
from PIL.ImageFilter import SHARPEN

app = QApplication([])
main_window = QWidget()

button_folder = QPushButton("Папка")
button_left = QPushButton("Вліво")
button_right = QPushButton("Вправо")
button_flip = QPushButton("Джеркалоо")
button_sharp = QPushButton("Різкість")
button_bw = QPushButton("Ч.Б")

lst_files = QListWidget()

# image = "2824384.jpg"
# kat = QPixmap(image)

Photo = QLabel(main_window)
# Photo.setPixmap(kat)

layouth1 = QHBoxLayout()
layoutv1 = QVBoxLayout()
layouth2 = QHBoxLayout()
layoutv2 = QVBoxLayout()

layoutv1.addWidget(button_folder)
layoutv1.addWidget(lst_files)
layouth1.addWidget(button_left)
layouth1.addWidget(button_right)
layouth1.addWidget(button_flip)
layouth1.addWidget(button_sharp)
layouth1.addWidget(button_bw)

layoutv2.addWidget(Photo)
layoutv2.addLayout(layouth1)

layouth2.addLayout(layoutv1, 1)
layouth2.addLayout(layoutv2, 4)


def filter(files):
    result = []
    ext = ['jpg', 'jpeg', 'bmp', 'gif', 'jfif', 'svg', 'png']

    for file in files:

        if file.split('.')[-1] in ext:
            result.append(file)
    return result


def showFiles():
    global workdir

    workdir = QFileDialog.getExistingDirectory()

    files_and_folders = os.listdir(workdir)
    filtered_img = filter(files_and_folders)

    lst_files.clear()
    lst_files.addItems(filtered_img)


class ImageProcescor():
    def __init__(self):
        self.filename = None
        self.original = None
        self.save_dir = "Modified/"

    def loadImage(self, filename):
        self.filename = filename

        file_path = os.path.join(workdir, filename)

        self.original = Image.open(file_path)

    def show_image(self, path):
        Photo.hide()

        pixmapimage = QPixmap(path)
        w, h = Photo.width(), Photo.height()

        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)

        Photo.setPixmap(pixmapimage)

        Photo.show()



workimage = ImageProcescor()



main_window.setLayout(layouth2)

main_window.show()
app.exec_()