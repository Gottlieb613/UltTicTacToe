import sys
import pygame as pg


from Board import *


#Initializing pygame and the display
pg.init()
pg.display.set_caption('Ultimate Tic Tac Toe')

#Global variables
#   Can play around with the values of line_width and tile_font
line_width = 4
tile_length = 50
box_length = 3 * tile_length + 2 * line_width
screen_size = 3 * box_length, 3 * box_length
tile_font = pg.font.SysFont('Arial', 10)
screen = pg.display.set_mode(screen_size)
was_pressed = False


def draw_background():
    screen.fill(pg.Color("white"))

'''
TODO: why does it, for some boxes, highlight more
than just the particular box? for example, if the middle
box (4) is next_box, then boxes 4,5,7,8 will all be be highlighted
the same is true for the left box (3): 3,6 will all be highglighted.
* Figure out why.
Note: might be an issue in the DRAWING segment of game_loop as opposed to here'''
def draw_box(box, color):
    top_left = get_box_coords(box)
    bottom_right = top_left[0] + box_length, top_left[1] + box_length
    
    pg.draw.rect(screen, color, pg.Rect(top_left, bottom_right))


def draw_lines():
    #Draw the inner tile lines
    for i in range(10):
        line_color = pg.Color("grey")
        if i % 3 != 0: 
            pg.draw.line(screen, pg.Color(line_color), (i * box_length // 3, 0), (i * box_length // 3, screen_size[0]), line_width)
            pg.draw.line(screen, pg.Color(line_color), (0, i * box_length // 3), (screen_size[0], i * box_length // 3), line_width)
    
    #then afterwards draw the outer box lines
    # do them in successive loops instead of the same loop because I want
    # these lines to be on TOP of the tile ones
    for i in range(10):
        line_color = pg.Color("blue")
        if i % 3 == 0:
            pg.draw.line(screen, pg.Color(line_color), (i * box_length // 3, 0), (i * box_length // 3, screen_size[0]), line_width)
            pg.draw.line(screen, pg.Color(line_color), (0, i * box_length // 3), (screen_size[0], i * box_length // 3), line_width)


def draw_symbol(box, tile, symbol):
    directory = f"./Images/{symbol}.png"
    image = pg.image.load(directory)
    screen.blit(image, get_tile_coords(box, tile))

def get_box_coords(box):
    return get_tile_coords(box, 0)

def get_tile_coords(box, tile):
    x_board, y_board = Board.tile_box_to_board(box, tile)

    x = x_board * (line_width + tile_length)
    y = y_board * (line_width + tile_length)

    return x, y

#just the inverse of get_tile_coords above
def get_coords_tile(x, y):
    x_board = x // (line_width + tile_length)
    y_board = y // (line_width + tile_length)

    return Board.board_to_tile_box(x_board, y_board)




def game_loop(board, clock):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    
    #------DRAWING-------
    draw_background()
    for i in range(9): #draw box colors
        if i == board.get_next_box(): #highlight the next box
            draw_box(board.get_next_box(), pg.Color("yellow"))
        # elif not board.check_box_accessible(i): #grey out inaccessible boxes
        #     draw_box(board.get_next_box(), pg.Color("azure2"))
        # else: #for normal boxes
        #     draw_box(board.get_next_box(), pg.Color("white"))
        #     #force it to be white even though the background it
        #     # because i had an issue with boxes getting highlighted even
        #     # though they are not next_box
        '''
        TODO: figure out why the above lines, when not commented out
        generate strange behavior with the box highlights
            - ex: the wrong box being grey (azure2) when one is inacessible
        Even with those lines commented out, the yellow highlight does
        hit boxes that are not included. not sure why. figure it out'''
    draw_lines()

        #draw tile x's and o's
    for i in range(9):
        for j in range(9):
            symbol = board.get_tile(i, j)
            if symbol == 1:
                draw_symbol(i, j, "cross")
            elif symbol == 2:
                draw_symbol(i, j, "circle")
        
        #draw box x's and o's
        symbol_big = board.get_box(i)
        if symbol_big == 1:
            draw_symbol(i, 0, "cross_big")
        elif symbol_big == 2:
            draw_symbol(i, 0, "circle_big")


    #------PLAYER CLICKING------
    global was_pressed 
        #this var is so that we only process a click
        # the moment it was released, and only for a single frame
    if pg.mouse.get_pressed()[0]:
        was_pressed = True
    elif not pg.mouse.get_pressed()[0] and was_pressed:
        was_pressed = False
        mouse_x, mouse_y = pg.mouse.get_pos()
        mouse_box, mouse_tile = get_coords_tile(mouse_x, mouse_y)
        print(f"box: {mouse_box}, tile: {mouse_tile}")

        if board.place_tile_full(mouse_box, mouse_tile, board.get_player()):
            #switch player
            board.next_player()

            print(board)
            board.print_boxes()

            if board.win:
                print("You win!")



    # font = tile_font.render('Hello!', True, pg.Color("black"))
    # screen.blit(font, get_tile_coords(5, 4))

    pg.display.flip()
    

def main():
    board = Board()
    clock = pg.time.Clock

    while 1:
        game_loop(board, clock)

if __name__ == "__main__": 
    main()

'''
TODO: for some reason the wrong tile is updated on a given click, not sure why'''