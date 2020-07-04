import pygame

pygame.init()
max_height = 300
max_width = 400

rect_width = 60

screen = pygame.display.set_mode((max_width, max_height))
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

        if x >= max_width:
            x = -rect_width
        elif x < -rect_width: x = max_width - 1 

        if y >= max_height:
            y = -rect_width
        elif y < -rect_width: y = max_height - 1 

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color, pygame.Rect(x, y, rect_width, rect_width))
        pygame.display.flip()

        # will block execution until 1/60 seconds have passed
        # since the previous time clock.tick was called.
        clock.tick(60)
