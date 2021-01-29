#TYPE:DEV
import pygame
import random
import player
import location

pygame.init()
clock = pygame.time.Clock()
screen_height = 600
screen_width = 800

size = [screen_width, screen_height]
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

pygame.display.set_caption("Dev")

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [32, 58, 39]
GRAY = [128, 128, 128]
RED = [255, 0, 0]
YELLOW = [247, 242, 26]
BLUE = [135, 206, 250]
colors_arr = [BLACK, WHITE, GREEN, GRAY, RED, YELLOW, BLUE]

hero = player.Player(50, 350, 100, 0, 10, 2)

dev_loc = location.Location(-1, -1, -1, -1, -1, "dev_loc", "dev_loc.txt")

pygame.mouse.set_visible(False)

done = False

while not done:
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                done = True

    screen.fill(WHITE)

    dev_loc.draw(screen, colors_arr)

    hero.update(screen, RED, screen_width, screen_height)

    pygame.display.flip()
    clock.tick(60)
