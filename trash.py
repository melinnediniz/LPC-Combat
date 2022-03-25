keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.green_tank.move_up(self.green_tank_angle)
        if keys[pygame.K_a]:
            self.green_tank.move_down(self.green_tank_angle)
        if keys[pygame.K_w]:
            if self.green_tank_sprite_change_limiter == 5:
                if self.green_tank_angle == 0:
                    self.green_tank_angle = 22
                else:
                    self.green_tank_angle -= 1
                self.green_tank.move_left(self.green_tank_angle)
                self.green_tank_sprite_change_limiter = 0
            self.green_tank_sprite_change_limiter += 1
        if keys[pygame.K_s]:
            if self.green_tank_sprite_change_limiter == 5:
                if self.green_tank_angle == 23:
                    self.green_tank_angle = 1
                else:
                    self.green_tank_angle += 1
                self.green_tank.move_right(self.green_tank_angle)
                self.green_tank_sprite_change_limiter = 0
            self.green_tank_sprite_change_limiter += 1
        if keys[pygame.K_LEFT]:
            self.blue_tank.move_up(self.blue_tank_angle)
        if keys[pygame.K_RIGHT]:
            self.blue_tank.move_down(self.blue_tank_angle)
        if keys[pygame.K_UP]:
            if self.blue_tank_sprite_change_limiter == 5:
                if self.blue_tank_angle == 23:
                    self.blue_tank_angle = 1
                else:
                    self.blue_tank_angle += 1
                self.blue_tank.move_right(self.blue_tank_angle)
                self.blue_tank_sprite_change_limiter = 0
            self.blue_tank_sprite_change_limiter += 1
        if keys[pygame.K_DOWN]:
            if self.blue_tank_sprite_change_limiter == 5:
                if self.blue_tank_angle == 0:
                    self.blue_tank_angle = 22
                else:
                    self.blue_tank_angle -= 1
                self.blue_tank.move_left(self.blue_tank_angle)
                self.blue_tank_sprite_change_limiter = 0
            self.blue_tank_sprite_change_limiter += 1
        if keys[pygame.K_g] and not self.green_already_thrown:
            self.new_green_shot = Shot(GREEN_SHOT_SPRITE, self.green_tank.rect.center, self.green_tank.shot_x_speed,
                                       self.green_tank.shot_y_speed)
            self.all_sprites.add(self.new_green_shot)
            self.green_shot_limiter = 0
            self.green_already_thrown = True
        if keys[pygame.K_l] and not self.blue_already_thrown:
            self.new_blue_shot = Shot(BLUE_SHOT_SPRITE, self.blue_tank.rect.center, self.blue_tank.shot_x_speed,
                                      self.blue_tank.shot_y_speed)
            self.all_sprites.add(self.new_blue_shot)
            self.blue_shot_limiter = 0
            self.blue_already_thrown = True



     pygame.display.update()
        if self.green_shot_limiter == TICK_SHOT_LIMITER:
            self.green_already_thrown = False
        if self.blue_shot_limiter == TICK_SHOT_LIMITER:
            self.blue_already_thrown = False
        self.green_shot_limiter += 1
        self.blue_shot_limiter += 1