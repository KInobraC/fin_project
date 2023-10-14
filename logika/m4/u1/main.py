def do_left(self):
    if self.original:
        left = self.original.transpose(Image.ROTATE_90)
        self.edited.append(left)
        left.show()
    else:
        print("Откройте изображение сначала")