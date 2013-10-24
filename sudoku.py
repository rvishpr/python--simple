#!/router/bin/python-2.7.1
import sys

class Sudoku:
    def __init__(self, size):
        self.board = [[3,0,0,8,9,0,0,0,0],
                [9,7,0,0,0,3,0,0,0],
                [0,0,2,0,0,4,0,0,0],
                [2,8,0,0,0,9,0,0,1],
                [1,0,0,0,0,0,0,0,8],
                [6,0,0,2,0,0,0,4,9],
                [0,0,0,1,0,0,4,0,0],
                [0,0,0,9,0,0,0,1,5],
                [0,0,0,0,4,7,0,0,3]]
        self.solution = [[3,0,0,8,9,0,0,0,0],
                [9,7,0,0,0,3,0,0,0],
                [0,0,2,0,0,4,0,0,0],
                [2,8,0,0,0,9,0,0,1],
                [1,0,0,0,0,0,0,0,8],
                [6,0,0,2,0,0,0,4,9],
                [0,0,0,1,0,0,4,0,0],
                [0,0,0,9,0,0,0,1,5],
                [0,0,0,0,4,7,0,0,3]]

        self.size = size

    def print_line(self):
        print "+ - - - + - - - + - - - +"

    def __repr__(self):
        self.print_line()
        count = 0

        for i in self.board:
            col = 0
            for j in i:
                if col %3 == 0:
                    print '|',
                col += 1
                if j == 0:
                    j = '.'
                print j,
            print '|'
            count+=1
            if count %3 == 0:
                self.print_line()
        return ""

    def is_valid_placement(self, row, column, value):
        if value not in self.solution[row]:
            if value not in [self.solution[rr][column] for rr in range(self.size)]:
                row_s = (row / 3) * 3
                col_s = (column / 3) * 3
                for x in range(row_s, row_s + 3):
                    for y in range(col_s, col_s + 3):
                        if self.solution[x][y] == value:
                            return False
            else:
                return False
        else:
            return False
        self.solution[row][column] = value
        return True

    def clear_board(self, start_row, start_col):
        for x in range(start_row, self.size):
            for y in range(start_col, self.size):
                self.solution[x][y] = self.board[x][y]

    def solve(self, start_row = 0, start_col = 0):
        value = 1
        while value <= self.size:
            if self.solution[start_row][start_col] == 0:
                is_valid = self.is_valid_placement(start_row, start_col, value)
            else:
                is_valid = True
                value = self.size
            if is_valid:
                new_start_col = start_col + 1
                new_start_row = start_row
                if new_start_col >= self.size:
                    new_start_col = 0
                    new_start_row = start_row + 1
                    if new_start_row >= self.size:
                        return True
                if not self.solve(new_start_row, new_start_col):
                    self.clear_board(start_row, start_col)
                else:
                    return True
            value = value + 1
        return False

def main():
    puzzle = Sudoku(9)

    puzzle.solve()
    print puzzle
    puzzle.board = puzzle.solution
    print puzzle

if __name__ == '__main__':
    main()
