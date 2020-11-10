class checkColRowSubox:
    def __init__(self, indexCol, indexRow, db):
        self.indexCol = indexCol
        self.indexRow = indexRow
        self.db = db

    def checkRow(self):
        strRow = "".join(self.db[self.indexRow]).replace(".", "")
        if len(set(strRow)) == len(strRow):
            return True
        else:
            return False

    def checkCol(self):
        strCol = "".join([row[self.indexCol] for row in self.db]).replace(".", "")
        if len(set(strCol)) == len(strCol):
            return True
        else:
            return False

    def checkSubox(self):
        startRowSubox = 3*int(self.indexRow/3)
        startColSubox = 3 * int(self.indexCol / 3)
        strSubox = "".join(["".join(row[startColSubox:startColSubox+3])
                            for row in self.db[startRowSubox:startRowSubox+3]]).replace(".", "")
        if len(set(strSubox)) == len(strSubox):
            return True
        else:
            return False


board = [[".", ".", "5", ".", ".", ".", ".", ".", "."],
         ["1", ".", ".", "2", ".", ".", ".", ".", "."],
         [".", ".", "6", ".", ".", "3", ".", ".", "."],
         ["8", ".", ".", ".", ".", ".", ".", ".", "."],
         ["3", ".", "1", "5", "2", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "4", "."],
         [".", ".", "6", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "9", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]


indexCol = 0
timesCol = 0

indexRow = 0

while indexRow < len(board):
    if checkColRowSubox(indexCol, indexRow, board).checkRow() and checkColRowSubox(indexCol, indexRow, board).checkCol() and checkColRowSubox(indexCol, indexRow, board).checkSubox():
        indexRow += 1
        timesCol += 1
        indexCol = (timesCol % 3 + int(indexRow/3)) % 3 + 3*(timesCol % 3)
    else:
        print(False)
