from Extraction import Extraction
import numpy as np


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

    def getmagnitude(self, center, neighbours):
        magnitude = []
        for n in neighbours:
            magnitude.append(abs(n - center))
        return magnitude

    def run(self):
        neighbours = [28, 56, 64, 99, 10, 9, 12, 34]
        center = 25
        magnitude = self.getmagnitude(center, neighbours)
        print self.threshold(magnitude)
