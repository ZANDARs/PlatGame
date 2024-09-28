import pygame
from pygame import font
import random

pygame.init()

win_width = 700
win_height = 500

FPS = 60

font_ = font.Font(None, 65)
win = pygame.display.set_mode((win_width, win_height))
main_window = (127, 132, 255)
menu_window = (0, 0, 77)


clock = pygame.time.Clock()