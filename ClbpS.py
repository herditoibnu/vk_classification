from Extraction import Extraction


class ClbpS(Extraction):
    def threshold(self, center, neighbours):
        thresholded = []
        for n in neighbours:
            if n >= center:
                thresholded.append(1)
            else:
                thresholded.append(0)

        return self.weighting(thresholded)

    def run(self):
        neighbours = [25, 100, 15, 1, 8, 5, 3, 36]
        center = 12
        print self.threshold(center, neighbours)

        # for i in range(self.img_read.shape[0]):  # traverses through height of the image
        #     for j in range(self.img_read.shape[1]):  # traverses through width of the image
        #         print self.img_read[i][j]
