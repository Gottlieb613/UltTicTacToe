import sys
import pygame as pg


from Board import *


#Initializing pygame and the display
pg.init()
pg.display.set_caption('Ultimate Tic Tac Toe')

#Global variables
#   Can play around with the values of line_width and tile_font
line_width = 4
tile_size = 50
box_length = 3 * tile_size + 2 * line_width
screen_size = 3 * box_length, 3 * box_length
tile_font = pg.font.SysFont('Arial', 10)
screen = pg.display.set_mode(screen_size)


def draw_background():
    screen.fill(pg.Color("white"))


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




'''
TODO: figure out why is it not okay for me to use the static Board.tile_box_to_board(box, tile)?
it gave me a 'type object 'Board' has no attribute 'type_box_to_board' and i do not know why
i could skip the first few lines by just calling that function from Board
'''
def get_tile_coords(box, tile):
    '''TODO:
    this doesnt work lol. might have the math wrong for x_board and y_board or x, y
    '''


    x_board, y_board = Board.tile_box_to_board(box, tile)

    x = x_board * (line_width + tile_size)
    y = y_board * (line_width + tile_size)

    return x, y

#just the inverse of get_tile_coords above
def get_coords_tile(x, y):
    x_board = x // (line_width + tile_size)
    y_board = y // (line_width + tile_size)

    return Board.board_to_tile_box(x_board, y_board)




def game_loop(board, clock):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    
    #------DRAWING-------
    draw_background()
    draw_lines()
        #draw tile x's and o's
    for i in range(9):
        for j in range(9):
            symbol = board.get_tile(i, j)
            if symbol == 1:
                draw_symbol(i, j, "cross")
            elif symbol == 2:
                draw_symbol(j, j, "circle")
        #draw box x's and o's
    for i in range(9):
        symbol_big = board.get_box(i)
        if symbol_big == 1:
            draw_symbol(i, 0, "cross_big")
        elif symbol_big == 2:
            draw_symbol(j, 0, "circle_big")


    #------GAMEPLAY------
    if pg.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pg.mouse.get_pos()
        mouse_box, mouse_tile = get_coords_tile(mouse_x, mouse_y)
        print(f"box: {mouse_box}, tile: {mouse_tile}")
        board.update_tile(mouse_box, mouse_tile, board.get_player())

    # font = tile_font.render('Hello!', True, pg.Color("black"))
    # screen.blit(font, get_tile_coords(5, 4))

    pg.display.flip()

    #switch player
    board.next_player()
    

def main():
    board = Board()
    clock = pg.time.Clock

    while 1:
        game_loop(board, clock)

if __name__ == "__main__": 
    main()