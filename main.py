import pygame
import random
import sys
import time

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((835, 600))
    clock = pygame.time.Clock()
    FPS = 60
    SCORE = 0
    game = True

    #img load in pygame
    bird_1 = pygame.image.load('img/birds/bird_1.png')

    lavel_1 = pygame.transform.scale(pygame.image.load('img/lavel/lavel_1.png'), (835, 600))
    lavel_2 = pygame.transform.scale(pygame.image.load('img/lavel/lavel_2.jpg'), (835, 600))
    lavel_3 = pygame.transform.scale(pygame.image.load('img/lavel/lavel_3.png'), (835, 600))

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # MAKING A PLAYER'S CAR MOVE TO OTHER ROAD LINE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    screen.blit(lavel_2, (0, 0))
                    pygame.display.update()
                    pygame.display.flip()

                    str += 1
                if event.key == pygame.K_RIGHT:
                    screen.blit(lavel_3, (0, 0))
                    pygame.display.update()
                    pygame.display.flip()

                    str -= 1

        if str == 1:
            screen.blit(lavel_1, (0, 0))

        clock.tick(FPS)
        pygame.display.update()
        pygame.display.flip()
