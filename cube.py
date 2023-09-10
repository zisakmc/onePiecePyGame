import pygame as pg
import random
import os
import threading

pg.init()

screen = pg.display.set_mode((800, 800))

clock = pg.time.Clock()

running = True

dt = 0

width = screen.get_width()
height = screen.get_height()
player_pos = pg.Vector2(width - (width / 2), height - (height / 10))
y_pos = 0
speed = 5 
score = 0
high_score = 0
miss = 0
ctime = 0

x_pos = random.randint(10, width - 20)

white = (255, 255, 255)
pg.font.init()
font = pg.font.SysFont('firacode', 22) 

with open('highScore.txt','r') as f:
    high_score =int( f.read() )


# fonts = pg.font.get_fonts()
# for f in fonts:
#    print(f)
#
sunny = pg.image.load(os.path.join('resource', 'sunny.png'))
boat = pg.image.load(os.path.join('resource', 'boat.png'))
sea = pg.image.load(os.path.join('resource', 'sea.jpg'))
sunny = pg.transform.scale(sunny,(50,50))
boat = pg.transform.scale(boat,(100,60))

choper = pg.mixer.music.load(os.path.join('resource', 'choper.mp3'))
theme = pg.mixer.music.load(os.path.join('resource', 'theme.mp3'))
pg.mixer.music.play(-1)

def effect(sounds,chan):
    # m=pg.mixer.Sound(os.path.join('resource', sounds))
    pg.mixer.Channel(chan).play(pg.mixer.Sound(os.path.join('resource', sounds))
)

t2 = threading.Thread(target=effect, args=('theme.mp3',0,))
t2.start()
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # ctime = time.time()
    screen.blit(sea,(0,0))
    # pg.draw.rect(screen, "blue",(player_pos,(100,30)) )
    screen.blit(boat, player_pos) 
    # txt_time= font.render(f"{ctime} ", True, white)
    txt_score= font.render(f"Score : {score} ", True, white)
    txt_speed = font.render(f"Speed : {speed} ", True, white)
    txt_miss = font.render(f"Misses : {miss}", True, white)
    txt_high= font.render(f"High Score : {high_score}", True, white)
    # screen.blit(txt_time,(10,20))
    screen.blit(txt_score,(10,50))
    screen.blit(txt_speed,(10,80))
    screen.blit(txt_miss,(10,110))
    screen.blit(txt_high,(10,140))

    ball = pg.Vector2(x_pos, y_pos)

    if score >= 80:
        speed = 7 
    if score >= 150:
        speed = 10




    if ball.y <= height:
       y_pos +=  speed

    else:

        t1 = threading.Thread(target = effect, args=("nami.mp3",1)) 
        t1.start()
        t1.join()
        y_pos = 0
        x_pos = random.randint(10, width - 20)
        miss+= 1

    if ball.y >= player_pos.y - 50 and \
       ball.y <= player_pos.y and \
       ball.x >= player_pos.x and \
       ball.x <= player_pos.x + 100:
        y_pos = 0
        x_pos = random.randint(10, width - 20)
        t1 = threading.Thread(target = effect, args=("recieve.mp3",2)) 
        t1.start()
        t1.join()

        if score >= 300:
            score += 20
        elif score >=80 and score < 300: 
            score += 15
        else:
            score += 10

    

    # pg.draw.rect(screen, "yellow", (ball, (5,50)))
    screen.blit(sunny, ball) 
    keys = pg.key.get_pressed()


    # if keys[pg.K_k]:
    #     player_pos.y -= 300 * dt
    # if keys[pg.K_j]:
    #     player_pos.y += 300 * dt
    if (keys[pg.K_h] or keys[pg.K_LEFT]) and player_pos.x >= 0:
        player_pos.x -= 500 * dt

    if (keys[pg.K_l] or keys[pg.K_RIGHT]) and player_pos.x <= (width - 100):
        player_pos.x += 500 * dt
        
    
    if score > high_score:
        high_score = score
        with open("highScore.txt", 'w') as f:
            f.write(str(score))

    # if miss >= 10:
    #     running = False
    pg.display.update()
    dt = clock.tick(60) / 1000
pg.quit()


