import sudoku_generator

class SudokuGenerator:
    def __init__(self,removed_cells,row_length=9):
        self.row_length=row_length
        self.removed_cells=removed_cells

    def get_board(self):
        self.board=[["_" for i in range(9)] for j in range(9)]
        return self.board

    def print_board(self):
        for r in self.board:
            for c in r:
                print(c, end=" ")
            print()

    #To be added

    #Vaildity
    def valid_in_row(self, row, num):
        #returns True or False
    def valid_in_col(self, col, num):
        #return T or F
    def valid_in_box(self, row_start, col_start, num):
        #return T or F
    def is_valid(self, row, col, num):
        #return T/F

    #filling
    def fill_box(self, row_start, col_start):
        #randomly fills in values in 3x3 box
    def fill_diagonal(self):
        #fill box
    def fill_remaining(self):
        #method is prvoided
    def fill_values(self):
        #method provided
        #calls fill_diagonal & remaining
    def remove_cells(self):
        #remove random cells

def generate_sudoku(size, removed):
    #calls class appropriatly








