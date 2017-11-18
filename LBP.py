class LBP:
    def __init__(self, img_read):
        self.img_read = img_read

    def weighting(self, thresholded):
        weighted = []
        i = 0
        for t in thresholded:
            weighted.append(t * 2**i)
            i += 1

        return sum(weighted)

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

        # for i in range(self.img_read.shape[0]):  # traverses through height of the image
        #     for j in range(self.img_read.shape[1]):  # traverses through width of the image
        #         print self.img_read[i][j]
