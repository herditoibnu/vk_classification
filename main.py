import cv2
import Image
import ClbpS
import ClbpM
import ClbpC
import numpy as np


if __name__ == '__main__':
    # dir_name = "DatasetWajah/"
    # inp = "F2.1.jpg"
    # img = Image.Image(dir_name + inp)


    img = Image.Image("coba2.png")
    img_read = img.run()
    cv2.imshow("a", img_read)
    cv2.waitKey()

    ClbpS_classifier = ClbpS.ClbpS(img_read)
    ClbpS_result = ClbpS_classifier.run()

    ClbpM_classifier = ClbpM.ClbpM(img_read)
    ClbpM_result = ClbpM_classifier.run()

    ClbpC_classifier = ClbpC.ClbpC(img_read)
    ClbpC_result = ClbpC_classifier.run()

    print ClbpS_result
    print ClbpM_result
    print ClbpC_result



    file = open("tes.txt","w")
    list = np.concatenate((ClbpS_result, ClbpM_result, ClbpC_result), axis=0)
    for item in list:
        file.write( "%s\n" % item )
    file.write("\n")
    file.close()