class Extraction(object):
    def __init__(self, img_read):
        self.img_read = img_read

    def weighting(self, thresholded):
        weighted = []
        i = 0
        for t in thresholded:
            weighted.append(t * 2 ** i)
            i += 1

        return sum(weighted)
