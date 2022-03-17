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

minimap_x_coord = 2
minimap_y_coord = 2
#LOCATIONS---------------------------------------------------------
locations = []
#LEFT, RIGHT, UP, DOWN, ID, NAME, TEXTMAP
dev_loc1 = location.Location(-1, -1, -1, -1, 0, "dev_loc1")
locations.append(dev_loc1)

sandras_field_1 = location.Location(4, -1, 2, -1, 1, "sandras_field_1")  # ID 1
locations.append(sandras_field_1)

sandras_field_2 = location.Location(3, -1, -1, 1, 2, "sandras_field_2")  # ID 2
locations.append(sandras_field_2)

sandras_field_3 = location.Location(-1, 2, 5, 4, 3, "sandras_field_3")  # ID 3
locations.append(sandras_field_3)

sandras_field_4 = location.Location(-1, 1, 3, -1, 4, "sandras_field_4")  # ID 4
locations.append(sandras_field_4)

newbie_bridge_1 = location.Location(-1, -1, 6, 3, 5, "newbie_bridge_1")  # ID 5
locations.append(newbie_bridge_1)

newbie_bridge_2 = location.Location(-1, -1, 10, 5, 6, "newbie_bridge_2")  # ID 6
locations.append(newbie_bridge_2)

church = location.Location(10, -1, 8, -1, 7, "church")  # ID 7
locations.append(church)

village_houses = location.Location(9, -1, -1, 7, 8, "village_houses")  # ID 8
locations.append(village_houses)

townhall = location.Location(12, 8, -1, 10, 9, "townhall")  # ID 9
locations.append(townhall)

village_1 = location.Location(11, 7, 9, 6, 10, "village_1")  # ID 10
locations.append(village_1)

village_2 = location.Location(14, 10, 12, -1, 11, "village_2")  # ID 11
locations.append(village_2)

market = location.Location(13, 9, 15, 11, 12, "market")  # ID 12
locations.append(market)

garden_1 = location.Location(-1, 12, 18, 14, 13, "garden_1")  # ID 13
locations.append(garden_1)

garden_2 = location.Location(19, 11, 13, -1, 14, "garden_2")  # ID 14
locations.append(garden_2)

meadow_1 = location.Location(18, -1, 16, 12, 15, "meadow")
locations.append(meadow_1)

meadow_2 = location.Location(17, -1, -1, 15, 16, "meadow")
locations.append(meadow_2)

meadow_3 = location.Location(22, 16, -1, 18, 17, "meadow")
locations.append(meadow_3)

meadow_4 = location.Location(21, 15, 17, 13, 18, "meadow")
locations.append(meadow_4)

meadow_5 = location.Location(26, 14, 20, -1, 19, "meadow")
locations.append(meadow_5)

meadow_6 = location.Location(25, 13, 21, 19, 20, "meadow")
locations.append(meadow_6)

meadow_7 = location.Location(24, 18, 22, 20, 21, "meadow")
locations.append(meadow_7)

meadow_8 = location.Location(23, 17, -1, 21, 22, "meadow")
locations.append(meadow_8)

meadow_9 = location.Location(30, 22, -1, 24, 23, "meadow")
locations.append(meadow_9)

meadow_10 = location.Location(29, 21, 23, 25, 24, "meadow")
locations.append(meadow_10)

meadow_11 = location.Location(28, 20, 24, 26, 25, "meadow")
locations.append(meadow_11)

meadow_12 = location.Location(27, 19, 25, -1, 26, "meadow")
locations.append(meadow_12)

meadow_13 = location.Location(34, 26, 28, -1, 27, "meadow")
locations.append(meadow_13)

meadow_14 = location.Location(33, 25, 29, 27, 28, "meadow")
locations.append(meadow_14)

meadow_15 = location.Location(32, 24, 30, 28, 29, "meadow")
locations.append(meadow_15)

meadow_16 = location.Location(31, 23, -1, 29, 30, "meadow")
locations.append(meadow_16)

meadow_17 = location.Location(38, 30, -1, 32, 31, "meadow")
locations.append(meadow_17)

meadow_18 = location.Location(37, 29, 31, 33, 32, "meadow")
locations.append(meadow_18)

