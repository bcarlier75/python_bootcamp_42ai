from sys import argv

if len(argv) == 2:
    print(argv[1][::-1])
elif len(argv) > 2:
    for i in range(1, len(argv)):
        argv[i] = argv[i].swapcase()
        argv[i] = argv[i][::-1]
    for i in range(1, len(argv) - 1):
        print(argv[len(argv) - i], end=' ')
    print(argv[1])
