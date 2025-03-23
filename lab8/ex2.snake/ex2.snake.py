import pygame
import random
import time

snake_speed = 5

pygame.init()

W, H = 720, 480

#defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((W, H))

FPS = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruit_pos = [random.randrange(1, (W//10))*10, random.randrange(1, (H//10))*10]

fruit_spawn = True

direction = "RIGHT"
change_to = direction

score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.Font(font, size)

    score_surf = score_font.render('Score: '+str(score), True, color)

    score_rect = score_surf.get_rect()

    screen.blit(score_surf, score_rect)

def game_over():
    my_font = pygame.font.Font("font_user (1).ttf", 30)

    game_over_surf = my_font.render("Your score is: "+str(score), True, RED)

    game_over_rect = game_over_surf.get_rect()

    game_over_rect.midtop = (W/4, H/4)

    screen.blit(game_over_surf, game_over_rect)

    
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    exit()

count_food = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
    
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        count_food += 1
        fruit_spawn = False

    else:
        snake_body.pop()
    
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (W//10))*10, random.randrange(1, (H//10))*10]

    fruit_spawn = True
    screen.fill(BLACK)

    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(screen, RED, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0]>W-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > H-10:
        game_over()
    
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    if count_food == 4 and snake_speed < 24:
        snake_speed += 3
        count_food = 0
    show_score(1, PURPLE, 'font_user (1).ttf', 20)
    pygame.display.update()

    FPS.tick(snake_speed)