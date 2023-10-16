# print("\033[31mTexto Vermelho\033[0m")
# print("\033[32mTexto Verde\033[0m")
# print("\033[33mTexto Amarelo\033[0m")
# print("\033[34mTexto Azul\033[0m")
# print("\033[35mTexto Roxo\033[0m")
import random, os

class Minesweeper:
    def __init__(self, width, lenght, mines):
        self.width = width
        self.lenght = lenght
        self.boardGame = []
        self.boardGameNexus = []
        self.totalMines = 0
        self.gameIsRunning = False
        self.__letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'

        counter = 0
        for x in range(lenght):
            self.boardGame.append([])
            self.boardGameNexus.append([])
            for y in range(width):
                self.boardGame[x].append(False)
                random_number = random.randint(0,1)
                if(random_number == 0 and counter < mines):
                    counter += 1
                    self.totalMines += 1
                    self.boardGameNexus[x].append(self.totalMines)
                else:
                    self.boardGameNexus[x].append(None)
        self.totalMines -= 1

        self.startGame()
        
    def printGame(self):
        #os.system('cls')
        for c in range(self.lenght + 1):
            print(f'\033[33m{c: ^5}\033[0m', end='')
            
            for c1 in range(self.width):
                if(not c):
                    print(f'\033[33m{self.__letters[c1]: >4}\033[0m', end='')
                else:
                    if(not self.boardGame[c - 1][c1]):
                        print(f'{"=": >4}', end='')
                    else:
                        #print(f'{self.boardGame[c - 1][c1]: >4}', end='')
                        print(f'{"V": >4}', end='')
            print(f'\033[33m{c: >5}\033[0m', end='')
            print()
        
    def startGame(self):
        self.gameIsRunning = True

        while(self.gameIsRunning):
            pos1 = input('Type the position: ')
            self.attempt(pos1)

            self.printGame()


    def clearCmd():
        os.system('cls')

    def lossGame(self):
        print("'You've loss the game")
        self.gameIsRunning = False
    
    def attempt(self, pos1):
        position1 = self.findPositionByLetter(pos1[0])
        position2 = self.findPositionByNumber(int(pos1[1:3]))

        self.setBoardGame(position1, position2)

    def findPositionByLetter(self, letter):
        for i, l in enumerate(str(self.__letters).lower()):
            if(l == str(letter).lower()):
                return i
    def findPositionByNumber(self, number):
        return number - 1
    
    def setBoardGame(self, pos1, pos2):
        self.boardGame[pos2][pos1] = True
        if(self.boardGameNexus[pos2][pos1]):
            self.lossGame()

    def lookArround(self, pos1, pos2):
        for x in range(8):
            if(self.boardGameNexus[pos2][pos1]):
                pass
            
    

test = Minesweeper(10,10,5)

#os.system('cls')



