import pygame
import time
import random
from Settings import *
from objects import *
pygame.init()



game_screen = pygame.display.set_mode((screen_width, screen_height)) # задаем экран
pygame.display.set_caption("Теннис большой это хорошо")
font = pygame.font.SysFont("arial", 60)


# счет
player1_score = 0
player2_score = 0
# пауза
s = 0
pause = False
game_over = False
while not game_over:
    pressed = pygame.key.get_pressed()
    pygame.key.set_repeat()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    if pressed[pygame.K_ESCAPE]:
        game_over = True
    if pressed[pygame.K_p]:
            pause = True
    if pressed[pygame.K_u]:
            pause = False
    if player1_score >= 5:
        win1_text = font.render("WIN LEFT", 1, color_score)
        game_screen.blit(win1_text, (160, 200))
        pygame.display.update()
        if pressed[pygame.K_r]:
            player2_score = 0
            player1_score = 0
    elif player2_score >= 5:
        win2_text = font.render("WIN RIGHT", 1, color_score)
        game_screen.blit(win2_text, (160, 200))
        pygame.display.update()
        if pressed[pygame.K_r]:
            player2_score = 0
            player1_score = 0
    elif pause:
        pause_text = font.render("PAUSE", 1, color_score)
        game_screen.blit(pause_text, (160, 200))
        pygame.display.update()
    else:
        if pressed[pygame.K_w]:
            racket1_y -= 5
        elif pressed[pygame.K_s]:
            racket1_y += 5

        if pressed[pygame.K_UP]:
            racket2_y -= 5
        elif pressed[pygame.K_DOWN]:
            racket2_y += 5

        # движение шара
        ball_x += ball_xv
        ball_y += ball_yv

        (ball_xv, ball_yv, racket1_y, racket2_y) = colision(ball_x, ball_y, ball_xv, ball_yv, ball_r, racket1_x, racket1_y, racket1_w, racket1_h, racket2_x, racket2_y,
                 racket2_w, racket2_h, screen_height)

        # счет
        if ball_x <= 0:
            player2_score += 1
            ball_x = screen_width // 2
            ball_y = screen_height // 2
            ball_xv = 4 * ran_sighn()
            ball_yv = 4 *ran_sighn()
        elif ball_x >= screen_width:
            player1_score += 1
            ball_x = screen_width // 2
            ball_y = screen_height // 2
            ball_xv = 4 * ran_sighn()
            ball_yv = 4 * ran_sighn()

        #отрисовка
        game_screen.fill(color_field)
        racket_1 = pygame.draw.rect(game_screen, color_p1, (racket1_x, racket1_y, racket1_w, racket1_h), 0)
        racket_2 = pygame.draw.rect(game_screen, color_p2, (racket2_x, racket2_y, racket2_w, racket2_h), 0)
        net = pygame.draw.line(game_screen, color_net , (300, 5), (300, 400))
        ball = pygame.draw.circle(game_screen, color_ball, (ball_x, ball_y), ball_r, 0)

        score_text = font.render(str(player1_score) + " " + str(player2_score), 1, color_score)
        game_screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 10))

        pygame.display.update()

        time.sleep(0.01666)

pygame.quit()
