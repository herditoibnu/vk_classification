import cv2
import Image
import ClbpS
import ClbpM

if __name__ == '__main__':
    dir_name = "DatasetWajah/"
    inp = "F2.1.jpg"
    img = Image.Image(dir_name + inp)
    img_read = img.run()

    cv2.imshow("a", img_read)
    cv2.waitKey()

    ClbpS_classifier = ClbpS.ClbpS(img_read)
    ClbpS_result = ClbpS_classifier.run()

    ClbpM_classifier = ClbpM.ClbpM(img_read)
    ClbpM_result = ClbpM_classifier.run()