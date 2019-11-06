from time import sleep


def ft_progress(my_list):
    a = 1


def main():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)

if __name__ == '__main__':
    main()
