from objects import *

pl = Player_Test(250, 100, 10, None, 50, 100, (125, 125, 125))
lv = Level(50, 200, 100, 50, (0, 125, 0))
def random_lvl():
    global lv
    r_lvl = random.randint(1, 2)
    if r_lvl == 1:
        lv = Level(100, 200, 100, 50, (0, 125, 0))
    elif r_lvl == 2:
        lv = Level(400, 200, 100, 50, (0, 125, 0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(main_window)
    pl.draw()
    pl.update()
    lv.draw()
    if lv.rect.colliderect(pl.rect):
        pl.stop()
    if pl.rect.centerx >= win_width - pl.width:
        random_lvl()
        pl.rect.centerx = 0
        print("A")
    pygame.display.update()
    clock.tick(FPS)