meadow_19 = location.Location(36, 28, 32, 34, 33, "meadow")
locations.append(meadow_19)

meadow_20 = location.Location(35, 27, 33, -1, 34, "meadow")
locations.append(meadow_20)

meadow_21 = location.Location(42, 34, 36, -1, 35, "meadow")
locations.append(meadow_21)

meadow_22 = location.Location(41, 33, 37, 35, 36, "meadow")
locations.append(meadow_22)

meadow_23 = location.Location(40, 32, 38, 36, 37, "meadow")
locations.append(meadow_23)

meadow_24 = location.Location(39, 31, -1, 37, 38, "meadow")
locations.append(meadow_24)

meadow_25 = location.Location(-1, 38, -1, 40, 39, "meadow")
locations.append(meadow_25)

meadow_26 = location.Location(-1, 37, 39, 41, 40, "meadow")
locations.append(meadow_26)

meadow_27 = location.Location(-1, 36, 40, 42, 41, "meadow")
locations.append(meadow_27)

meadow_28 = location.Location(-1, 35, 41, -1, 42, "meadow")
locations.append(meadow_28)
#LEFT, RIGHT, UP, DOWN, ID, NAME, TEXTMAP
#------------------------------------------------------------------
#ENTITIES MAP------------------------------------------------------
global_entities_map = []

dev_loc_enemies = []
global_entities_map.append(dev_loc_enemies)

sandras_field_1_enemies = []
sandras_field_1_enemies.append(entity.Entity(0, 0, 0, 800, 600, 1, hero))
sandras_field_1_enemies.append(entity.Entity(0, 0, 0, 800, 600, 1, hero))
sandras_field_1_enemies.append(entity.Entity(0, 0, 0, 800, 600, 1, hero))
global_entities_map.append(sandras_field_1_enemies)

sandras_field_2_enemies = []
sandras_field_2_enemies.append(entity.Entity(0, 0, 0, 800, 600, 2, hero))
sandras_field_2_enemies.append(entity.Entity(0, 0, 0, 800, 600, 2, hero))
sandras_field_2_enemies.append(entity.Entity(0, 0, 0, 800, 600, 2, hero))
global_entities_map.append(sandras_field_2_enemies)

sandras_field_3_enemies = []
sandras_field_3_enemies.append(entity.Entity(0, 0, 0, 800, 600, 3, hero))
sandras_field_3_enemies.append(entity.Entity(0, 0, 0, 800, 600, 3, hero))
sandras_field_3_enemies.append(entity.Entity(0, 0, 0, 800, 600, 3, hero))
global_entities_map.append(sandras_field_3_enemies)

sandras_field_4_enemies = []
sandras_field_4_enemies.append(entity.Entity(0, 0, 0, 800, 600, 4, hero))
sandras_field_4_enemies.append(entity.Entity(0, 0, 0, 800, 600, 4, hero))
sandras_field_4_enemies.append(entity.Entity(0, 0, 0, 800, 600, 4, hero))
global_entities_map.append(sandras_field_4_enemies)

newbie_bridge_1_enemies = []
global_entities_map.append(newbie_bridge_1_enemies)

newbie_bridge_2_enemies = []
global_entities_map.append(newbie_bridge_2_enemies)

church_enemies = []
global_entities_map.append(church_enemies)

village_houses_enemies = []
global_entities_map.append(village_houses_enemies)

townhall_enemies = []
global_entities_map.append(townhall_enemies)

village_1_enemies = []
global_entities_map.append(village_1_enemies)

village_2_enemies = []
global_entities_map.append(village_2_enemies)

market_enemies = []
global_entities_map.append(market_enemies)

garden_1_enemies = []
garden_1_enemies.append(entity.Entity(1, 0, 0, 400, 300, 13, hero))
garden_1_enemies.append(entity.Entity(1, 400, 300, 800, 600, 13, hero))
garden_1_enemies.append(entity.Entity(1, 0, 0, 800, 600, 13, hero))
global_entities_map.append(garden_1_enemies)

garden_2_enemies = []
garden_2_enemies.append(entity.Entity(1, 0, 0, 400, 300, 14, hero))
garden_2_enemies.append(entity.Entity(1, 400, 300, 800, 600, 14, hero))
garden_2_enemies.append(entity.Entity(1, 0, 0, 800, 600, 14, hero))
global_entities_map.append(garden_2_enemies)

