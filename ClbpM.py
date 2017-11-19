from Extraction import Extraction


class ClbpM(Extraction):
    def threshold(self, c, neighbours):
        thresholded = []
        for n in neighbours:
            if n >= c:
                thresholded.append(1)
            else:
                thresholded.append(0)

        return self.weighting(thresholded)

    def run(self):
        neighbours = [25, 10, 15, 1, 8, 5, 3, 36]
        center = 12
        print self.threshold(center, neighbours)
