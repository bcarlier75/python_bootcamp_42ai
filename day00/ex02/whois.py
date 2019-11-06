from sys import argv

if len(argv) != 2:
    print('ERROR')
else:
    argv[1] = int(argv[1])
    if isinstance(argv[1], int):
        if argv[1] == 0:
            print("I'm Zero.")
        elif argv[1] % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print('ERROR')