meadow_1_enemies = []
global_entities_map.append(meadow_1_enemies)

meadow_2_enemies = []
global_entities_map.append(meadow_2_enemies)

meadow_3_enemies = []
global_entities_map.append(meadow_3_enemies)

meadow_4_enemies = []
global_entities_map.append(meadow_4_enemies)

meadow_5_enemies = []
global_entities_map.append(meadow_5_enemies)

meadow_6_enemies = []
global_entities_map.append(meadow_6_enemies)

meadow_7_enemies = []
global_entities_map.append(meadow_7_enemies)

meadow_8_enemies = []
global_entities_map.append(meadow_8_enemies)

meadow_9_enemies = []
global_entities_map.append(meadow_9_enemies)

meadow_10_enemies = []
global_entities_map.append(meadow_10_enemies)

meadow_11_enemies = []
global_entities_map.append(meadow_11_enemies)

meadow_12_enemies = []
global_entities_map.append(meadow_12_enemies)

meadow_13_enemies = []
global_entities_map.append(meadow_13_enemies)

meadow_14_enemies = []
global_entities_map.append(meadow_14_enemies)

meadow_15_enemies = []
global_entities_map.append(meadow_15_enemies)

meadow_16_enemies = []
global_entities_map.append(meadow_16_enemies)

meadow_17_enemies = []
global_entities_map.append(meadow_17_enemies)

meadow_18_enemies = []
global_entities_map.append(meadow_18_enemies)

meadow_19_enemies = []
global_entities_map.append(meadow_19_enemies)

meadow_20_enemies = []
global_entities_map.append(meadow_20_enemies)

meadow_21_enemies = []
global_entities_map.append(meadow_21_enemies)

meadow_22_enemies = []
global_entities_map.append(meadow_22_enemies)

meadow_23_enemies = []
global_entities_map.append(meadow_23_enemies)

meadow_24_enemies = []
global_entities_map.append(meadow_24_enemies)

meadow_25_enemies = []
global_entities_map.append(meadow_25_enemies)

meadow_26_enemies = []
global_entities_map.append(meadow_26_enemies)

meadow_27_enemies = []
global_entities_map.append(meadow_27_enemies)

meadow_28_enemies = []
global_entities_map.append(meadow_28_enemies)
#------------------------------------------------------------------


user_interface = interface.Interface()
user_minimap = minimap.Minimap()
is_minimap_drawing = False

font1 = pygame.font.Font(None, 15)
font2 = pygame.font.Font(None, 12)

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
                    minimap_x_coord = 2
                    minimap_y_coord = 2
                else:
                    is_minimap_drawing = False
                    pygame.mouse.set_visible(False)

            elif i.key == pygame.K_i:
                if user_interface.is_drawing:
                    user_interface.is_drawing = False
                else:
                    user_interface.is_drawing = True

            elif i.key == pygame.K_LEFT and is_minimap_drawing:
                minimap_x_coord += 1

            elif i.key == pygame.K_RIGHT and is_minimap_drawing:
                minimap_x_coord -= 1

            elif i.key == pygame.K_UP and is_minimap_drawing:
                minimap_y_coord += 1

            elif i.key == pygame.K_DOWN and is_minimap_drawing:
                minimap_y_coord -= 1

    screen.fill(WHITE)

    locations[hero.location].draw(screen, font2)

    hero.update(screen, GRAY, screen_width, screen_height, locations, global_entities_map)

    for i in global_entities_map:
        for j in i:
            j.update(screen, font1)

    user_interface.draw(screen, GRAY, hero.hp, hero.maxhp, hero.money, font1, locations[hero.location].location_matrix, hero.x, hero.y, global_entities_map[hero.location], hero.levels, hero.level, hero.exp, hero.dmg, hero.armor)

    if is_minimap_drawing:
        screen.fill(WHITE)
        user_minimap.draw(screen, minimap_x_coord, minimap_y_coord, hero.location, locations, locations[hero.location].location_matrix, font1, hero.location)

        for i in locations:
            i.is_on_map = False

    pygame.display.flip()
    clock.tick(60)
