import random


def guessing_game(low=1, high=10):

    def game(low, high):
        number = random.randint(low, high)
        while True:
            while True:
                try:
                    guess = int(input('Guess a number between {}-{} '.format(low, high)))
                    if low-1 < guess < high+1:
                        break
                except ValueError:
                    pass

            if guess == number:
                print('Correct!')
                break

            if guess < number:
                print('Too low!')
            else:
                print('Too high!')

    play_again = True
    while play_again is True:
        game(low, high)
        while True:
            choice = input('Would you like to play again? Y/N ')
            if choice.lower() == 'n':
                play_again = False
                break
            elif choice.lower() == 'y':
                break


if __name__ == "__main__":

    guessing_game()
