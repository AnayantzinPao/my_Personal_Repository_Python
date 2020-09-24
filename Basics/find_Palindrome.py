def palindrome(word):
    """[Find a palindrome with the insert and join function]

    Args:
        word ([string]): [String get by the user by the function input ]
        """

    reverse_letters = []

    for letter in word:
        reverse_letters.insert(0, letter)#Insert letter in the position [0]
                                        #Shifting the other letter to the right
    reversed_word = ''.join(reverse_letters)

    if reversed_word == word:
        return True
    return False

def palindrome2(word):
    """[Find a palindrome through slicing]

    Args:
        word ([string]): [String get by the user by the function input]
    """
    reversed_word = word[::-1] #Reverse the word by the jump in slicing
                            #word[Starts:ends:jump from the end to the begining]

    if reversed_word == word:
        return True
    return False

if __name__ == '__main__':
    word = str(input('Write a word: '))

    result = palindrome2(word)

    if result is True:
        print('{} is a palindrome'.format(word))
    else:
        print('{} is NOT a palindrome'.format(word))