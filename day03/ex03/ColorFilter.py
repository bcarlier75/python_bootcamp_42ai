import numpy as np


class ColorFilter:
    def invert(self, array: np.array) -> np.array:
        return 1.0 - array

    def to_blue(self, array: np.array) -> np.array:
        for color_array in array:
            for rgb in color_array:
                rgb[0], rgb[1] = float(0), float(0)
        return array

    def to_green(self, array: np.array) -> np.array:
        for color_array in array:
            for rgb in color_array:
                rgb[0], rgb[2] = float(0), float(0)
        return array

    def to_red(self, array: np.array) -> np.array:
        for color_array in array:
            for rgb in color_array:
                rgb[1], rgb[2] = float(0), float(0)
        return array

    def upd(self, val: float) -> float:
        if val < 0.2:
            return 0.0
        elif 0.2 <= val < 0.4:
            return 0.2
        elif 0.4 <= val < 0.6:
            return 0.4
        elif 0.6 <= val < 0.8:
            return 0.6
        elif 0.8 <= val <= 1.0:
            return 0.8

    # not quite sure if it is working as intended
    def celluloid(self, array: np.array) -> np.array:
        for color_array in array:
            for rgb in color_array:
                # flooring not the luminance but the color themselves? not sure if it's cel shading
                # rgb[0], rgb[1], rgb[2] = self.upd(rgb[0]), self.upd(rgb[1]), self.upd(rgb[2])

                # alternative calculus for luminance, more computational and less easier to reinject in color
                # luminance = sqrt((0.299 * rgb[0]**2) + (0.587 * rgb[1]**2) + (0.113 * rgb[2]**2))

                luminance = (0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2])
                luminance = self.upd(luminance)
                # reinjecting the color with new luminance
                rgb[0] = (luminance - 0.7152 * rgb[1] - 0.0722 * rgb[2]) / 0.2126
                rgb[1] = (luminance - 0.2126 * rgb[0] - 0.0722 * rgb[2]) / 0.7152
                rgb[2] = (luminance - 0.2126 * rgb[0] - 0.7152 * rgb[1]) / 0.0722
        return array

    def to_grayscale(self, array: np.array, filt='mean') -> np.array:
        if filt == 'mean' or filt == 'm':
            for color_array in array:
                for rgb in color_array:
                    rgb[..., :3] = np.mean(rgb[..., :3])
            return array
        elif filt == 'weighted' or filt == 'w':
            for color_array in array:
                for rgb in color_array:
                    rgb[..., :3] = np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
            return array


# imp = ImageProcessor()
# arr = imp.load("../resources/42AI.png")
# cf = ColorFilter()
# imp.display(arr)

# ewarr = cf.invert(arr)
# print(newarr)
# imp.display(newarr)

# newarr = cf.to_blue(arr)
# print(newarr)
# imp.display(newarr)

# newarr = cf.to_green(arr)
# print(newarr)
# imp.display(newarr)

# newarr = cf.to_red(arr)
# print(newarr)
# imp.display(newarr)

# newarr = cf.celluloid(arr)
# print(newarr)
# imp.display(newarr)

# newarr = cf.to_grayscale(arr, 'm')
# print(newarr)
# imp.display(newarr)
