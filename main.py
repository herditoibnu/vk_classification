import Image
import ClbpS

if __name__ == '__main__':
    img = Image.Image("coba.jpg")
    img_read = img.run()

    ClbpS_classifier = ClbpS.ClbpS(img_read)
    ClbpS_result = ClbpS_classifier.run()
