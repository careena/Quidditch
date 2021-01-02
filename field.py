# OOP and OOAD Assessment
# Karina Sudnicina
# 17.12.2020
# Field class
class Field:

    def __init__(self):
        self.field = [['#','#','#','#','#','#','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ','#','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#','#','#','#','#','#','#']]
        self.snitch = 1
        self.height = 7
        self.width = 7

    def toString(self):
        printme = ""
        for i in range (0, len(self.field)):
            for j in self.field[i]:
                printme = printme + j
            printme = printme + "\n"
        return printme

    def placeSeeker1 (self, seek_char, row, column):
        self.field[row][column] = seek_char

    def placeSeeker2 (self, seek_char, row, column):
        self.field[row][column] = seek_char

    def placeSnitch(self, snitch_char, row, column):
        self.field[row][column] = snitch_char

    def clearAtPos(self, row, col):
        self.field[row][col] = " "

    def getCharAtPos(self, row, col):
        return self.field[row][col]

    def canMove(self, row, col):
        return self.field[row][col] == ' ' or self.field[row][col] == '@'

    def catchSnitch(self):
        self.snitch -= 1


    def goToLevel2(self):
        self.field = [['#','#','#','#','#','#','#','#', '#', '#'],
               ['#',' ','#',' ',' ',' ','#',' ', '#', "#"],
               ['#',' ','#',' ',' ',' ',' ', ' ',' ','#'],
               ['#',' ',' ',' ',' ','#','#',' ', '#', '#'],
			   ['#',' ',' ',' ',' ','#',' ', ' ', '#', '#'],
               ['#',' ',' ',' ',' ','#',' ',' ', '#','#'],
               ['#',' ',' ',' ',' ','#',' ', '#', ' ', '#'],
               ['#',' ',' ',' ',' ',' ',' ', ' ',' ', '#'],
               ['#','#',' ','#',' ',' ','#', ' ', '#', '#'],
               ['#','#','#','#','#','#','#', '#', '#', '#']]
        self.snitch = 1
        self.width = 10
        self.height = 10

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getSnitch(self):
        return self.snitch