import Image
import LBP

if __name__ == '__main__':
    img = Image.Image("coba.jpg")
    img_read = img.run()

    LBP_classifier = LBP.LBP(img_read)
    LBP_result = LBP_classifier.run()
