import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import cv2
import copy
from random import randint

class Filter:
    Mean_Filter_3_3 = [
        [1/9, 1/9, 1/9], 
        [1/9, 1/9, 1/9], 
        [1/9, 1/9, 1/9]
    ]
    Laplacian_Filter_3_3 = [
        [0, -1, 0], 
        [-1, 4, -1], 
        [0, -1, 0]]

    def __init__(self, fileName):
        self.Image = cv2.cvtColor(cv2.imread(fileName), cv2.COLOR_BGR2GRAY)
        self.Image_size = self.Image.shape





    def Convolution(self, filter, filterSize = 3):
        ResultImage = np.zeros((self.Image_size[0], self.Image_size[1]), dtype=np.uint8)
        col = int(filterSize / 2)
        row = int(filterSize / 2) + 1

        for h in range(1, self.Image_size[0] - col):
            for w in range(1, self.Image_size[1] - col):
                tmp = np.ravel(self.Image[h-col:h+row, w-col:w+row]) * np.ravel(filter)
                ResultImage[h][w] = np.sum(tmp)
        self.showImage(self.Image, ResultImage)





    def mean_filtering_3_3(self):
        ResultImage = np.zeros((self.Image_size[0], self.Image_size[1]), dtype=np.uint8)

        for h in range(1, self.Image_size[0] - 1):
            for w in range(1, self.Image_size[1] - 1):
                tmp = self.Image[h-1:h+2, w-1:w+2]
                ResultImage[h][w] = np.sum(tmp) / 9
        self.showImage(self.Image, ResultImage)

    def mean_filtering_5_5(self):
        ResultImage = np.zeros((self.Image_size[0], self.Image_size[1]), dtype=np.uint8)

        for h in range(2, self.Image_size[0] - 2):
            for w in range(2, self.Image_size[1] - 2):
                tmp = self.Image[h-2:h+3, w-2:w+3]
                ResultImage[h][w] = np.sum(tmp) / 25
        self.showImage(self.Image, ResultImage)


    def median_filtering_3_3(self, NoiseImage):
        ResultImage = np.zeros((self.Image_size[0], self.Image_size[1]), dtype=np.uint8)

        for h in range(1, self.Image_size[0] - 1):
            for w in range(1, self.Image_size[1] - 1):
                tmp = NoiseImage[h-1:h+2, w-1:w+2]
                tmp = np.sort(tmp.ravel())
                ResultImage[h][w] = tmp[4]
        self.showImage(NoiseImage, ResultImage)

    def median_filtering_5_5(self, NoiseImage):
        ResultImage = np.zeros((self.Image_size[0], self.Image_size[1]), dtype=np.uint8)

        for h in range(2, self.Image_size[0] - 2):
            for w in range(2, self.Image_size[1] - 2):
                tmp = NoiseImage[h-2:h+3, w-2:w+3]
                tmp = np.sort(tmp.ravel())
                ResultImage[h][w] = tmp[12]
        self.showImage(NoiseImage, ResultImage)
        

    def laplacian_filtering_3_3(self):
        ResultImage = np.zeros((self.Image_size[0], self.Image_size[1]), dtype=np.uint8)

        for h in range(1, self.Image_size[0] - 1):
            for w in range(1, self.Image_size[1] - 1):
                tmp = np.ravel(self.Image[h-1:h+2, w-1:w+2]) * np.ravel(self.Laplacian_Filter_3_3)
                ResultImage[h][w] = np.sum(tmp)
        self.showImage(self.Image, ResultImage)


    def SaltPepper(self):
        SaltPepperImage = np.zeros((self.Image_size[0], self.Image_size[1]), dtype=np.uint8)

        if self.Image.ndim > 2: height, width, _ = self.Image.shape
        else: height, width = self.Image.shape
        SaltPepperImage = copy.deepcopy(self.Image)
        number_of_pixels = randint(int(height * width / 100), int(height * width / 10))
    
        for i in range(number_of_pixels):
            y_coord = randint(0, height - 1)
            x_coord = randint(0, width - 1)
            if SaltPepperImage.ndim > 2:
                SaltPepperImage[y_coord][x_coord] = [randint(0, 255), randint(0, 255), randint(0, 255)]
            else:
                SaltPepperImage[y_coord][x_coord] = 255
        for i in range(number_of_pixels):
            y_coord = randint(0, height - 1)
            x_coord = randint(0, width - 1)
            if SaltPepperImage.ndim > 2:
                SaltPepperImage[y_coord][x_coord] = [randint(0, 255), randint(0, 255), randint(0, 255)]
            else:
                SaltPepperImage[y_coord][x_coord] = 0
        return SaltPepperImage

    def showImage(self, Originimage, ResultImage):
        cv2.resize(Originimage, (0, 0), None, .5, .5)
        sumImage = np.hstack((Originimage, ResultImage))
        cv2.imshow("Filtered Image", sumImage)
        cv2.waitKey(0)

filter = Filter("Cat_640p.jpg")
filter.Convolution(filter.Mean_Filter_3_3, 5)

