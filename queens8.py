#!/router/bin/python-2.7.1
import sys

class Board:
    def __init__(self, size):
        self.board = [[0 for x in range(size)]for y in range(size)]
        self.size = size

    def __repr__(self):
        for i in self.board:
            for j in i:
                print j,
            print
        return ""

    def clear_board(self, start_row):
        for x in range(start_row, self.size):
            for y in range(0, self.size):
                self.board[x][y] = 0
        #print self

    def is_valid_placement(self, row, column):
        if 1 not in self.board[row]:
            if 1 not in [self.board[x][column] for x in range(8)]:
                tmplistud = []
                tmplistdu = []
                #top left---->bottom right
                if row > column:
                    i = row - column
                    j = 0
                elif row < column:
                    i = 0
                    j = column - row
                else:
                    i = j = 0
                while i < 8 and j < 8:
                    if 1 == self.board[i][j]:
                        return False
                    i += 1
                    j += 1

                #bottom left---->top right
                if (row + column) >= 7:
                    i = 7
                    j = row + column - 7
                else:
                    i = row + column
                    j = 0
                while i >= 0 and j < 8:
                    if 1 == self.board[i][j]:
                        return False
                    i -= 1
                    j += 1
            else:
                return False
        else:
            return False
        return True

    def solve(self, current_row):
        for column in range(self.size):
            self.clear_board(current_row)
            if self.is_valid_placement(current_row, column):
                self.board[current_row][column] = 1
                #print "'", current_row, column, "' is a valid placement"
                if current_row == 7:
                    print "valid solution:"
                    print self
                    return False
                else:
                    #print " here "
                    if self.solve(current_row + 1):
                        return True
                    else:
                        continue
            else:
                #print "'", current_row, column, "' is not a valid placement"
                continue

        #if code reaches here, no valid placement in the column.
        #clear board and return False
        self.clear_board(current_row)
        return False

def main():
    n = 8

    chess = Board(8)

    print chess
    chess.solve(0)
    print chess

if __name__ == '__main__':
    main()
