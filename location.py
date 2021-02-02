import pygame
import random

undefined_tile = pygame.image.load("res/tiles/undefined.png")
dirt_tile = pygame.image.load("res/tiles/dirt.png")
grass_tile = pygame.image.load("res/tiles/grass.png")
rock_tile = pygame.image.load("res/tiles/rock.png")
tiles = [dirt_tile, grass_tile, rock_tile]


class Location:
    def __init__(self, left_neighbour, right_neighbour, up_neighbour, down_neighbour, id_map, name, location_map):
        self.l_n = left_neighbour
        self.r_n = right_neighbour
        self.u_n = up_neighbour
        self.d_n = down_neighbour
        self.id = id_map
        self.name = name
        self.location_matrix = []
        f = open("res/maps/" + location_map, "r")
        for line in f:
            self.location_matrix.append(line.split())
        f.close()


    def draw(self, sc):
        for x in range(32):
            for y in range(24):
                if int(self.location_matrix[y][x]) < len(tiles):
                    sc.blit(tiles[int(self.location_matrix[y][x])], (x * 25, y * 25))
                else:
                    sc.blit(undefined_tile, (x * 25, y * 25))
