import random
import os
#Build a hangman game with ASCII art

#Write a constant in python with UPPER letters
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [ #Define the words for the game
    'cloud',
    'dream',
    'calculator',
    'goverment',
    'smartphone',
    'programmer',
    'book',
    'gentleman'
]

def random_word():
    #Choose a word in random way from the list of words
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def display_board(hidden_word, tries,letters_used):
    """[Draw the hangman figure with the list IMAGES]

    Args:
        hidden_word ([list]): [Hidden word previously defined]
        tries ([int]): [The number of mistakes the users have had]
    """
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print("Letters you have used: ",letters_used)
    print('*________________________*')


def run():
    word = random_word() #Choose a word
    hidden_word = ['-'] * len(word) #Build a "hidden word"
    tries = 0 #Use the first figure
    letters_used =[]

    while True:
        display_board(hidden_word, tries,letters_used)
        current_letter = str(input('Write a letter: '))#Ask for a letter
        letters_used.append(current_letter)

        letter_indexes = []
        for idx in range(len(word)):
            #Compare the current letter with all the letter in the word that is playing
            if word[idx] == current_letter:
                #If the comparison was right then save the index in a new list
                letter_indexes.append(idx)
        os.system('cls') #windows #Clean the screen
        #os.system('clear') #unix

        if len(letter_indexes) == 0:#If we cannot find any letter in our word then
            tries += 1 #Add one to the mistakes

            if tries == 7: #If the users have 7 mistakes then he lose
                display_board(hidden_word, tries,letters_used)
                print('')
                print('You lose. Correct word: {}'.format(word))
                break
        else: #If we find a letter that match then replace the hidden word
            #in the correct index with the letter
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = [] #Clean the letter index to compare in the next iteration

        try:
            #When python does not find an index for ['-'] 
            # it returns an error and it means the users has won
            hidden_word.index('-')
        except ValueError: #We catch that error and break while loop
            print('')
            print('Yoy win!. Correct word: {}'.format(word))
            break

if __name__ == '__main__':
    #Start
    print('WELCOME,DEAR <3!')
    run() #Execute run method
