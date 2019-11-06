def what_are_the_vars(*args, **kwargs):
    my_obj = ObjectC()
    for i, value in enumerate(args):
        setattr(my_obj, 'var_' + str(i), value)
    for key, val in kwargs.items():
        if hasattr(my_obj, key):
            return None
        setattr(my_obj, key, val)
    return my_obj


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(my_obj):
    if my_obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(my_obj):
        if attr[0] != '_':
            value = getattr(my_obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
