from sys import argv
import string

if len(argv) != 3:
    print(f'ERROR')
else:
    argv[2] = int(argv[2])
    if not (isinstance(argv[1], str) and isinstance(argv[2], int)):
        print('ERROR')
    if str.isdigit(argv[1]):
        print('ERROR')
    else:
        w_list = argv[1].split()
        w_list = [words.translate(str.maketrans('', '', string.punctuation))
                  for words in w_list if (len(words) > argv[2])]
        print(w_list)
