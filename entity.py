import pygame
import random


class Entity:
    def __init__(self, health, damage, speed, xlc, ylc, xrc, yrc, loc, beh_type, player_class):
        self.radius = 15
        self.x = xlc + self.radius
        self.y = ylc + self.radius
        self.hp = health
        self.maxhp = health
        self.dmg = damage
        self.spd = speed
        self.location = loc
        self.player_class = player_class
        self.type = beh_type  # Friendly(F), passive(P), aggressive(A)
        self.status = "W"  # Wandering(W), attacking(A)

        self.x_left_corner = xlc
        self.y_left_corner = ylc
        self.x_right_corner = xrc
        self.y_right_corner = yrc
        self.x_rand_coord = random.randint(self.x_left_corner + self.radius, self.x_right_corner - self.radius)
        self.y_rand_coord = random.randint(self.y_left_corner + self.radius, self.y_right_corner - self.radius)
        self.go_timer = 0
        self.max_go_timer = 300
        self.attack_timer = 0
        self.max_attack_timer = 100
        self.revive_timer = 0
        self.max_revive_timer = 2000

    def setBehaviorAggressive(self):
        if self.type == "P" or self.type == "A":
            self.status = "A"

    def drop_count(self):
        pass

    def dead_check(self):
        if self.hp <= 0:
            self.revive_timer = self.max_revive_timer
            self.drop_count()

    def get_damage(self, damage):
        self.hp -= damage

    def draw(self, sc, color):
        if self.location == self.player_class.location:
            pygame.draw.circle(sc, color, (self.x, self.y), self.radius)
            pygame.draw.line(sc, [255, 0, 0], [self.x - self.radius, self.y - self.radius * 1.5], [self.x + (self.radius * 2 / self.maxhp * self.hp) - self.radius, self.y - self.radius * 1.5], 3)

    def move(self):
        if self.status == "W":
            if self.go_timer == 0:
                if self.x > self.x_rand_coord:
                    self.x -= self.spd
                elif self.x < self.x_rand_coord:
                    self.x += self.spd

                if 2 > abs(self.x - self.x_rand_coord) > 0:
                    self.x = self.x_rand_coord

                if self.y > self.y_rand_coord:
                    self.y -= self.spd
                elif self.y < self.y_rand_coord:
                    self.y += self.spd

                if 2 > abs(self.y - self.y_rand_coord) > 0:
                    self.y = self.y_rand_coord

                if self.x == self.x_rand_coord and self.y == self.y_rand_coord:
                    self.go_timer = self.max_go_timer
        else:
            if self.x > self.player_class.x + self.player_class.radius + self.radius:
                self.x -= self.spd
            elif self.x < self.player_class.x - self.player_class.radius - self.radius:
                self.x += self.spd

            if self.y > self.player_class.y + self.player_class.radius + self.radius:
                self.y -= self.spd
            elif self.y < self.player_class.y - self.player_class.radius - self.radius:
                self.y += self.spd

            if abs(self.x - self.player_class.x) < (self.player_class.radius + self.radius * 1.5) and abs(self.y - self.player_class.y) < (self.player_class.radius + self.radius * 1.5):
                if self.attack_timer == 0:
                    self.player_class.get_damage(self.dmg)
                    self.attack_timer = self.max_attack_timer

    def update(self, sc, color):
        #timers
        if self.go_timer == 1:
            self.go_timer = 0
            self.x_rand_coord = random.randint(self.x_left_corner + self.radius, self.x_right_corner - self.radius)
            self.y_rand_coord = random.randint(self.y_left_corner + self.radius, self.y_right_corner - self.radius)
        elif self.go_timer > 1:
            self.go_timer -= 1

        if self.attack_timer > 0:
            self.attack_timer -= 1

        if self.revive_timer == 1:
            self.revive_timer = 0
            self.hp = self.maxhp
            self.x_rand_coord = random.randint(self.x_left_corner + self.radius, self.x_right_corner - self.radius)
            self.y_rand_coord = random.randint(self.y_left_corner + self.radius, self.y_right_corner - self.radius)
            self.go_timer = self.max_go_timer
            self.status = "W"
        elif self.revive_timer > 1:
            self.revive_timer -= 1

        #------
        if self.player_class.revive_timer > 0 and self.status == "A":
            self.status = "W"

        if self.location != self.player_class.location and self.status == "A":
            self.status = "W"

        if self.revive_timer == 0:
            self.move()
            self.draw(sc, color)
