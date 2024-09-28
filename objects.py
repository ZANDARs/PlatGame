from settings import *

class Game_Sprite_Test(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, image, width, height, color):
        super().__init__()

        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        #elf.start_image = self.image
        self.color = color
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, width//2, height//2)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.start_image, angle)
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

    def change_image(self, new_image):
        self.image = pygame.transform.scale(pygame.image.load(new_image).convert_alpha(), (self.width, self.height))
        self.start_image = self.image

    def draw(self):
        win.blit(self.image, self.rect)


class Player_Test(Game_Sprite_Test):
    def __init__(self, x, y, speed, image, width, height, color):
        super().__init__(x, y, speed, image, width, height, color)
        self.jump_height = 15
        self.gravity = 1
        self.velocity = 0
        self.is_jumping = False
        self.on_obstacle = False  # Новий атрибут для перевірки контакту з перешкодою

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity = -self.jump_height

    def apply_gravity(self):
        if not self.on_obstacle:  # Якщо не на перешкоді, застосовуй гравітацію
            self.velocity += self.gravity
            self.rect.centery += self.velocity

        # Перевірка на зіткнення з підлогою
        if self.rect.centery >= win_height - self.rect.height + 50:
            self.rect.centery = win_height - self.rect.height + 50
            self.is_jumping = False
            self.velocity = 0

    def stop(self):
        # Зупинка тільки якщо на перешкоді
        self.velocity = 0
        self.is_jumping = False
        self.on_obstacle = True  # Вказує, що персонаж на перешкоді

    def update(self):
        self.hitbox.center = self.rect.center
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.centerx -= self.speed
        if keys[pygame.K_d] and self.rect.x < win_width - self.rect.width:
            self.rect.centerx += self.speed
        if keys[pygame.K_w]:
            self.jump()
        if keys[pygame.K_g]:
            self.rect.centery -= self.speed

        self.apply_gravity()

        if keys[pygame.K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.centery += self.speed

        # Логіка для перевірки, чи об'єкт сходить з перешкоди
        if not self.check_collision_with_obstacle():
            self.on_obstacle = False  # Якщо немає зіткнення з перешкодою, гравітація діє

    def check_collision_with_obstacle(self):
        # Логіка для перевірки зіткнення з перешкодою
        # Повертає True, якщо є зіткнення, інакше False
        # Наприклад, перевірка може включати порівняння з позицією перешкоди
        pass

class Level(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.image = pygame.Surface((width, height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.center = x, y

    def draw(self):
        win.blit(self.image, self.rect)