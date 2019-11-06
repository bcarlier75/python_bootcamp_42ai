from sys import argv


MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
                   '-': '-....-', '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ''
    for c in message:
        if c != ' ':
            cipher += MORSE_CODE_DICT[c] + ' '
        else:
            cipher += ' '
    return cipher

if __name__ == '__main__':
    if len(argv) >= 2:
        for i in range(1, len(argv)):
            argv[i] = argv[i].split()
            for elem in argv[i]:
                elem = elem.upper()
                for car in elem:
                    if car not in MORSE_CODE_DICT.keys():
                        print('ERROR')
                        exit()
        for i in range(1, len(argv) - 1):
            for elem in argv[i]:
                elem = elem.upper()
                message_encrypted = encrypt(elem)
                if message_encrypted == 'ERROR':
                    print('ERROR')
                    exit()
                else:
                    print(message_encrypted, end='/ ')
        for elem in argv[len(argv) - 1]:
            elem = elem.upper()
            message_encrypted = encrypt(elem)
            if message_encrypted == 'ERROR':
                print('ERROR')
                exit()
            else:
                print(message_encrypted)
