from sys import argv


if len(argv) == 1:
    print(f'Usage: python operations.py\n'
          f'Example:\n'
          f'\tpython operations.py 10 3')
elif len(argv) == 3:
    try:
        my_sum = int(argv[1]) + int(argv[2])
        my_diff = int(argv[1]) - int(argv[2])
        my_mul = int(argv[1]) * int(argv[2])
        if int(argv[2]) != 0:
            my_div = int(argv[1]) / int(argv[2])
            my_mod = int(argv[1]) % int(argv[2])
        else:
            my_div = 'ERROR (div by zero)'
            my_mod = 'ERROR (modulo by zero)'
        print(f'Sum:\t\t {my_sum}\n'
              f'Difference:\t {my_diff}\n'
              f'Product:\t {my_mul}\n'
              f'Quotient:\t {my_div}\n'
              f'Remainder:\t {my_mod}')
    except ValueError as e:
        print(f'InputError: only numbers\n'
              f'Usage: python operations.py\n'
              f'Example:\n'
              f'\tpython operations.py 10 3')

elif len(argv) > 3:
    print(f'InputError: too many arguments\n'
          f'Usage: python operations.py\n'
          f'Example:\n'
          f'\tpython operations.py 10 3')
elif len(argv) == 2:
    print(f'InputError: too few arguments\n'
          f'Usage: python operations.py\n'
          f'Example:\n'
          f'\tpython operations.py 10 3')