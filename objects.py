from Settings import *
import random
# Ball globals
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_xv = 4
ball_yv = 4
ball_r = 10

# Draw  1
racket1_x = 10
racket1_y = 10
racket1_w = 13
racket1_h = 100

# Draw racket 2
racket2_x = screen_width - 35
racket2_y = 10
racket2_w = 13
racket2_h = 100

def ran_sighn ():
    return [-1,1][random.randrange(2)]

def colision (ball_x, ball_y , ball_xv, ball_yv, ball_r, racket1_x, racket1_y, racket1_w, racket1_h, racket2_x, racket2_y, racket2_w, racket2_h, screen_height):
    # Collision of ball with top/bottom of the screen
    if ball_y - ball_r <= 0 or ball_y + ball_r >= screen_height:
        ball_yv *= -1.05

    # Collision of rackets with top/bottom of the screen
    if racket1_y < 0:
        racket1_y = 0
    elif racket1_y + racket1_h > screen_height:
        racket1_y = screen_height - racket1_h

    if racket2_y < 0:
        racket2_y = 0
    elif racket2_y + racket2_h > screen_height:
        racket2_y = screen_height - racket2_h


    if ball_x - ball_r < racket1_x + racket1_w and ball_y+ball_r >= racket1_y and ball_y -ball_r <= racket1_y + racket1_h and ball_x > racket1_x + racket1_w:
        ball_xv *= -1.05
    if ball_x + ball_r > racket2_x and ball_y +ball_r >= racket2_y and ball_y -ball_r <= racket2_y + racket2_h and ball_x < racket2_x:
        ball_xv *= -1.05
    return ball_xv, ball_yv, racket1_y, racket2_y

