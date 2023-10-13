import random

with open('exercise_26.txt', 'r') as arquivo:
    palavras = arquivo.read().split()

randomWord = palavras[random.randint(0,len(palavras)-1)]

class Hangman:
    def __init__(self, word):
        self.word = word
        self.letters = str(list(word)).lower()
        self.hits = []
        self.gameIsRunning = False
        self.errors = []

        self.start()


    def start(self):
        for letter in self.word:
            self.hits.append(False)

        self.gameIsRunning = True

        self.printGame()
    
        while(self.gameIsRunning):
            self.attempt(str(input('Type a word: ')).lower())
            if(self.gameIsRunning):
                self.printGame()
                self.gameIsWon()    
    
    def gameIsWon(self):
        gameIsWon = True
        
        for x in self.hits:
            if(not x):
                gameIsWon = False

        if (gameIsWon):
            self.winGame()

    def lossGame(self):
        self.gameIsRunning = False

    def winGame(self):
        print('You won this game. The word was: ', self.word)
        print()
        self.gameIsRunning = False
    
    def addError(self, letter):
        if(len(self.errors) < 6):
            self.errors.append(letter)
        else:
            self.lossGame()
         
    def printGame(self):
        print()
        self.printErrors()
        if(self.gameIsRunning):
            
            for i, w in enumerate(self.hits):
                if(w):
                    print(self.word[i], end=' ')
                else:
                    print('_', end=' ')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
    
    def attempt(self, letter):
        error = True
        if(letter == self.word):
            self.winGame()
            return

        for i, w in enumerate(self.word):
            if(w == letter):
                self.hits[i] = True
                error = False
        if(error):
            self.addError(letter)
    
    def printErrors(self):
        print(f'Number of errors: {len(self.errors)}, you have more {7 - len(self.errors)} attempts')
        print('Errors: ', self.errors)

# print(randomWord)
test = Hangman(randomWord)

    