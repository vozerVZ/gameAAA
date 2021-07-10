import pygame

undefined_tile = pygame.image.load("res/tiles/undefined.png")
dirt_tile = pygame.image.load("res/tiles/dirt.png")
grass_tile = pygame.image.load("res/tiles/grass.png")
rock_tile = pygame.image.load("res/tiles/rock.png")
wood_tile = pygame.image.load("res/tiles/wood.png")
water_tile = pygame.image.load("res/tiles/water.png")
tiles = [dirt_tile, grass_tile, rock_tile, wood_tile, water_tile]


class Location:
    def __init__(self, left_neighbour, right_neighbour, up_neighbour, down_neighbour, id_map, name):
        self.l_n = left_neighbour
        self.r_n = right_neighbour
        self.u_n = up_neighbour
        self.d_n = down_neighbour
        self.id = id_map
        self.name = name
        self.is_on_map = False

        self.location_matrix = []
        f = open("res/maps/" + self.name + ".txt", "r")
        for line in f:
            self.location_matrix.append(line.split())
        f.close()

        self.location_relief_matrix = []
        f = open("res/relief_maps/" + self.name + ".txt", "r")
        for line in f:
            self.location_relief_matrix.append(line.split())
        f.close()

    def draw(self, sc, font):
        for x in range(32):
            for y in range(24):
                if int(self.location_matrix[y][x]) < len(tiles):
                    sc.blit(tiles[int(self.location_matrix[y][x])], (x * 25, y * 25))

                    #pygame.draw.rect(sc, [0, 0, 0], (x * 25, y * 25, 25, 25), 1)
                    #hp_text = font.render(str(x) + "/" + str(y), 1, [255, 255, 255])
                    #sc.blit(hp_text, (x*25 + 2, y*25 + 2))
                else:
                    sc.blit(undefined_tile, (x * 25, y * 25))
