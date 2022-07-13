import sys
import pygame as pg

from Board import *


#Initializing pygame and the display
pg.init()
pg.display.set_caption('Ultimate Tic Tac Toe')
    
#Global variables
#   Can play around with the values   
line_width = 10
tile_size = 50
box_length = 3 * tile_size + 2 * line_width
screen_size = 3 * box_length, 3 * box_length
tile_font = pg.font.SysFont('Arial', 10)
screen = pg.display.set_mode(screen_size)

def draw_background():
    screen.fill(pg.Color("white"))

def draw_box(xleft, ytop):

        #to figure out: why can i set the border to red but
        #   not the inside fill?
    pg.draw.rect(screen, pg.Color("blue"), pg.Rect(xleft, ytop, box_length, box_length), 2)
    
    #Not sure why the font 'is not initialized
    font = tile_font.render('Hello!', True, (255,0,0))
    screen.blit(font, (200, 100))


def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    
    draw_background()
    for i in range(3):
        for j in range(3):
            draw_box(i * box_length, j * box_length)

    pg.display.flip()
    

while 1:
    game_loop()