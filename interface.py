import pygame

tile_w = 5
tile_h = 5

undefined_tile_M = pygame.transform.scale(pygame.image.load("res/tiles/undefined.png"), (tile_w, tile_h))
dirt_tile_M = pygame.transform.scale(pygame.image.load("res/tiles/dirt.png"), (tile_w, tile_h))
grass_tile_M = pygame.transform.scale(pygame.image.load("res/tiles/grass.png"), (tile_w, tile_h))
rock_tile_M = pygame.transform.scale(pygame.image.load("res/tiles/rock.png"), (tile_w, tile_h))
wood_tile_M = pygame.transform.scale(pygame.image.load("res/tiles/wood.png"), (tile_w, tile_h))
water_tile_M = pygame.transform.scale(pygame.image.load("res/tiles/water.png"), (tile_w, tile_h))
tiles = [dirt_tile_M, grass_tile_M, rock_tile_M, wood_tile_M, water_tile_M]


class Interface:
    def __init__(self):
        self.is_drawing = True

    def draw(self, sc, color, hp, maxhp, money, font, loc_map, x_player, y_player, entities_map, lvl_arr, curr_level, player_exp, damage, armor):
        if self.is_drawing:
            pygame.draw.rect(sc, [162, 95, 42], (0, 0, 101, 70))  # left&up rect
            pygame.draw.rect(sc, [150, 75, 0], (0, 0, 800, 600), 15)  # screen frame

            pygame.draw.rect(sc, [162, 95, 42], (800 - 32 * tile_w - 14, 600 - 24 * tile_h - 14, 32 * tile_w + 6, 24 * tile_h + 6), 5)  # minimap rect

            for x in range(32):
                for y in range(24):
                    if int(loc_map[y][x]) < len(tiles):
                        sc.blit(tiles[int(loc_map[y][x])], (629 + x * tile_w, 469 + y * tile_h))
                    else:
                        sc.blit(undefined_tile_M, (1, 1))

            pygame.draw.circle(sc, color, (625 + x_player / 5, 465 + y_player / 5), 3)

            for i in entities_map:
                if i.revive_timer == 0:
                    pygame.draw.circle(sc, i.color, (625 + i.x / 5, 465 + i.y / 5), 3)

        pygame.draw.line(sc, [255, 0, 0], [9, 15], [2 + (98 / maxhp * hp), 15], 10)  # hp bar
        hp_text = font.render(str(round(hp)) + "/" + str(maxhp), 1, [255, 255, 255])
        sc.blit(hp_text, (10, 11))  # hp text

        pygame.draw.line(sc, [255, 255, 0], [9, 27], [9 + (80 / (lvl_arr[curr_level] - lvl_arr[curr_level - 1]) * (player_exp - lvl_arr[curr_level - 1])), 27], 5)
        hp_text = font.render(str(curr_level), 1, [255, 255, 255])
        sc.blit(hp_text, (90, 23))  # exp text

        money_text = font.render(str(damage) + " damage", 1, [0, 0, 0])
        sc.blit(money_text, (10, 32))  # damage text

        money_text = font.render(str(armor) + " armor", 1, [64, 58, 58])
        sc.blit(money_text, (10, 45))  # armor text

        money_text = font.render(str(money) + " coins", 1, [255, 255, 0])
        sc.blit(money_text, (10, 57))  # money text

        #money_text = font.render(str(x_player//25) + "/" + str(y_player//25), 1, [0, 0, 255])
        #sc.blit(money_text, (10, 80))
