import pygame


class Interface:
    def __init__(self):
        pass

    def draw(self, sc, hp, maxhp, font):
        pygame.draw.rect(sc, [150, 75, 0], (0, 0, 150, 60))

        pygame.draw.line(sc, [255, 0, 0], [2, 10], [2 + (98 / maxhp * hp), 10], 4)
        hp_text = font.render(str(hp), 1, [255, 255, 255])
        sc.blit(hp_text, (105, 6))
