import pygame
import random
#hp, dmg, spd, behavior, name, color, money_reward, exp_reward
entities_arr = [[1, 0, 1, "F", "butterfly", [255, 255, 0], 0, 0],
                [50, 5, 1, "P", "scarecrow", [135, 206, 250], 10, 1],
                [100, 10, 1, "A", "sheep", [255, 182, 193], 10, 10]]


class Entity:
    def __init__(self, id_e, xlc, ylc, xrc, yrc, loc, player_class):
        self.maxhp = entities_arr[id_e][0]
        self.hp = self.maxhp
        self.dmg = entities_arr[id_e][1]
        self.spd = entities_arr[id_e][2]
        self.type = entities_arr[id_e][3]  # Friendly(F), passive(P), aggressive(A)
        self.name = entities_arr[id_e][4]
        self.color = entities_arr[id_e][5]
        self.money_reward = entities_arr[id_e][6]
        self.exp_reward = entities_arr[id_e][7]

        self.radius = 15
        self.agr_radius = self.radius * 5
        self.location = loc
        self.player_class = player_class
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

        self.x = random.randint(self.x_left_corner + self.radius, self.x_right_corner - self.radius)
        self.y = random.randint(self.y_left_corner + self.radius, self.y_right_corner - self.radius)

    def setBehaviorAggressive(self):
        if self.type == "P" or self.type == "A":
            if self.status != "A":
                self.player_class.increase_decrease_attackers(1)
            self.status = "A"

    def drop_count(self):
        pass

    def dead_check(self):
        if self.hp <= 0:
            self.revive_timer = self.max_revive_timer
            self.drop_count()
            self.player_class.increase_decrease_attackers(-1)
            self.player_class.get_money(self.money_reward)
            self.player_class.get_exp(self.exp_reward)

    def get_damage(self, damage):
        self.hp -= damage

    def draw(self, sc, font):
        if self.location == self.player_class.location:
            pygame.draw.circle(sc, self.color, (self.x, self.y), self.radius)
            pygame.draw.line(sc, [255, 0, 0], [self.x - self.radius, self.y - self.radius * 1.5], [self.x + (self.radius * 2 / self.maxhp * self.hp) - self.radius, self.y - self.radius * 1.5], 3)
            name_text = font.render(self.name, 1, [255, 255, 255])
            sc.blit(name_text, (self.x - self.radius * 1.5, self.y - self.radius * 2.5))

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

    def update(self, sc, font):
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
        if self.type == "A" and abs(self.player_class.x - self.x) < self.agr_radius and abs(self.player_class.y - self.y) < self.agr_radius and self.player_class.location == self.location:
            if self.status != "A":
                self.player_class.increase_decrease_attackers(1)
            self.status = "A"

        if self.player_class.revive_timer > 0 and self.status == "A":
            self.status = "W"
            self.player_class.increase_decrease_attackers(-1)
            self.hp = self.maxhp

        if self.location != self.player_class.location and self.status == "A" and self.revive_timer == 0:
            self.status = "W"
            self.player_class.increase_decrease_attackers(-1)
            self.hp = self.maxhp

        if self.revive_timer == 0:
            self.move()
            self.draw(sc, font)
