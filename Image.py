import cv2


class Image:
    def __init__(self, img_file):
        self.img_file = img_file

    def read_img(self):
        return cv2.imread(self.img_file)

    def run(self):
        img_read = self.read_img()
        return img_read
