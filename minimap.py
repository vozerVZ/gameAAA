import pygame

tile_w = 5
tile_h = 5

undefined_tile_S = pygame.transform.scale(pygame.image.load("res/tiles/undefined.png"), (tile_w, tile_h))
dirt_tile_S = pygame.transform.scale(pygame.image.load("res/tiles/dirt.png"), (tile_w, tile_h))
grass_tile_S = pygame.transform.scale(pygame.image.load("res/tiles/grass.png"), (tile_w, tile_h))
rock_tile_S = pygame.transform.scale(pygame.image.load("res/tiles/rock.png"), (tile_w, tile_h))
wood_tile_S = pygame.transform.scale(pygame.image.load("res/tiles/wood.png"), (tile_w, tile_h))
water_tile_S = pygame.transform.scale(pygame.image.load("res/tiles/water.png"), (tile_w, tile_h))
tiles = [dirt_tile_S, grass_tile_S, rock_tile_S, wood_tile_S, water_tile_S]


class Minimap:
    def __init__(self):
        pass

    def draw(self, sc, x, y, id_loc, global_loc_map, loc_map, font, player_location):
        if not global_loc_map[id_loc].is_on_map:
            global_loc_map[id_loc].is_on_map = True

            for xx in range(32):
                for yy in range(24):
                    if int(loc_map[yy][xx]) < len(tiles):
                        sc.blit(tiles[int(loc_map[yy][xx])], (32 * tile_w * x + xx * tile_w, 24 * tile_h * y + yy * tile_h))
                    else:
                        sc.blit(undefined_tile_S, (32 * tile_w * x + xx * tile_w, 24 * tile_h * y + yy * tile_h))

            pygame.draw.rect(sc, [0, 0, 0], (32 * tile_w * x, 24 * tile_h * y, 32 * tile_w, 24 * tile_h), 1)

            loc_name_text = font.render(global_loc_map[id_loc].name, 1, [0, 0, 0])
            sc.blit(loc_name_text, (32 * tile_w * x + 5, 24 * tile_h * y + 2))

            if player_location == id_loc:
                pygame.draw.circle(sc, [255, 0, 0], (32 * tile_w * x + 80, 24 * tile_h * y + 60), 15)

            if global_loc_map[id_loc].l_n != -1:
                self.draw(sc, x - 1, y, global_loc_map[id_loc].l_n, global_loc_map, global_loc_map[global_loc_map[id_loc].l_n].location_matrix, font, player_location)
            if global_loc_map[id_loc].r_n != -1:
                self.draw(sc, x + 1, y, global_loc_map[id_loc].r_n, global_loc_map, global_loc_map[global_loc_map[id_loc].r_n].location_matrix, font, player_location)
            if global_loc_map[id_loc].u_n != -1:
                self.draw(sc, x, y - 1, global_loc_map[id_loc].u_n, global_loc_map, global_loc_map[global_loc_map[id_loc].u_n].location_matrix, font, player_location)
            if global_loc_map[id_loc].d_n != -1:
                self.draw(sc, x, y + 1, global_loc_map[id_loc].d_n, global_loc_map, global_loc_map[global_loc_map[id_loc].d_n].location_matrix, font, player_location)
