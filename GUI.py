import sys
import pygame as pg
from Board import *

#Initializing pygame and the display
pg.init()
pg.display.set_caption('Ultimate Tic Tac Toe')

DEBUG = False

#Global variables
#   Can play around with the value of line_width
line_width = 4
tile_length = 50
box_length = 3 * tile_length + 2 * line_width
screen_length = 9 * tile_length + 10 * line_width
screen = pg.display.set_mode((screen_length, screen_length))
was_pressed = False
last_box_tile = None
board = None

#Global colors
color_background = pg.Color("white")
color_box_line = pg.Color("blue")
color_tile_line = pg.Color("grey")
color_box_highlight = pg.Color("yellow")
color_box_full = pg.Color("azure2")
color_last_tile = pg.Color("lightgreen")

def draw_background():
    screen.fill(color_background)

def draw_box(box, color):
    top_left = get_box_coords(box)

    pg.draw.rect(screen, color, pg.Rect(top_left, (box_length, box_length)))

def draw_lines():
    #Draw the inner tile lines
    line_color = color_tile_line
    for i in range(10):
        if i % 3 != 0:
            next_line = i * (tile_length + line_width)
            pg.draw.line(screen, line_color, (next_line, 0), (next_line, screen_length), line_width)
            pg.draw.line(screen, line_color, (0, next_line), (screen_length, next_line), line_width)
    
    #then afterwards draw the outer box lines
    # do them in successive loops instead of the same loop because I want
    # these lines to be on TOP of the tile ones
    line_color = color_box_line
    for i in range(10):
        if i % 3 == 0:
            next_line = i * (tile_length + line_width)
            pg.draw.line(screen, line_color, (next_line, 0), (next_line, screen_length), line_width)
            pg.draw.line(screen, line_color, (0, next_line), (screen_length, next_line), line_width)

def draw_symbol(box, tile, symbol):
    directory = f"./Images/{symbol}.png"
    image = pg.image.load(directory)
    x, y = get_tile_coords(box, tile)
    screen.blit(image, (x, y))

def draw_fill_last_tile():
    if last_box_tile is not None: #at start it is None
        box, tile = last_box_tile
        x, y = get_tile_coords(box, tile)
        pg.draw.rect(screen, color_last_tile, pg.Rect((x, y), (tile_length, tile_length)))

def draw_all(board):
    draw_background()
    for i in range(9): #draw box colors
        if      i == board.get_next_box() or (
                board.get_next_box() == -1 and board.check_box_accessible(i)): #highlight the next box– highlight ALL if can go in any box
            draw_box(i, color_box_highlight)
        if not board.check_box_accessible(i): #grey out inaccessible boxes
            draw_box(i, color_box_full)
    draw_fill_last_tile()
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

def write_message(message):
    pg.display.set_caption(f'Ultimate Tic Tac Toe | {message}')

def get_box_coords(box):
    return get_tile_coords(box, 0)

def get_tile_coords(box, tile):
    x_board, y_board = Board.tile_box_to_board(box, tile)

    x = line_width + x_board * (line_width + tile_length)
    y = line_width + y_board * (line_width + tile_length)

    return x, y

#just the inverse of get_tile_coords above
def get_coords_tile(x, y):
    x_board = x // (line_width + tile_length)
    y_board = y // (line_width + tile_length)

    return Board.board_to_tile_box(x_board, y_board)

def game_loop():
    #exiting
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    
    #------DRAWING-------
    draw_all(board)

    #------PLAYER CLICKING------
    global was_pressed 
        #this var is so that we only process a click
        # the moment it was released, and only for a single frame
    if pg.mouse.get_pressed()[0]:
        was_pressed = True

    elif not pg.mouse.get_pressed()[0] and was_pressed: #run on release of mouse
        was_pressed = False

        if board.win:
            reset()
        
        else:
            mouse_x, mouse_y = pg.mouse.get_pos()
            mouse_box, mouse_tile = get_coords_tile(mouse_x, mouse_y)
            
            if DEBUG: print(f"box: {mouse_box}, tile: {mouse_tile}"); print(f"x: {mouse_x}, y: {mouse_y}")

            if board.place_tile_full(mouse_box, mouse_tile, board.get_player()):
                global last_box_tile
                last_box_tile = (mouse_box, mouse_tile)

                if DEBUG: print(board); board.print_boxes()

                if board.win:
                    write_message(f"{board.get_player_symbol()} wins! Click to restart")
                    pg.display.flip()
                    #TODO: add a play again selection, and reset board and the other variables
                        # would prob need to add a board_reset function in Board.py
            
                if not board.win:
                    #switch player
                    board.next_player()
                    write_message(f"Good spot! {board.get_player_symbol()}'s turn.")
            else:
                write_message(f"Illegal move, try again. {board.get_player_symbol()}'s turn.")

    pg.display.flip()

def reset():
    board.reset_board()
    write_message("X begins")
    global last_box_tile
    last_box_tile = None


    

def main():
    global board
    board = Board()
    clock = pg.time.Clock()

    while 1:
        game_loop()
        clock.tick(20)

if __name__ == "__main__": 
    main()