'''
Created on 20 Oct 2016

@author: william
'''

import pygame
from pygame import display

from environment import create_grid, unit

x_blocks = 10  # int(input('x_blocks: '))
y_blocks = 10  # int(input('y_blocks: '))
GUI = display.set_mode([x_blocks * unit + 1, y_blocks * unit + 1])

if __name__ == '__main__':
    pygame.init()
    create_grid(x_blocks, y_blocks)
