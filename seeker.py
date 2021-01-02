# OOP and OOAD Assessment
# Karina Sudnicina
# 17.12.2020
# Seeker class
class Seeker:

    def __init__(self, sc, r, c):
        self.seek_char = sc
        self.row = r
        self.column = c

    def setChar(self, newvalue):
        self.seek_char = newvalue
    def setRow(self, newvalue):
        self.row = newvalue
    def setCol(self, newvalue):
        self.column = newvalue

    def getChar(self):
        return self.seek_char
    def getRow(self):
        return self.row
    def getCol(self):
        return self.column


    def moveDown(self):
        return self.row + 1

    def moveUp(self):
        return self.row - 1

    def moveLeft(self):
        return self.column - 1

    def moveRight(self):
        return self.column + 1

    def toString(self):
        info = "Seeker " + self.seek_char + " at row " + str(self.row) + " and column " + str(self.column)
        return info