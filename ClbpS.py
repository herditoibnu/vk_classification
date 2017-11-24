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

    def getValue(self,img_read,x,y):
        try:
            return img_read[x,y]
        except IndexError:
            return 0

    def run(self):
        histogramCLBPS = [0]*256
        for x in range(self.img_read.shape[0]):
            for y in range(self.img_read.shape[1]):
                center_right = self.getValue(self.img_read, x, y + 1)
                down_right = self.getValue(self.img_read, x+1, y + 1)
                down_center = self.getValue(self.img_read, x, y + 1)
                down_left = self.getValue(self.img_read, x-1, y + 1)
                center_left = self.getValue(self.img_read, x, y - 1)
                top_left = self.getValue(self.img_read, x-1, y - 1)
                top_center = self.getValue(self.img_read, x, y - 1)
                top_right = self.getValue(self.img_read, x+1, y - 1)
                neighbours = [center_right, down_right,down_center,down_left,center_left,top_left,top_center,top_right]
                center = self.threshold(self.img_read[x,y],neighbours)

                histogramCLBPS[center]+=1

        return histogramCLBPS

