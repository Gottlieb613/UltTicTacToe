import sys
import pygame as pg

from Board import *
    
#Global variables
#   Can play around with the values   
line_width = 10
tile_size = 50
box_length = 3 * tile_size + 2 * line_width
screen_size = 3 * box_length, 3 * box_length
black = (255, 255, 255)
red = (255, 0, 0)
tile_font = pg.font.SysFont('Arial', 10)

pg.init()
pg.display.set_caption('Ultimate Tic Tac Toe')
screen = pg.display.set_mode(screen_size)

def draw_background():
    screen.fill((0, 0, 0))

def draw_box(xleft, ytop):
    pg.draw.rect(screen, red, pg.Rect(xleft, ytop, box_length, box_length), 2)
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

'''
def main():
    pygame.init()
    font = pygame.font.SysFont('Arial', 25)
    screen_h = 1000
    screen_w = 1000

    win = pygame.display.set_mode((screen_w, screen_h))
    win.fill((0, 0, 0))
    pygame.display.set_caption("Ultimate Tic Tac Toe")

    box_side = 10

    b = Board()
'''


while 1:
    game_loop()