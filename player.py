import pygame


class Player:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.maxhp = 100
        self.hp = self.maxhp
        self.exp = 0

        self.level = 1
        self.money = 0
        self.dmg = 10
        self.spd = 2
        self.regen_speed = 0.2
        self.armor = 0
        self.radius = 15
        self.location = 0
        self.isAttacked = False
        self.attackers_count = 0

        self.attack_timer = 0
        self.max_attack_timer = 100
        self.revive_timer = 0
        self.max_revive_timer = 2000

        self.levels = [0, 5, 15, 100, 300, 1000, 999999]
        self.level_reward = [[0, 0, 0], [3, 1, 15], [3, 1, 15], [3, 1, 15], [3, 1, 15], [3, 1, 15]]  # damage, armor, maxHP

    def get_damage(self, damage):
        self.hp -= damage

        if self.hp <= 0:
            self.revive_timer = self.max_revive_timer
            self.money = round(self.money * 0.8)

    def increase_decrease_attackers(self, plus_minus):
        self.attackers_count += plus_minus

    def get_money(self, money):
        self.money += money

    def get_exp(self, experience):
        self.exp += experience

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
                    if abs(self.x - i.x) <= (self.radius * 1.5 + i.radius) and abs(self.y - i.y) <= (self.radius * 1.5 + i.radius) and i.revive_timer == 0:
                        i.get_damage(self.dmg)
                        i.setBehaviorAggressive()
                        i.dead_check()

                        self.attack_timer = self.max_attack_timer
                        break

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
        if self.attackers_count == 0 and self.hp < self.maxhp and self.revive_timer == 0:
            self.hp += self.regen_speed
            if self.hp >= self.maxhp:
                self.hp = self.maxhp

        if self.revive_timer == 0:
            self.move(global_ent_map)
            self.draw(sc, color)

        if self.exp >= self.levels[self.level]:
            self.dmg += self.level_reward[self.level][0]
            self.armor += self.level_reward[self.level][1]
            self.maxhp += self.level_reward[self.level][2]
            self.level += 1
