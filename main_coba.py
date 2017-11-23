import collections as cl
import Image
import ClbpS
import ClbpM
import ClbpC
import numpy as np
import os.path



def canberra_distance(testing, training): #menghitung jarak menggunakan Canberra Distance
    kelas = training[514]
    jarak = 0
    i=0
    for val in testing:
        if val == 0 and training[i] == 0:
            continue
        else:
            jarak += (abs(float(val - training[i])) / (abs(float(val)) + abs(float(training[i]))))
        i += 1
    jarak_dan_kelas = [jarak, kelas]
    return jarak_dan_kelas

def akurasi(kelas_training, hasil): #menghitung akurasi hasil knn
    total_benar = 0
    count = 0
    for val in kelas_training:
        if val == hasil[count]:
            total_benar+=1
        count+=1
    return (float(total_benar)/float(count))*100


if __name__ == '__main__':

    dir_name = "d1dikit/"
    nilai_k = raw_input("Masukkan nilai k:")
    nilai_k  = int(nilai_k)
    file = open("d1dikit.txt","r")
    kelas = 1
    flag = 0
    hasil = []
    kelas_testing = []
    # mengubah gambar training menjadi histogram CLBP dan ditulis ke dalam file
    if not os.path.isfile("pixeldikit_train.csv"):
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

            data = open("pixeldikit_train.csv","a")
            for item in list:
                data.write( "%s," % item )
            data.write("%s" %kelas)
            data.write("\n")
            data.close()
            if flag == 16:
                flag = 0
                kelas +=1

    dir_name = "d2dikit/"
    file = open("d2dikit.txt", "r")
    line_count = 0
    flag = 0
    kelas = 1
    conter = 0
    #iterasi file testing
    if not os.path.isfile("pixeldikit_test.csv"):
        for item in file:
            flag+=1
            conter+=1
            print "Gambar ke: " + str(conter)
    #        print item.strip()
            img = Image.Image(dir_name + item.strip())
            img_read = img.run()
            # mencari histogram CLBP dari gambar input
            ClbpS_classifier = ClbpS.ClbpS(img_read)
            ClbpS_result = ClbpS_classifier.run()

            ClbpM_classifier = ClbpM.ClbpM(img_read)
            ClbpM_result = ClbpM_classifier.run()

            ClbpC_classifier = ClbpC.ClbpC(img_read)
            ClbpC_result = ClbpC_classifier.run()

            list = np.concatenate((ClbpS_result, ClbpM_result, ClbpC_result), axis=0)
            kelas_testing.append(kelas)
            print kelas

            data = open("pixeldikit_test.csv", "a")
            for item in list:
                data.write("%s," % item)
            data.write("%s" % kelas)
            data.write("\n")
            data.close()

            if flag == 4:
                flag = 0
                kelas += 1

        #     file_training = open("pixeldikit_train.csv","r")
        #     line_count = 0
        #     training_array = [] #array untuk menyimpan histogram CLBP dari file training, per image array direset
        #     array_jarak = []
        #
        #     #menghitung jarak dari data testing ke setiap data training
        #     for line in file_training:
        #         line_count+=1
        #         if line_count<=515:
        #             training_array.append(int(line))
        #         elif line_count == 516:
        #             jarak = canberra_distance(list, training_array)
        #            # print jarak
        #             array_jarak.append(jarak)
        #             line_count = 0
        #             training_array = []
        #     #mencari data jarak terkecil sebanyak k, mencari kelas yang paling banyak terjadi, dan ditaruh ke dalam array hasil
        #     array_jarak.sort(key = lambda jarak: jarak[0])
        #     #print array_jarak
        #     i = 0
        #     kelas_vote=[]
        #     cnt = cl.Counter()
        #
        #     for jarak in array_jarak:
        #         i+=1
        #         cnt[jarak[1]]+=1
        #         if(i==nilai_k):
        #             break
        #     hasil.append(max(cnt, key=cnt.get))
        #
        #
        # print kelas_testing
        # print hasil
        # print akurasi(kelas_testing,hasil)
