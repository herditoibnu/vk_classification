from Extraction import Extraction


class ClbpC(Extraction):
    def threshold(self,center,img_mean):
        if center>=img_mean:
            return 1
        else:
            return 0

    def run(self):
        histogramCLBPC = [0] * 2
        rata2 = self.img_read.mean()
        for x in range(self.img_read.shape[0]):
            for y in range(self.img_read.shape[1]):
                histogramCLBPC[self.threshold(self.img_read[x,y],rata2)] += 1
        return histogramCLBPC
