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
    
    def update(self, box, tile, new_val):
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



b = Board()
b.update(4, 2, 1)
b.update(5, 1, 1)
b.update(8, 4, 2)

print(b)


                
    
