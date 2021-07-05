import pygame


class Player:
    def __init__(self, x_pos, y_pos, health, exp, damage, speed):
        self.x = x_pos
        self.y = y_pos
        self.hp = health
        self.maxhp = health
        self.xp = exp
        self.dmg = damage
        self.spd = speed
        self.radius = 15
        self.location = 0

        self.attack_timer = 0
        self.max_attack_timer = 100
        self.revive_timer = 0
        self.max_revive_timer = 2000

    def get_damage(self, damage):
        self.hp -= damage

        if self.hp <= 0:
            self.revive_timer = self.max_revive_timer

    def draw(self, sc, color):
        pygame.draw.circle(sc, color, (self.x, self.y), self.radius)

    def move(self, global_ent_map):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.spd
        if keys[pygame.K_a]:
            self.x -= self.spd
        if keys[pygame.K_s]:
            self.y += self.spd
        if keys[pygame.K_d]:
            self.x += self.spd

        if keys[pygame.K_RETURN]:
            if self.attack_timer == 0:
                for i in global_ent_map[self.location]:
                    if abs(self.x - i.x) <= (self.radius * 1.5 + i.radius) and abs(self.y - i.y) <= (self.radius * 1.5 + i.radius):
                        i.get_damage(self.dmg)
                        i.setBehaviorAggressive()
                        i.dead_check()

                        self.attack_timer = self.max_attack_timer

    def update(self, sc, color, sc_w, sc_h, loc_arr, global_ent_map):
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

        #timers
        if self.attack_timer > 0:
            self.attack_timer -= 1

        if self.revive_timer == 1:
            self.revive_timer = 0
            self.hp = self.maxhp
            self.location = 0
            self.x = 400
            self.y = 500
        elif self.revive_timer > 1:
            self.revive_timer -= 1
        #------

        if self.revive_timer == 0:
            self.move(global_ent_map)
            self.draw(sc, color)
