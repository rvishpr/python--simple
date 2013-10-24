#!/router/bin/python-2.7.1
#Solution to the nQueens problem via backtracking
import sys

class Board:
    def __init__(self, size, showAll, countOnly):
        self.board = [[0 for x in range(size)]for y in range(size)]
        self.size = size
        self.showAll = showAll
        self.count = 0
        self.countOnly = countOnly

    def __repr__(self):
        for i in self.board:
            for j in i:
                print j,
            print
        return ""

    ##############################################################
    # Clears the board from the given row (used when backtrasking)
    ##############################################################
    def clear_board(self, start_row):
        for x in range(start_row, self.size):
            for y in range(0, self.size):
                self.board[x][y] = 0

    ##############################################################
    # Checks if current placement of the queen is a valid one
    # Check current row, column and both diagonals
    ##############################################################
    def is_valid_placement(self, row, column):
        if 1 not in self.board[row]:
            if 1 not in [self.board[x][column] for x in range(self.size)]:
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
                while i < self.size and j < self.size:
                    if 1 == self.board[i][j]:
                        return False
                    i += 1
                    j += 1

                #bottom left---->top right
                if (row + column) >= (self.size - 1):
                    i = self.size - 1
                    j = row + column - (self.size - 1)
                else:
                    i = row + column
                    j = 0
                while i >= 0 and j < self.size:
                    if 1 == self.board[i][j]:
                        return False
                    i -= 1
                    j += 1
            else:
                return False
        else:
            return False
        return True

    ##############################################################
    # Function to solve the puzzle.
    # This is recursively called to solve, and if needed,
    #   backtrack, row by row until the entire function is solved.
    # This either prints all the possibilities or exits after the
    #   first solution found, based on the value of the
    #   showAll flag
    ##############################################################
    def solve(self, current_row):
        for column in range(self.size):
            self.clear_board(current_row)
            if self.is_valid_placement(current_row, column):
                self.board[current_row][column] = 1
                if current_row == (self.size - 1):
                    if not self.countOnly:
                        print "valid solution:"
                        print self
                    self.count += 1
                    if not self.showAll and not self.countOnly:
                        return True
                    return False
                else:
                    if self.solve(current_row + 1):
                        return True
                    else:
                        continue
            else:
                continue

        #if code reaches here, no valid placement in the column.
        #clear board and return False
        self.clear_board(current_row)
        return False

def main():
    n = 8
    num = False
    showAll = False
    countOnly = False
    usage = "Usage:\n./queens8 [-s | --showAll] [{-n | --numQueens} <num>] [-c | --countOnly]"
    if len(sys.argv) > 1:
        for x in range(1, len(sys.argv)):
            arg = sys.argv[x]
            if arg == '-s' or arg == '--showAll':
                showAll = True
                if countOnly:
                    print 'Both showAll[-s] and countOnly[-c] cannot be given as options'
                    print usage
                    return
            elif arg == '-n' or arg == '--numQueens':
                if len(sys.argv) > x + 1:
                    n = int(sys.argv[x + 1])
                    num = True
                else:
                    print usage
                    return
            elif arg == '-c' or arg == '--countOnly':
                countOnly = True
                if showAll:
                    print 'Both showAll[-s] and countOnly[-c] cannot be given as options'
                    print usage
                    return
            elif num:
                num = False
                continue
            else:
                print usage
                return

    chess = Board(n, showAll, countOnly)

    print chess
    chess.solve(0)

    if showAll or countOnly:
        print "Total number of solutions is:", chess.count

if __name__ == '__main__':
    main()
