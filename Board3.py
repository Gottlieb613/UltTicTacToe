
class Board3:
    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]
        self.box_board = [[0 for i in range(3) for j in range(3)]]
        self.win = False

    def get_board(self):
        return self.board
    
    def update(self, row, col, new_val):
        self.board[row][col] = new_val

    def update_box(self, row, col, new_val):
        row = row // 3
        col = col // 3

        self.box_board[row][col] = new_val
    
    def check_empty(self, row, col):
        return self.board[row][col] == 0 

    def check_board_complete(self, row, col):
        row = row // 3
        col = col // 3
        
        return self.check_complete_helper(row, col, self.board)
    
    def check_box_board_complete(self, row, col):
        return self.check_complete_helper(0, 0, self.box_board)
    
    #input: any tile coordinates and which board you're checking (i.e. self.board or self.box_board)
    #check that there is a completed row/col/diag, and return that player
    def check_complete_helper(self, row, col, b):

        #get top-left coordinate of that box
        #this allows us to input ANY tile coordinate, and 
        #then replace row and col with the coord of the box it is in
        row = row - (row % 3)
        col = col - (col % 3)
        
        for i in range(3):
            #check row
            i_row = row + i
            top_row = b[i_row][col]
            if top_row != 0 and top_row == b[i_row][col + 1] == b[i_row][col + 2]:
                return top_row

            #check col
            i_col = col + i
            left_col = b[row][i_col]
            if left_col != 0 and left_col == b[row + 1][i_col] == b[row + 2][i_col]:
                return left_col

        #check diagonals
        middle = b[row + 1][col + 1]
        if  (   middle != 0 and
                (middle == b[row][col] == b[row + 2][col + 2] or #topleft-bottomright
                middle == b[row + 2][col] == b[row][col + 2])):  #topright-bottomleft
            return middle
        
        #no solutions
        return 0

    def place_tile_full(self, row, col, player):
        if (player < 1 or player > 2):
            print("invalid player")
            return False
        
        #if either is out of range, return False
        if not (0 <= row, col <= 8):
            print("coordinates out of range")
            return False
        
        #already full spot
        if not self.check_empty(row, col):
            print("that spot is already full")
            return False
        
        self.update(row, col, player)

        #now check if that player completed the box
        box_win = self.check_board_complete(row, col)
        if box_win > 0:
            print(f"Player {player} has completed the box!")
            self.update_box(row, col, player)

            #now check if that player won
            full_win = self.check_box_board_complete(row, col)
            if full_win > 0:
                print(f"Player {player} has won the game!")
                self.win = True

        return True
        


    def __repr__(self):
        rep = ""
        for i in range(9):
            for j in range(9):
                rep += str(self.board[i][j])
                if (j % 3 == 2):
                    rep += " "
            rep += "\n"
            if i % 3 == 2:
                rep += "\n"
        
        return rep

       


            
                


    
