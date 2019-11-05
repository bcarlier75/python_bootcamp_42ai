class Vector:
    def __init__(self, values, size, my_range):
        flag = 0
        if values:
            if isinstance(values, list):
                for elem in values:
                    if not isinstance(elem, float):
                        flag = 1
                if flag == 0:
                    self.values = values
                    self.length = int(len(self.values))
                else:
                    print('The list should only contain float values.')
            else:
                print('Init error: expect a list of float for parameter values')
        elif size:
            if isinstance(size, int):
                self.values = [float(i) for i in range(0, size)]
                self.length = len(self.values)
            else:
                print('Init error: expect an integer for parameter size.')
        elif my_range:
            if isinstance(my_range, tuple) and len(my_range) == 2:
                for elem in my_range:
                    if not isinstance(elem, int):
                        flag = 1
                    if flag == 0:
                        self.values = [float(i) for i in range(my_range[0], my_range[1])]
                        self.length = len(self.values)
                    else:
                        print('The tuple should only contain int values.')
            else:
                print('Init error: expect a tuple with 2 integer for parameter my_range.')
        else:
            print('Init error: expect either a list of float, an integer or  tuple with 2 integer.')

    def __add__(self, vec_or_scalar):
        if isinstance(vec_or_scalar, Vector) and self.length == vec_or_scalar.length:
            for i in range(0, self.length):
                self.values[i] = self.values[i] + vec_or_scalar.values[i]
        elif isinstance(vec_or_scalar, float):
            for i in range(0, self.length):
                self.values[i] = self.values[i] + vec_or_scalar
        else:
            print(f'Value error: {vec_or_scalar} is not an instance of class Vector or a float'
                  'or vectors have different length.')

    def __radd__(self, vec_or_scalar):
        pass

    def __sub__(self, vec_or_scalar):
        if isinstance(vec_or_scalar, Vector) and self.length == vec_or_scalar.length:
            for i in range(0, self.length):
                self.values[i] = self.values[i] - vec_or_scalar.values[i]
        elif isinstance(vec_or_scalar, float):
            for i in range(0, self.length):
                self.values[i] = self.values[i] - vec_or_scalar
        else:
            print(f'Value error: {vec_or_scalar} is not an instance of class Vector or a float '
                  'or vectors have different length.')

    def __rsub__(self, vec_or_scalar):
        pass

    def __truediv__(self, scalar):
        if isinstance(scalar, float):
            for i in range(0, self.length):
                self.values[i] = self.values[i] / scalar
        else:
            print('Value error: scalar should be a float')

    def __rtruediv__(self, vec_or_scalar):
        pass

    def __mul__(self, vec_or_scalar):
        if isinstance(vec_or_scalar, Vector) and self.length == vec_or_scalar.length:
            for i in range(0, self.length):
                self.values[i] = self.values[i] * vec_or_scalar.values[i]
        elif isinstance(vec_or_scalar, float):
            for i in range(0, self.length):
                self.values[i] = self.values[i] * vec_or_scalar
        else:
            print(f'Value error: {vec_or_scalar} is not an instance of class Vector or a float '
                  'or vectors have different length.')

    def __rmul__(self, vec_or_scalar):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
