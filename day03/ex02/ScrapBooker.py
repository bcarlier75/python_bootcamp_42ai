import numpy as np


class ScrapBooker:
    def crop(self, array: np.array, dimensions: tuple, position=(0, 0)) -> np.array:
        pass
        if dimensions[0] > array.shape[0] \
                or dimensions[1] > array.shape[1] \
                or (dimensions[0] + position[0] > array.shape[0]) \
                or (dimensions[1] + position[1] > array.shape[1]):
            return 'Error: new array would be outside of current array'
        return array[position[0]:position[0] + dimensions[0], position[1]:position[1] + dimensions[1]]

    def thin(self, array: np.array, n: int, axis=0) -> np.array:
        if axis == 0:
            return array[:, :n]
        elif axis == 1:
            return array[:n, :]

    def juxtapose(self, array: np.array, n: int, axis=0) -> np.array:
        if axis == 0:
            return np.tile(array, (n, 1))
        elif axis == 1:
            return np.tile(array, (1, n))

    def mosaic(self, array: np.array, dimensions: tuple) -> np.array:
        return np.tile(array, dimensions)


# myarr = np.asarray([[1, 2, 3, 4, 5, 6],
#                     [7, 8, 9, 10, 11, 12],
#                     [13, 14, 15, 16, 17, 18],
#                     [19, 20, 21, 22, 23, 24],
#                     [25, 26, 27, 28, 29, 30],
#                     [31, 32, 33, 34, 35, 36]])
# print('--- Original array ---')
# print(myarr)
# print(type(myarr))
# scp = ScrapBooker()
#
# newarr = scp.crop(myarr, (4, 3), (1, 2))
# print('\n--- Perform crop ---')
# print(newarr)
# print(f'Type of this array: {type(newarr)}')
# print(f'Shape of this array: {newarr.shape}')
#
# newarr = scp.thin(myarr, 4, 1)
# print('\n--- Perform thin horizontal ---')
# print(newarr)
# print(f'Type of this array: {type(newarr)}')
# print(f'Shape of this array: {newarr.shape}')
#
# newarr = scp.thin(myarr, 4, 0)
# print('\n--- Perform thin vertical ---')
# print(newarr)
# print(f'Type of this array: {type(newarr)}')
# print(f'Shape of this array: {newarr.shape}')
#
# newarr = scp.juxtapose(myarr, 3, 1)
# print('\n--- Perform juxtapose vertical ---')
# print(newarr)
# print(f'Type of this array: {type(newarr)}')
# print(f'Shape of this array: {newarr.shape}')
#
# newarr = scp.juxtapose(myarr, 2, 0)
# print('\n--- Perform juxtapose horizontal ---')
# print(newarr)
# print(f'Type of this array: {type(newarr)}')
# print(f'Shape of this array: {newarr.shape}')
#
# newarr = scp.mosaic(myarr, (2, 3))
# print('\n--- Perform mosaic ---')
# print(newarr)
# print(f'Type of this array: {type(newarr)}')
# print(f'Shape of this array: {newarr.shape}')
