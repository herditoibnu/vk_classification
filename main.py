import cv2
import Image
import ClbpS
import ClbpM
import ClbpC
import numpy as np
import os.path
from PIL import Image as PImage
from os import listdir

if __name__ == '__main__':
    dir_name = "kacamati/"
   # inp = "F2.1.jpg"


    # img = Image.Image("coba2.png")
    file = open("datasit.txt","r")
    kelas = 1
    flag = 0
    if not os.path.isfile("pixel.txt"):
        for item in file:
            flag+=1
    #        print item.strip()
            img = Image.Image(dir_name + item.strip())
            img_read = img.run()
            ClbpS_classifier = ClbpS.ClbpS(img_read)
            ClbpS_result = ClbpS_classifier.run()

            ClbpM_classifier = ClbpM.ClbpM(img_read)
            ClbpM_result = ClbpM_classifier.run()

            ClbpC_classifier = ClbpC.ClbpC(img_read)
            ClbpC_result = ClbpC_classifier.run()
            list = np.concatenate((ClbpS_result, ClbpM_result, ClbpC_result), axis=0)

            data = open("pixel.txt","a")
            for item in list:
                data.write( "%s\n" % item )
            data.write("%s\n" %kelas)
            data.write("\n")
            data.close()
            if flag == 16:
                flag = 0
                kelas +=1
    # def loadImages(path):
    #     # return array of images
    #
    #     imagesList = listdir(path)
    #     loadedImages = []
    #     for image in imagesList:
    #         img = PImage.open(path + image)
    #         loadedImages.append(img)
    #         print img.filename
    #     return loadedImages
    #
    #
    # path = "DatasetWajah/"
    #
    # # your images in an array
    # imgs = loadImages(path)

