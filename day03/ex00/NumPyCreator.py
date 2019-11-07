import numpy as np


class NumpyCreator:
    def from_list(self, lst: list, dtype=None) -> np.array:
        return np.asarray(lst, dtype=dtype)

    def from_tuple(self, tup: tuple, dtype=None) -> np.array:
        return np.asarray(tup, dtype=dtype)

    def from_iterable(self, itr, dtype=None) -> np.array:
        return np.asarray(itr, dtype=dtype)

    def from_shape(self, shp, dtype=None) -> np.array:
        return np.zeros(shp, dtype=dtype)

    def random(self, shp, dtype=None) -> np.array:
        return np.random.rand(shp[0], shp[1]).astype(dtype)

    def identity(self, n, dtype=None) -> np.array:
        return np.identity(n, dtype=dtype)


# npc = NumpyCreator()
# my_array = npc.from_list([[1, 2, 3], [6, 3, 4]])
# print(type(my_array))
# print(my_array)
#
# my_array = npc.from_tuple(("a", "b", "c"))
# print(type(my_array))
# print(my_array)
#
# my_array = npc.from_iterable(range(5))
# print(type(my_array))
# print(my_array)
#
# shape = (3, 5)
# my_array = npc.from_shape(shape, int)
# print(type(my_array))
# print(my_array)
#
# my_array = npc.random(shape)
# print(type(my_array))
# print(my_array)
#
# my_array = npc.identity(4)
# print(type(my_array))
# print(my_array)
