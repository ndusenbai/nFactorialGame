import pygame
import random
import sys
import time


class Player(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename).convert_alpha(), (70, 50))
        self.rect = self.image.get_rect(center=(240, 230))

    def update(self, x, y):
        if self.rect.y < HEIGHT:
            self.rect.y = y
            self.rect.x = x


class Egg(pygame.sprite.Sprite):
    def __init__(self, x, y, surf, group, speed):
        super().__init__()
        # ROTATING CARS, SO WE HAVE 2 DIRECTIONS OF OTHER CAR MOTIONS
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)
        self.speede = speed

    def update(self):
        if self.rect.y < HEIGHT - 50:
            self.rect.y += self.speede
        else:
            self.kill()


# Not work
class Bomb(pygame.sprite.Sprite):
    pass


# Not work
class Top:
    pass


class Write_text:
    def __init__(self, font, text):
        self.font = font
        self.text = text

    def score_text(self, x, y):
        # text surface object
        textRect = self.text.get_rect()

        # set the center of the rectangular object.
        textRect.center = (x, y)
        return textRect

    def leval_text(self, x, y):
        textRect = self.text.get_rect()

        # set the center of the rectangular object.
        textRect.center = (x, y)
        return textRect


class Bottom_kill(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(img).convert_alpha(), (800, 50))
        self.rect = self.image.get_rect(center=(400, 550))

    def update(self, x, y):
        pass



if __name__ == '__main__':
    # Main parameters
    FPS = 60
    SCORE = 0
    game = True
    SPEED = 10
    WIDTH = 800
    HEIGHT = 600
    STARTING_POINTS_LIST_VERTICAL_EGG = [240, 550]
    STARTING_POINTS_LIST_HORIZONTAL_EGG = [100, 300]
    STARTING_POINTS_LIST_VERTICAL = [190, 500]
    STARTING_POINTS_LIST_HORIZONTAL = [180, 450]
    point_x = 190
    point_y = 180
    LEVAL = [5, 10]
    INTERVAL = 1000

    pygame.init()
    pygame.time.set_timer(pygame.USEREVENT, INTERVAL)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    EGGS = ['./img/egg/egg.png']
    EGGS_SURF = []

    for i in range(len(EGGS)):
        EGGS_SURF.append(pygame.transform.scale(pygame.image.load(EGGS[i]).convert_alpha(), (50, 50)))

    # img load in pygame
    bird_1 = pygame.image.load('img/birds/bird_1.png')
    bird_2 = pygame.image.load('img/birds/bird_2.png')
    bird_3 = pygame.image.load('img/birds/bird_3.png')
    bird_4 = pygame.image.load('img/birds/bird_4.png')

    # Group
    eggs = pygame.sprite.Group()

    # Obj. class
    obj_player = Player('img/basket.png')

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.USEREVENT:
                Egg(random.choice(STARTING_POINTS_LIST_VERTICAL_EGG), random.choice(STARTING_POINTS_LIST_HORIZONTAL_EGG), EGGS_SURF[0], eggs, SPEED)

            # MAKING A PLAYER'S CAR MOVE TO OTHER ROAD LINE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if point_x != STARTING_POINTS_LIST_VERTICAL[0]:
                        point_x = STARTING_POINTS_LIST_VERTICAL[0]
                        obj_player.update(point_x, point_y)
                elif event.key == pygame.K_RIGHT:
                    if point_x != STARTING_POINTS_LIST_VERTICAL[1]:
                        point_x = STARTING_POINTS_LIST_VERTICAL[1]
                        obj_player.update(point_x, point_y)
                elif event.key == pygame.K_UP:
                    if point_y != STARTING_POINTS_LIST_HORIZONTAL[0]:
                        point_y = STARTING_POINTS_LIST_HORIZONTAL[0]
                        obj_player.update(point_x, point_y)
                elif event.key == pygame.K_DOWN:
                    if point_y != STARTING_POINTS_LIST_HORIZONTAL[1]:
                        point_y = STARTING_POINTS_LIST_HORIZONTAL[1]
                        obj_player.update(point_x, point_y)

        screen.fill((255, 255, 255))

        #backgrount image
        background = pygame.transform.scale(pygame.image.load('./img/lavel/lavel_1.png'), (800, 600))
        screen.blit(background, (0, 0))
        eggs.draw(screen)

        # text font
        font = pygame.font.Font('./fonts/Blessed.ttf', 32)
        # text score
        text = font.render(f'Score: {SCORE}', True, (34, 139, 34), (25, 25, 112))
        obj_text_score = Write_text(font, text)
        screen.blit(text, obj_text_score.score_text(80, 50))

        #text leval
        if SCORE <= LEVAL[0]:
            text = font.render(f'Leval: 1', True, (34, 139, 34), (25, 25, 112))
        elif LEVAL[0] < SCORE <= LEVAL[1]:
            text = font.render(f'Leval: 2', True, (34, 139, 34), (25, 25, 112))
        else:
            text = font.render(f'Leval: 3', True, (34, 139, 34), (25, 25, 112))
        obj_text_score = Write_text(font, text)
        screen.blit(text, obj_text_score.leval_text(600, 50))

        #black rect. in bottom
        hero = pygame.Surface((800, 50))
        hero.fill((0, 0, 0))
        rect = hero.get_rect()
        screen.blit(hero, (0, 550))

        #build player image
        screen.blit(obj_player.image, obj_player.rect)

        #egg score, sceed
        hit_player = pygame.sprite.spritecollide(obj_player, eggs, True)
        if hit_player:
            SCORE += 1

            if SCORE <= LEVAL[0]:
                SPEED = 6
            elif LEVAL[0] < SCORE <= LEVAL[1]:
                SPEED = 8
            else:
                SPEED = 13

        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)
        eggs.update()