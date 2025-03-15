import pygame

pygame.init()
W, H = 600, 400
sc = pygame.display.set_mode((W, H))

WHITE = (255, 255, 255)
RED = (255, 0, 0)


speed = 20
x, y = W//2, H//2

clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.fill(WHITE)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        if y>H-27:
            y = H-26
        else:
            y += speed
    if pressed[pygame.K_UP]:
        if y<27:
            y=26
        else:
            y -= speed
    if pressed[pygame.K_LEFT]:
        if x<27:
            x=26
        else:
            x-=speed
    if pressed[pygame.K_RIGHT]:
        if x>W-27:
            x=W-26
        else:
            x+=speed
    

    circle = pygame.draw.circle(sc, RED, (x, y), 25)
    
    pygame.display.update()
    clock.tick(60)
            