from database import *
from objects import *

# Ініціалізація Pygame
shop = False
game = False
finish = True
die = False
# Вікно та кольори
lvl_rec = 0
# Ініціалізація гравця та рівнів
pl = Player_Test(250, 100, 10, None, 50, 100, (125, 125, 125))
lvl_grp = pygame.sprite.Group()  # Створюємо групу рівнів
main_map = ["WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "W---W-------------------------W",
            "W---W-------------------------W",
            "W---W-------------------------W",
            "W----W------------------------W",
            "W----W------------------------W",
            "W-----------------------------W",
            "W-----------------------------W",
            "W-----------------------------W",
            "W-----------------------------W",
            "W-----------------------------W",
            "W-----------------------------W",
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"]

main_map1 = ["WWWWWWWWWW",
            "W---W----W",
            "W---W----W",
            "W---W----W",
            "W----W---W",
            "W----W---W",
            "W--------W",
            "W--------W",
            "W--------W",
            "WWWWWWWWWW"]

main_map2 = ["WWWWWWWWWW",
            "W---W----W",
            "W---W----W",
            "W---W----W",
            "W----W---W",
            "W----W---W",
            "W--------W",
            "W--------W",
            "W--------W",
            "WWWWWWWWWW"]

main_map3 = ["WWWWWWWWWW",
            "W---W----W",
            "W---W----W",
            "W---W----W",
            "W----W---W",
            "W----W---W",
            "W--------W",
            "W--------W",
            "W--------W",
            "WWWWWWWWWW"]

main_map4 = ["WWWWWWWWWW",
            "W---W----W",
            "W---W----W",
            "W---W----W",
            "W----W---W",
            "W----W---W",
            "W--------W",
            "W--------W",
            "W--------W",
            "WWWWWWWWWW"]
len_y = len(main_map)
height_block = win_height // len_y
# Функція генерації випадкового рівня
def random_lvl():
    # for y, row in enumerate(main_map):
    #     y *= height_block
    #     for x, sym in enumerate(row):
    #         len_x = len(row)
    #         width_block = win_width // len_x
    #         x *= width_block
    #         if sym == "W":
    #             lvl_grp.add(Level(x, y, width_block, height_block, "Textures/2_lvl.png"))
    global lv, lv1, lv2, lv3, lv4, lv5, lv6, lv7, lv8, lv9, lv10, lv11, lv12, lv13, spikes
    r_lvl = random.randint(1, 5)
    lvl_grp.empty()  # Очищаємо групу перед генерацією нового рівня

    # # Спільна підлога для всіх рівнів
    for i in range(32):  # Підлога на всю ширину екрана
         lv2 = Level(25 * i, 575, 50, 50, "Textures/2_lvl.png")  # Підлога внизу екрану
         lvl_grp.add(lv2)

    if r_lvl == 1:
         print(1)
         # Рівень з кількома платформами
         lv = Level(50, 200, 50, 50, "Textures/1_lvl.png")
         lv7 = Level(100, 200, 50, 50, "Textures/3_lvl.png")
         lv1 = Level(650, 200, 50, 50, "Textures/1_lvl.png")
         lv8 = Level(700, 200, 50, 50, "Textures/3_lvl.png")
         lv3 = Level(350, 475, 50, 50, "Textures/1_lvl.png")
         lv9 = Level(400, 475, 50, 50, "Textures/2_lvl.png")
         lv10 = Level(450, 475, 50, 50, "Textures/3_lvl.png")
         lv4 = Level(150, 400, 50, 50, "Textures/1_lvl.png")
         lv11 = Level(200, 400, 50, 50, "Textures/3_lvl.png")
         lv5 = Level(550, 400, 50, 50, "Textures/1_lvl.png")
         lv12 = Level(600, 400, 50, 50, "Textures/3_lvl.png")
         lv6 = Level(350, 300, 50, 50, "Textures/1_lvl.png")
         lv13 = Level(400, 300, 50, 50, "Textures/3_lvl.png")
         lvl_grp.add(lv, lv1, lv3, lv4, lv5, lv6, lv7, lv8, lv9, lv10, lv11, lv12, lv13)
    elif r_lvl == 2:
         print(2)
         # Один великий рівень з платформами в центрі та шипами
         lv = Level(250, 225, 50, 50, "Textures/1_lvl.png")
         lv1 = Level(300, 225, 50, 50, "Textures/2_lvl.png")
         lv5 = Level(350, 225, 50, 50, "Textures/2_lvl.png")
         lv6 = Level(400, 225, 50, 50, "Textures/3_lvl.png")
         lv3 = Level(200, 425, 50, 50, "Textures/1_lvl.png")
         lv4 = Level(250, 425, 50, 50, "Textures/2_lvl.png")
         lv7 = Level(300, 425, 50, 50, "Textures/2_lvl.png")
         lv8 = Level(350, 425, 50, 50, "Textures/3_lvl.png")
         lv9 = Level(50, 300, 50, 50, "Textures/1_lvl.png")
         lv10 = Level(100, 300, 50, 50, "Textures/3_lvl.png")
         lv11 = Level(500, 400, 50, 50, "Textures/1_lvl.png")
         lv12 = Level(550, 400, 50, 50, "Textures/2_lvl.png")
         lv13 = Level(600, 400, 50, 50, "Textures/3_lvl.png")
         spikes = Level(450, 530, 50, 50, "Textures/kill_lvl.png", True)  # Шипи на підлозі
         lvl_grp.add(lv, lv3, lv4, lv1, spikes, lv5, lv6, lv7, lv8, lv9, lv10, lv11, lv12, lv13)

    elif r_lvl == 3:
         print(3)
         # Рівень з платформами, що розташовані як сходинки і шипи внизу
         for i in range(6):
             # Перший блок сходинки з текстурою 1_lvl
             lv_part1 = Level(100 + i * 100, win_height - 100 - i * 50, 50, 50, "Textures/1_lvl.png")
             # Другий блок сходинки з текстурою 2_lvl
             lv_part2 = Level(150 + i * 100, win_height - 100 - i * 50, 50, 50, "Textures/3_lvl.png")
             lvl_grp.add(lv_part1, lv_part2)

         for i in range(4):  # Шипи під сходинками
             spikes = Level(200 + i * 150, 530, 50, 50, "Textures/kill_lvl.png", True)
             lvl_grp.add(spikes)

    elif r_lvl == 4:
         print(4)
         # Рівень з розсіяними платформами і шипами на деяких платформах
         lv = Level(50, 350, 50, 50, "Textures/1_lvl.png")
         lv4 = Level(100, 350, 50, 50, "Textures/2_lvl.png")
         lv5 = Level(150, 350, 50, 50, "Textures/3_lvl.png")
         lv1 = Level(400, 250, 50, 50, "Textures/1_lvl.png")
         lv6 = Level(450, 250, 50, 50, "Textures/2_lvl.png")
         lv7 = Level(500, 250, 50, 50, "Textures/3_lvl.png")
         lv3 = Level(200, 450, 50, 50, "Textures/1_lvl.png")
         lv8 = Level(250, 450, 50, 50, "Textures/2_lvl.png")
         lv9 = Level(300, 450, 50, 50, "Textures/3_lvl.png")
         spikes = Level(125, 307, 50, 50, "Textures/kill_lvl.png", True)  # Шипи на платформі
         lvl_grp.add(lv, lv1, lv3, spikes, lv4, lv5, lv6, lv7, lv8, lv9)

    elif r_lvl == 5:
         print(5)
         # Рівень з платформою біля краю екрана і плаваючими платформами, додані шипи
         lv = Level(25, 400, 50, 50, "Textures/2_lvl.png")
         lv3 = Level(75, 400, 50, 50, "Textures/3_lvl.png")
         lv1 = Level(550, 300, 50, 50, "Textures/1_lvl.png")
         lv4 = Level(600, 300, 50, 50, "Textures/3_lvl.png")
         spikes = Level(625, 530, 50, 50, "Textures/kill_lvl.png", True)  # Шипи внизу біля краю
         lvl_grp.add(lv, lv1, spikes, lv3, lv4)
def start():
    global finish, game, boss_round, lvl_rec, shop, player, die
    shop = False
    finish = False
    game = True
    pl.rect.centerx = 0
    random_lvl()
    lvl_rec = 0
    #boss_round = False
    # player = Player(100, 100, 5, player_image, 25, 25)
    # player.hp = 100
def shopp():
    #global finish, game, shop, boss_round, zomb_k, die
    #finish = False
    #shop = True
    #die = False
    pass
def guns():
    pass

def menuu():
    global finish, game, shop, boss_round, zomb_k, die
    finish = True
    #shop = False
    game = False
    die = False

bts = Button(win_width / 2, 150, 200, 50, bt_text, (50, 50, 100), callback=start)
bth = Button(win_width / 2, 250, 200, 50, bt_text_shop, (50, 50, 100), callback=shopp)
#btg_1 = Button(20, 50, 50, 50, bt_shop_frst, (50, 50, 100), callback=guns)
#btg_2 = Button(90, 50, 50, 50, bt_shop_scnd, (50, 50, 100), callback=guns)
#btg_3 = Button(160, 50, 50, 50, bt_shop_trd, (50, 50, 100), callback=guns)
#btg_4 = Button(230, 50, 50, 50, bt_shop_fr, (50, 50, 100), callback=guns)
back_button = Button(win_width/2, win_height - 50, 200, 50, back_text, (50, 50, 100), callback=menuu)
restart_bt = Button(win_width/2, win_height/2, 200, 50, bt_restart, (50, 50, 100), callback=start)
menu_bt = Button(win_width/2, win_height/2 + 50, 200, 50, bt_menu, (50, 50, 100), callback=menuu)
# Початкова генерація рівня
#random_lvl()
txt_rc = font_.render(f"поточний рекорд: {lvl_rec}", True, (50, 50, 100))

record = Database("record.json")
txt_grc = font_.render(f"рекорд: {record.get_record()}", True, (50, 50, 100))
# Головний цикл гри
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if finish:
        bts.update()
        bts.draw()
        bth.update()
        bth.draw()
    # if shop:
    #     win.blit(background_menu_image, (0, 0))
    #     btg_1.update()
    #     btg_1.draw()
    #     btg_2.update()
    #     btg_2.draw()
    #     btg_3.update()
    #     btg_3.draw()
    #     btg_4.update()
    #     btg_4.draw()
    #     back_button.update()
    #     back_button.draw()
    if die:
        restart_bt.update()
        restart_bt.draw()
        menu_bt.update()
        menu_bt.draw()
        win.blit(txt_rc, (win_width-500, 100))
        win.blit(txt_grc, (win_width-500, 150))
        win.blit(die_text, (win_width-500, 50))
    if game:
        win.fill(main_window)

        # Оновлюємо та малюємо гравця
        pl.update()
        pl.draw()

        # Оновлюємо та малюємо рівень
        lvl_grp.update()
        lvl_grp.draw(win)
        #pygame.draw.rect(win, (125, 125, 0), spikes.rect())

        # Перевірка на зіткнення гравця з рівнем
        for lv in lvl_grp:
            if lv.rect.colliderect(pl.rect):
                if lv.dead:
                    print("die")
                    die = True
                    game = False
                    break
            if lv.rect.collidepoint(pl.rect.bottomleft) or lv.rect.collidepoint(pl.rect.bottomright):
                pl.stop()
                pl.rect.bottom = lv.rect.y
            if lv.rect.collidepoint(pl.rect.topright) or lv.rect.collidepoint(pl.rect.topleft):
                pl.stop()
                pl.rect.top = lv.rect.bottom
            # if pl.rect.top == lv.rect.bottom:
            #     pl.stop()
            #     pl.rect.top = lv.rect.y + 100
                #pl.rect.bottom = lv.rect.bottom + 100
            #if lv.rect.colliderect(pl.rect.top):
                #print("die")
        bar = f"{lvl_rec}/{record.get_record()}"
        txt_bar = font_.render(bar, True, color)
        win.blit(txt_bar, (550, 10))

        # Якщо гравець досягає правого краю екрана, змінюємо рівень
        if pl.rect.centerx >= 800 - 50:
            random_lvl()
            lvl_rec += 1
            record.save_record(lvl_rec)
            pl.rect.centerx = 0  # Переміщуємо гравця на початок екрана
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        # Оновлення дисплея
    pygame.display.update()
    clock.tick(FPS)