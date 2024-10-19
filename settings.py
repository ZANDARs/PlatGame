import pygame
from pygame import font
import random

pygame.init()

win_width = 800
win_height = 600

FPS = 60

font_ = font.Font(None, 65)
win = pygame.display.set_mode((win_width, win_height))
main_window = (127, 132, 255)
menu_window = (0, 0, 77)
color = (0, 247, 2)
bt_text = font_.render("Start", True, (255, 255, 255))
bt_text_shop = font_.render("Shop", True, (255, 255, 255))
bt_shop_frst = font_.render("GUN1", True, (255, 255, 255))
bt_shop_scnd = font_.render("GUN2", True, (255, 255, 255))
bt_shop_trd = font_.render("GUN3", True, (255, 255, 255))
bt_shop_fr = font_.render("PAS", True, (255, 255, 255))
back_text = font_.render("Back", True, (255, 255, 255))
bt_restart = font_.render("Restart", True, (255, 255, 255))
bt_menu = font_.render("Menu", True, (255, 255, 255))
die_text = font_.render("Die", True, (255, 255, 255))

lvl_grp = pygame.sprite.Group()

clock = pygame.time.Clock()