import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
alive = True
is_blue = True
x = 30
y = 30

dx = 1
dy = 0

clock = pygame.time.Clock()

while alive:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        alive = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue

        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            dy = -1
            dx = 0
        if pressed[pygame.K_DOWN]: 
            dy = 1
            dx = 0
        if pressed[pygame.K_LEFT]: 
            dx = -1
            dy = 0
        if pressed[pygame.K_RIGHT]: 
            dx = 1
            dy = 0

        x += dx
        y += dy

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        pygame.display.flip()

        # will block execution until 1/60 seconds have passed
        # since the previous time clock.tick was called.
        clock.tick(60)
