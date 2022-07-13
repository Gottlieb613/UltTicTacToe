class Board:
    class BoxNode:
        class TileNode:
            def __init__(self):
                self.player = 0

        def __init__(self):
            self.player = 0
            self.tiles = [self.TileNode() for i in range(9)]

    def __init__(self):
        self.boxes = [self.BoxNode() for i in range(9)]
        self.win = False
    
    def update(self, box, tile, new_val):
        self.boxes[box][tile].player = new_val
    
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
                
    
