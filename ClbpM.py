import numpy as np
from Extraction import Extraction


class ClbpM(Extraction):
    def threshold(self, magnitude):
        thresholded = []
        avg_magnitude = np.mean(magnitude)
        for m in magnitude:
            if m >= avg_magnitude:
                thresholded.append(1)
            else:
                thresholded.append(0)

        return self.weighting(thresholded)

    def getValue(self,img_read,x,y):
        try:
            return img_read[x,y]
        except IndexError:
            return 0

    def getmagnitude(self, center, neighbours):
        magnitude = []
        for n in neighbours:
            magnitude.append(abs(n - center))
        return magnitude

    def run(self):
        histogramCLBPM = [0] * 256
        for x in range(self.img_read.shape[0]):
            for y in range(self.img_read.shape[1]):
                center_right = self.getValue(self.img_read, x, y + 1)
                down_right = self.getValue(self.img_read, x + 1, y + 1)
                down_center = self.getValue(self.img_read, x, y + 1)
                down_left = self.getValue(self.img_read, x - 1, y + 1)
                center_left = self.getValue(self.img_read, x, y - 1)
                top_left = self.getValue(self.img_read, x - 1, y - 1)
                top_center = self.getValue(self.img_read, x, y - 1)
                top_right = self.getValue(self.img_read, x + 1, y - 1)
                neighbours = [center_right, down_right, down_center, down_left, center_left, top_left, top_center,
                              top_right]
                center = self.img_read[x,y]
                magnitude = self.getmagnitude(center, neighbours)

                histogramCLBPM[self.threshold(magnitude)]+=1

        return histogramCLBPM


