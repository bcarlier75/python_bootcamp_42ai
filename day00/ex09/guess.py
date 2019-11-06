from random import randint


def congrats(nb: int):
    if nb == 1:
        print(f"Congratulations! You got it on your first try!")
    elif nb == 2:
        print(f"Congratulations! You got it on your second try!")
    elif nb == 3:
        print(f"Congratulations! You got it on your third try!")
    else:
        print(f"Congratulations, you've got it! You won in {nb} attempts!")


print(f"This is an interactive guessing game!\n"
      f"You have to enter a number between 1 and 99 to find out the secret number.\n"
      f"Type 'exit' to end the game.\n"
      f"Good luck!\n")


def main():
    answer = randint(1, 99)
    i = 0
    while True:
        i += 1
        my_input = input(f"What's your guess between 1 and 99?\n")
        if my_input == 'exit':
            exit()
        try:
            if isinstance(int(my_input), int):
                if int(my_input) > answer:
                    print(f'Too high!')
                elif int(my_input) < answer:
                    print(f'Too low!')
                elif int(my_input) == answer:
                    if answer == 42:
                        print(f'The answer to the ultimate question of life, the universe and everything is 42.')
                    congrats(i)
                    exit()
        except ValueError:
            print("That's not a number.")

if __name__ == '__main__':
    main()