#TYPE:FROZEN
import pygame

import entity
import interface
import minimap
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

hero = player.Player(400, 500)

#LOCATIONS---------------------------------------------------------
locations = []
#LEFT, RIGHT, UP, DOWN, ID, NAME, TEXTMAP
dev_loc1 = location.Location(1, -1, -1, -1, -2, "dev_loc1", "dev_loc1.txt")

spawn_forest = location.Location(-1, -1, 1, -1, 0, "spawn_forest", "spawn_forest.txt")  # ID 0
sandras_field_1 = location.Location(-1, 2, -1, 0, 1, "sandras_field_1",  "sandras_field_1.txt")  # ID 1
sandras_field_2 = location.Location(1, 3, -1, -1, 2, "sandras_field_2",  "sandras_field_2.txt")  # ID 2
sandras_field_3 = location.Location(2, -1, -1, -1, 3, "sandras_field_3",  "sandras_field_3.txt")  # ID 3

locations.append(spawn_forest)
locations.append(sandras_field_1)
locations.append(sandras_field_2)
locations.append(sandras_field_3)
#------------------------------------------------------------------
#ENTITIES MAP------------------------------------------------------
global_entities_map = []
spawn_forest_entities = []
global_entities_map.append(spawn_forest_entities)

sandras_field_1_enemies = []
sandras_field_1_enemies.append(entity.Entity(0, 150, 60, 350, 250, 1, hero))
sandras_field_1_enemies.append(entity.Entity(0, 450, 0, 800, 250, 1, hero))
global_entities_map.append(sandras_field_1_enemies)

sandras_field_2_enemies = []
sandras_field_2_enemies.append(entity.Entity(0, 150, 60, 800, 250, 2, hero))
sandras_field_2_enemies.append(entity.Entity(0, 150, 60, 800, 250, 2, hero))
sandras_field_2_enemies.append(entity.Entity(0, 150, 60, 800, 250, 2, hero))

sandras_field_2_enemies.append(entity.Entity(0, 0, 450, 800, 600, 2, hero))
sandras_field_2_enemies.append(entity.Entity(0, 0, 450, 800, 600, 2, hero))
sandras_field_2_enemies.append(entity.Entity(0, 0, 450, 800, 600, 2, hero))
global_entities_map.append(sandras_field_2_enemies)

sandras_field_3_enemies = []
sandras_field_3_enemies.append(entity.Entity(1, 0, 0, 800, 600, 3, hero))
sandras_field_3_enemies.append(entity.Entity(1, 0, 0, 800, 600, 3, hero))
sandras_field_3_enemies.append(entity.Entity(1, 0, 0, 800, 600, 3, hero))
global_entities_map.append(sandras_field_3_enemies)
#------------------------------------------------------------------


user_interface = interface.Interface()
user_minimap = minimap.Minimap()
is_minimap_drawing = False

font1 = pygame.font.Font(None, 15)

pygame.mouse.set_visible(False)

done = False

while not done:
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                done = True

            elif i.key == pygame.K_m:
                if not is_minimap_drawing:
                    is_minimap_drawing = True
                    pygame.mouse.set_visible(True)
                else:
                    is_minimap_drawing = False
                    pygame.mouse.set_visible(False)

            elif i.key == pygame.K_i:
                if user_interface.is_drawing:
                    user_interface.is_drawing = False
                else:
                    user_interface.is_drawing = True

    screen.fill(WHITE)

    locations[hero.location].draw(screen)

    hero.update(screen, GRAY, screen_width, screen_height, locations, global_entities_map)

    for i in global_entities_map:
        for j in i:
            j.update(screen, font1)

    user_interface.draw(screen, GRAY, hero.hp, hero.maxhp, hero.money, font1, locations[hero.location].location_matrix, hero.x, hero.y, global_entities_map[hero.location], hero.levels, hero.level, hero.exp, hero.dmg, hero.armor)

    if is_minimap_drawing:
        screen.fill(WHITE)
        user_minimap.draw(screen, 2, 2, hero.location, locations, locations[hero.location].location_matrix)

        for i in locations:
            i.is_on_map = False

    pygame.display.flip()
    clock.tick(60)
