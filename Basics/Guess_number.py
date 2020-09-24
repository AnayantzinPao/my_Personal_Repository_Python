
import random

#Program will run until you guess the random number


def run():
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(input('Try a number：'))

        if number == random_number:
            print('Congrats!. That is the hidden number')
            number_found = True
        elif number > random_number:
            print('The hidden number is smaller')
        else:
            print('The hidden number is bigger')


if __name__ == '__main__':
    run()