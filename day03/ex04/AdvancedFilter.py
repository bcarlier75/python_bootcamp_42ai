import numpy as np
import os
import matplotlib.pyplot as plt


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


class AdvancedFilter:

    def get_corner(self, array, row, col, width, height, n):
        topleft = 0.0
        topright = 0.0
        bottomleft = 0.0
        bottomright = 0.0
        incr = 0
        if not row - 1 < 0 and not col - 1 < 0:
            topleft = array[row - 1][col - 1] * n
            incr += n
        if not row - 1 < 0 and not col + 1 > width - 1:
            topright = array[row - 1][col + 1] * n
            incr += n
        if not row + 1 > height - 1 and not col - 1 < 0:
            bottomleft = array[row + 1][col - 1] * n
            incr += n
        if not row + 1 > height - 1 and not col + 1 > width - 1:
            bottomright = array[row + 1][col + 1] * n
            incr += n
        return topleft, topright, bottomleft, bottomright, incr

    def get_cross(self, array, row, col, width, height, n):
        left = 0.0
        right = 0.0
        top = 0.0
        bottom = 0.0
        incr = 0
        if not col - 1 < 0:
            left = array[row][col - 1] * n
            incr += n
        if not col + 1 > width - 1:
            right = array[row][col + 1] * n
            incr += n
        if not row - 1 < 0:
            top = array[row - 1][col] * n
            incr += n
        if not row + 1 > height - 1:
            bottom = array[row + 1][col] * n
            incr += n
        return left, right, top, bottom, incr

    def mean_blur(self, array: np.array) -> np.array:
        # kernel size is 3
        width = array.shape[1]
        height = array.shape[0]
        result = np.zeros((height, width, 3), float)
        for row in range(height):
            for col in range(width):
                counter = 1
                current = array[row][col] * counter
                left, right, top, bottom, incr = self.get_cross(array, row, col, width, height, 1)
                counter += incr
                t_left, t_right, b_left, b_right, incr = self.get_corner(array, row, col, width, height, 1)
                counter += incr
                total = current + left + right + top + bottom + t_left + t_right + b_left + b_right
                avg = total / counter
                result[row][col] = avg[:3]
        return result

    def gaussian_blur(self, array: np.array) -> np.array:
        # kernel size is 3
        width = array.shape[1]
        height = array.shape[0]
        result = np.zeros((height, width, 3), float)
        for row in range(height):
            for col in range(width):
                counter = 41
                current = array[row][col] * counter
                left, right, top, bottom, incr = self.get_cross(array, row, col, width, height, 26)
                counter += incr
                t_left, t_right, b_left, b_right, incr = self.get_corner(array, row, col, width, height, 16)
                counter += incr
                total = current + left + right + top + bottom + t_left + t_right + b_left + b_right
                avg = total / counter
                result[row][col] = avg[:3]
        return result


# imp = ImageProcessor()
# arr = imp.load("../resources/42AI.png")
# adv = AdvancedFilter()
# imp.display(arr)

# ewarr = adv.mean_blur(arr)
# print(newarr)
# imp.display(newarr)

# newarr = adv.gaussian_blur(arr)
# print(newarr)
# imp.display(newarr)
