import numpy as np
import matplotlib.pyplot as plt
import os


class ImageProcessor:
    def load(self, path):
        if os.path.exists(path) and os.path.isfile(path):
            img_array = plt.imread(path)
            print(f'Loading image of dimensions {img_array.shape[0]} x {img_array.shape[1]}')
            return img_array
        else:
            return None

    def display(self, array: np.array):
        if array is not None:
            plt.axis('off')
            plt.imshow(array)
            plt.show()


# imp = ImageProcessor()
# arr = imp.load("../resources/42AI.png")
# print(arr)
# print(arr.shape)
# imp.display(arr)
