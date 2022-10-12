import pygame, sys
from pygame.locals import *
import random, time
from PlayerAndEnemy import Player, Enemy

pygame.init()


FPS = 60
FramePerSec = pygame.time.Clock()


BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


if __name__ == "__main__":
    P1 = Player()
    E1 = Enemy()
    E2 = Enemy()


    enemies = pygame.sprite.Group()
    enemies.add(E1, E2)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(E1)


    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)
    E2.speed = 3.5

    while True:
        enemies.add(E1)
        all_sprites.add(E1)
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                E1.speed += 0.5
                E2.speed += 0.5
                if E1.score > 3:
                    enemies.add(E2)
                    all_sprites.add(E2)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAYSURF.blit(background, (0, 0))
        scores = font_small.render(str(E1.score), True, BLACK)
        DISPLAYSURF.blit(scores, (10, 10))

        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound('crash.wav').play()
            time.sleep(0.5)

            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30, 250))

            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        FramePerSec.tick(FPS)