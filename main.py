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

hero = player.Player(400, 500, 100, 0, 10, 2)

locations = []

dev_loc1 = location.Location(1, -1, -1, -1, -2, "dev_loc1", "dev_loc1.txt")

spawn_forest = location.Location(-1, -1, 1, -1, 0, "spawn_forest", "spawn_forest.txt")
sandras_field_1 = location.Location(-1, -1, -1, 0, 1, "sandras_field_1",  "sandras_field_1.txt")

locations.append(spawn_forest)
locations.append(sandras_field_1)

pygame.mouse.set_visible(False)

done = False

while not done:
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                done = True

    screen.fill(WHITE)

    locations[hero.location].draw(screen)

    hero.update(screen, RED, screen_width, screen_height, locations)

    pygame.display.flip()
    clock.tick(60)
