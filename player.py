import pygame


class Player:
    def __init__(self, x_pos, y_pos, health, exp, damage, speed):
        self.x = x_pos
        self.y = y_pos
        self.hp = health
        self.xp = exp
        self.dmg = damage
        self.spd = speed
        self.radius = 15

    def draw(self, sc, color):
        pygame.draw.circle(sc, color, (self.x, self.y), self.radius)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.spd
        if keys[pygame.K_a]:
            self.x -= self.spd
        if keys[pygame.K_s]:
            self.y += self.spd
        if keys[pygame.K_d]:
            self.x += self.spd

    def update(self, sc, color, sc_w, sc_h):
        self.move()

        if self.x <= self.radius:
            self.x = self.radius
        if self.x >= sc_w - self.radius:
            self.x = sc_w - self.radius

        if self.y <= self.radius:
            self.y = self.radius
        if self.y >= sc_h - self.radius:
            self.y = sc_h - self.radius

        self.draw(sc, color)
