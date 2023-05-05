import pygame
import random
import sys
import time
import json


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
        self.rect = self.image.get_rect(center=(400, 600))

    def update(self, x, y):
        pass


class Top_player:

    def open_json_file(self):
        with open('top_10.json', 'r') as file:
            json_data = json.load(file)
        return json_data

    def list_value_order(self, json_file, new_element):
        done_list = list(json_file.values())
        done_list.append(new_element)
        done_list.sort(reverse=True)
        return done_list

    def record(self, done_list):
        done_json = {}

        for value in range(10):
            done_json[value] = done_list[value]
        return done_json

    def my_index(self, json, element):
        done_list = list(json.values())
        try:
            ele_index = done_list.index(element)
        except:
            ele_index = None
        return ele_index

    def save_json(self, json_data):

        with open('top_10.json', 'w') as f:
            json.dump(json_data, f)


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
    STARTING_POINTS_LIST_VERTICAL = [205, 515]
    STARTING_POINTS_LIST_HORIZONTAL = [180, 450]
    point_x = 215
    point_y = 180
    LEVAL = [15, 30]
    INTERVAL = 1000

    # time
    START_TIME = time.time()

    pygame.init()
    pygame.time.set_timer(pygame.USEREVENT, INTERVAL)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    EGGS = ['./img/egg/egg.png']
    EGGS_SURF = []

    for i in range(len(EGGS)):
        EGGS_SURF.append(pygame.transform.scale(pygame.image.load(EGGS[i]).convert_alpha(), (50, 50)))

    # img load in pygame
    bird_1 = pygame.transform.scale(pygame.image.load('img/birds/bird_1.png'), (80, 80))
    bird_2 = pygame.transform.scale(pygame.image.load('img/birds/bird_2.png'), (80, 80))
    bird_3 = pygame.transform.scale(pygame.image.load('img/birds/bird_3.png'), (80, 80))
    bird_4 = pygame.transform.scale(pygame.image.load('img/birds/bird_4.png'), (80, 80))
    egg_birds_left_top = pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load("img/other/egg_birds.png"), (170, 20)), -20)
    egg_birds_left_bottom = pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load("img/other/egg_birds.png"), (170, 20)), -20)
    egg_birds_right_top = pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load("img/other/egg_birds.png"), (170, 20)), 20)
    egg_birds_right_bottom = pygame.transform.rotate(
        pygame.transform.scale(pygame.image.load("img/other/egg_birds.png"), (170, 20)), 20)
    wolf_x = 320
    wolf_y = 370
    wolf_left = pygame.transform.scale(pygame.image.load("img/wolf/woif_left.png"), (wolf_x, wolf_y))
    wolf_right = pygame.transform.scale(pygame.image.load("img/wolf/woif_right.png"), (wolf_x, wolf_y))
    wolf_left_bottom = pygame.transform.scale(pygame.image.load("img/wolf/woif_left_bottom.png"), (wolf_x, wolf_y))
    wolf_right_bottom = pygame.transform.scale(pygame.image.load("img/wolf/woif_ritgh_bottom.png"), (wolf_x, wolf_y))

    # Group
    eggs = pygame.sprite.Group()

    # Obj. class
    obj_player = Player('img/other/basket.png')
    obj_bottom_kill = Bottom_kill('img/other/bottom.png')
    obj_top_player = Top_player()

    wolf_left_top = True
    wolf_right_top = False
    wolf_left_bottom_bool = False
    wolf_right_bottom_bool = False

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.USEREVENT:
                Egg(random.choice(STARTING_POINTS_LIST_VERTICAL_EGG),
                    random.choice(STARTING_POINTS_LIST_HORIZONTAL_EGG), EGGS_SURF[0], eggs, SPEED)

            # MAKING A PLAYER'S CAR MOVE TO OTHER ROAD LINE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if point_x != STARTING_POINTS_LIST_VERTICAL[0]:
                        point_x = STARTING_POINTS_LIST_VERTICAL[0]
                        obj_player.update(point_x, point_y)

                    if wolf_right_top:
                        wolf_left_top = True
                        wolf_left_bottom_bool = False
                        wolf_right_top = False
                        wolf_right_bottom_bool = False
                    elif wolf_right_bottom:
                        wolf_left_top = False
                        wolf_left_bottom_bool = True
                        wolf_right_top = False
                        wolf_right_bottom_bool = False

                elif event.key == pygame.K_RIGHT:
                    if point_x != STARTING_POINTS_LIST_VERTICAL[1]:
                        point_x = STARTING_POINTS_LIST_VERTICAL[1]
                        obj_player.update(point_x, point_y)

                    if wolf_left_top:
                        wolf_left_top = False
                        wolf_left_bottom_bool = False
                        wolf_right_top = True
                        wolf_right_bottom_bool = False
                    elif wolf_left_bottom_bool:
                        wolf_left_top = False
                        wolf_left_bottom_bool = False
                        wolf_right_top = False
                        wolf_right_bottom_bool = True

                elif event.key == pygame.K_UP:
                    if point_y != STARTING_POINTS_LIST_HORIZONTAL[0]:
                        point_y = STARTING_POINTS_LIST_HORIZONTAL[0]
                        obj_player.update(point_x, point_y)

                    if wolf_left_bottom_bool:
                        wolf_left_top = True
                        wolf_left_bottom_bool = False
                        wolf_right_top = False
                        wolf_right_bottom_bool = False
                    elif wolf_right_bottom:
                        wolf_left_top = False
                        wolf_left_bottom_bool = False
                        wolf_right_top = True
                        wolf_right_bottom_bool = False

                elif event.key == pygame.K_DOWN:
                    if point_y != STARTING_POINTS_LIST_HORIZONTAL[1]:
                        point_y = STARTING_POINTS_LIST_HORIZONTAL[1]
                        obj_player.update(point_x, point_y)

                    if wolf_left_top:
                        wolf_left_top = False
                        wolf_left_bottom_bool = True
                        wolf_right_top = False
                        wolf_right_bottom_bool = False
                    elif wolf_right_top:
                        wolf_left_top = False
                        wolf_left_bottom_bool = False
                        wolf_right_top = False
                        wolf_right_bottom_bool = True

        screen.fill((255, 255, 255))

        # backgrount image
        background = pygame.transform.scale(pygame.image.load('./img/lavel/lavel_1.png'), (800, 600))
        screen.blit(background, (0, 0))
        eggs.draw(screen)

        # text font
        font = pygame.font.Font('./fonts/Blessed.ttf', 32)
        # text score
        text = font.render(f'Score: {SCORE}', True, (34, 139, 34), (25, 25, 112))
        obj_text_score = Write_text(font, text)
        screen.blit(text, obj_text_score.score_text(250, 50))

        # text leval
        if SCORE <= LEVAL[0]:
            text = font.render(f'Leval: 1', True, (34, 139, 34), (25, 25, 112))
        elif LEVAL[0] < SCORE <= LEVAL[1]:
            text = font.render(f'Leval: 2', True, (34, 139, 34), (25, 25, 112))
        else:
            text = font.render(f'Leval: 3', True, (34, 139, 34), (25, 25, 112))
        obj_text_score = Write_text(font, text)
        screen.blit(text, obj_text_score.leval_text(600, 50))

        # build player image
        screen.blit(obj_player.image, obj_player.rect)
        screen.blit(obj_bottom_kill.image, obj_bottom_kill.rect)

        # build birds images
        screen.blit(bird_1, (50, 50))
        screen.blit(bird_2, (650, 50))
        screen.blit(bird_3, (50, 250))
        screen.blit(bird_4, (650, 250))
        screen.blit(egg_birds_left_top, (50, 120))
        screen.blit(egg_birds_left_bottom, (50, 320))
        screen.blit(egg_birds_right_top, (580, 120))
        screen.blit(egg_birds_right_top, (580, 320))

        wolf_img_x = 280
        wolf_img_y = 150
        if wolf_right_top == True and wolf_right_bottom_bool == False:
            screen.blit(wolf_right, (290, 80))
        elif wolf_left_top == True and wolf_left_bottom_bool == False:
            screen.blit(wolf_left, (190, 80))
        elif wolf_right_bottom_bool and wolf_right_top == False:
            screen.blit(wolf_right_bottom, (320, 240))
        elif wolf_left_bottom_bool and wolf_left_top == False:
            screen.blit(wolf_left_bottom, (150, 240))

        # kill
        hit_player = pygame.sprite.spritecollide(obj_bottom_kill, eggs, True)
        if hit_player:
            END_TIME = time.time()
            different_time = END_TIME - START_TIME

            file = obj_top_player.open_json_file()
            order_list = obj_top_player.list_value_order(file, different_time)
            done_json = obj_top_player.record(order_list)
            my_index = obj_top_player.my_index(done_json, different_time)
            obj_top_player.save_json(done_json)

            screen.blit(background, (0, 0))

            y_position = 50
            incrementation = 0
            for x, y in done_json.items():
                if incrementation == my_index:
                    text = font.render(f'{x}: {y}', True, (255, 0, 255), (25, 25, 112))
                    obj_text_score = Write_text(font, text)
                    screen.blit(text, obj_text_score.score_text(400, y_position))
                    y_position += 50
                else:
                    text = font.render(f'{x}: {y}', True, (70, 130, 180), (25, 25, 112))
                    obj_text_score = Write_text(font, text)
                    screen.blit(text, obj_text_score.score_text(400, y_position))
                    y_position += 50

                incrementation += 1

            pygame.display.update()

            # time.sleep(10)
            # game = False

        # egg score, sceed
        hit_player = pygame.sprite.spritecollide(obj_player, eggs, True)
        if hit_player:
            SCORE += 1

            if SCORE % 10 == 0:
                SPEED += 4

        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)
        eggs.update()
