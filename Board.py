class Board:
    class BoxNode:
        class TileNode:
            def __init__(self):
                self.player = 0
            
            def __repr__(self):
                return str(self.player)

        def __init__(self):
            self.player = 0
            self.tiles = [self.TileNode() for i in range(9)]

    def __init__(self):
        self.boxes = [self.BoxNode() for i in range(9)]
        self.win = False
        self.player = 1
    
    def get_player(self):
        return self.player
    
    def next_player(self):
        if self.player == 1:
            self.player = 2
        else:
            player = 1

    
    def get_tile(self, box, tile):
        return self.boxes[box].tiles[tile].player
    
    def get_box(self, box):
        return self.boxes[box].player
    
    def update_tile(self, box, tile, new_val):
        self.boxes[box].tiles[tile].player = new_val
    
    def update_box(self, box, new_val):
        self.boxes[box].player = new_val

    def check_empty(self, box, tile):
        return self.boxes[box][tile].player == 0
    
    def check_box_accessible(self, box):
        if self.boxes[box].player != 0: #if this has been 'completed'
            return True

        for tile in self.boxes[box].tiles:
            if (tile.player == 0): #if there is at least one empty tile
                return False
        return True #if no empty tiles then it is full

    def check_box_complete(self, box):
        return self.check_complete_helper(self, box)

    def check_board_complete(self):
        return self.check_complete_helper(self, self.boxes)

    def check_complete_helper(self, box):
        for i in range(3):

            #checking each row (compare 012, 345, and 678)
                #using t as temp var to shorten the expression
            t = 3 * i
            if (box[t].player == box[t + 1].player == box[t + 2].player):
                return box[t].player

            #checking each col (compare 036, 147, and 258)
            if (box[i].player == box[i + 3].player == box[i + 6].player):
                return box[i].player

        #manually checking both diagonals
        middle = box[4].player
        if (box[0].player == middle == box[8].player or box[2].player  == middle == box[6].player):
            return middle

        #no wins found so return 0
        return 0

    def __repr__(self):
        rep = ""
        next = 0, 0
        while next is not None:
            next_box = next[0]
            next_tile = next[1]
            
            rep += str(self.boxes[next_box].tiles[next_tile])
            if (next_tile % 3 == 2):
                rep += " "
            if next_box % 3 == 2 and next_tile % 3 == 2:
                rep += "\n"
                if next_tile == 8:
                    rep += "\n"

            next = self.next_tile(next[0], next[1])

        return rep
    
    def tile_box_to_board(box, tile):
        x_box = box % 3
        y_box = box // 3
        x_tile = tile % 3
        y_tile = tile // 3

        x_board = 3 * x_box + x_tile
        y_board = 3 * y_box + y_tile

        return x_board, y_board
    
    def board_to_tile_box(x, y):
        x_box = x // 3
        y_box = y // 3
        box = 3 * y_box + x_box

        x_tile = x % 3
        y_tile = y % 3
        tile = 3 * y_tile + x_tile

        return box, tile

    #The idea for this function is that it will return
    # the box, tile pair for the tile to the RIGHT
    # of the input one, and if it is at the end of the 
    # 9-tile row, then it goes to the next row
    #Returns None if given the bottom right tile of the board
    def next_tile(self, box, tile):
        box_row = box / 3
        box_col = box % 3
        tile_row = tile / 3
        tile_col = tile % 3

        if (tile_col < 2): #stay in box-> just move right
            return box, tile + 1

        else: #so we're in the rightmost col in the box
            if box_col < 2: #stay in box-row -> move to corresp. row in box to right
                return box + 1, tile - 2 #tile-2 allows us to go to 'start' of row in box

            else: #rightmost box of the row
                if tile_row < 2: #so just move to leftmost box of same row and next tile-row
                    return box - 2, tile + 1
                
                else: #bottom right of the rightmost box
                    if box_row < 2: #so we're NOT in the bottom right box
                        return box + 1, 0   #zero because we start at top left of new box
                    
                    else: #literally ONLY the bottom right tile of bottom right box, so end here
                        return None




                
    


'''
OLD CODE FOR CHECKING THAT A SPOT IS LEGAL
this was when I had the row/col 2d arraysystem
instead of the current box/tile tree system


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
'''