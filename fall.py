import pygame as pg
import random


class game:

    def __init__(self):
        self.score = 0
        self.dt = 0
        self.speed = 1
        self.running = True
        self.screen = pg.display.set_mode((800, 800))
        self.clock = pg.time.Clock()
        self.WIDTH = self.screen.get_width() 
        self.HEIGHT = self.screen.get_height() 
        pg.init()

    def player(self,color, player_x, player_y, player_w, player_h):
        player_pos = pg.Vector2(player_x,player_y)
        pg.draw.rect(self.screen,color, (player_pos,(player_w, player_h)) )

    def getPlayerPos(self, player_pos):

        self.pos = player_pos.x, player_pos.y

        return self.pos

    def ball(self, color, ball_x, ball_y, ball_w, ball_h):
        ball_pos = pg.Vector2(ball_x, ball_y)
        pg.draw.rect(self.screen, color, (ball_pos,(ball_w, ball_h)))

        if ball_pos.y <= self.HEIGHT:
            ball_y +=  1 * self.speed
        else:
             ball_y = 0
             ball_x = random.randint(0, self.WIDTH)

        
        # if ball_pos.y == getPlayerPos()- 50:
        #      y_pos = 0
        #      x_pos = random.randint(0, self.WIDTH)

    
    def control(self, dt, player_pos):
        keys = pg.key.get_pressed()
        # if keys[pg.K_k]:
        #     player_pos.y -= 300 * dt
        # if keys[pg.K_j]:
        #      player_pos.y += 300 * dt

        if keys[pg.K_h] and player_pos.x >= 0:
            player_pos.x -= 300 * dt

        if keys[pg.K_l] and player_pos.x <= (self.WIDTH - 100):
            player_pos.x += 300 * dt


    def play(self):

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            
            self.screen.fill('black')
            self.player("blue",0 ,0 ,100, 30)
            self.ball("yellow",0 ,0 ,100, 30)
            self.control(self.dt, 0)

            pg.display.update()
            self.dt = self.clock.tick(60) / 1000

        
        
        pg.quit()


