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
        self.location = 0

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

    def update(self, sc, color, sc_w, sc_h, loc_arr):
        self.move()

        if self.x <= self.radius:  # left corner
            if loc_arr[self.location].l_n != -1:
                self.x = sc_w - self.radius - 1
                self.location = loc_arr[self.location].l_n
            else:
                self.x = self.radius

        if self.x >= sc_w - self.radius:  # right corner
            if loc_arr[self.location].r_n != -1:
                self.x = self.radius + 1
                self.location = loc_arr[self.location].r_n
            else:
                self.x = sc_w - self.radius

        if self.y <= self.radius:  # upper corner
            if loc_arr[self.location].u_n != -1:
                self.y = sc_h - self.radius - 1
                self.location = loc_arr[self.location].u_n
            else:
                self.y = self.radius

        if self.y >= sc_h - self.radius:  # bottom corner
            if loc_arr[self.location].d_n != -1:
                self.y = self.radius + 1
                self.location = loc_arr[self.location].d_n
            else:
                self.y = sc_h - self.radius

        self.draw(sc, color)
