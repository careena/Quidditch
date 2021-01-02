# OOP and OOAD Assessment
# Karina Sudnicina
# 17.12.2020
# Snitch class

# import random to make snitch move on level2
import random

class Snitch:
    def __init__(self, snc, r, c):
        self.snitch_char = snc
        self.row = r
        self.column = c

    def setChar(self, newvalue):
        self.sn_char = newvalue
    def setRow(self, newvalue):
        self.row = newvalue
    def setCol(self, newvalue):
        self.column = newvalue

    def getChar(self):
        return self.sn_char
    def getRow(self):
        return self.row
    def getCol(self):
        return self.column

    # generate new row coordinates
    def moveSnitchRow(self):
        num = random.randint(0,2)
        if num == 1:
            return self.row + 1
        elif num == 2:
            return self.row - 1
        # leave the same row position
        return self.row

    # generate new column coordinates
    def moveSnitchCol(self):
        num = random.randint(3,5)
        if num == 3:
            return self.column - 1
        elif num == 4:
            return self.column + 1
        # leave the same column position
        return self.column

    def toString(self):
        info = "Snitch " + self.snitch_char + " at row " + str(self.row) + " and column " + str(self.column)
        return info