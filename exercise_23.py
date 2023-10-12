"""
Exercise: Palindrome Checker

Create a Python program that checks if a word is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that remains the same when read backward. For example, "radar" and "A man, a plan, a canal, Panama" are palindromes, while "python" and "hello" are not.

Hint: You can ignore spaces and consider uppercase and lowercase characters as equal. That is, "A man, a plan, a canal, Panama" should be considered a palindrome.
"""

wordOrPhrase = input('Type a word or a phrase to see if it is a palindrome: ')

def stringCleaner(wordOrPhrase, arrayOfLetters):
    for x in wordOrPhrase:
        if (x != ' ' and x != ',' and x != '.' and x != '!'):
            arrayOfLetters.append(str(x).lower())
    

def arrayInverter(array, arrayInverted):
    y = 0
    for x in array:
        y += 1
        arrayInverted.append(array[len(array) - y])
    
def palindromechecker(wordOrPhrase):
    arrayOfLetters = []
    arrayInverted = []

    stringCleaner(wordOrPhrase, arrayOfLetters)
    arrayInverter(arrayOfLetters, arrayInverted)

    if (arrayOfLetters == arrayInverted):
        print('The word or phrase "{}" is a palindrome!!!'.format(wordOrPhrase))
    else:
        print('The word or phrase "{}" is not a palindrome T-T'.format(wordOrPhrase))


palindromechecker(wordOrPhrase)

# word = 'Andrew'
# y = 0
# for x in word:
#     y += 1
#     print(word[len(word)- y])
