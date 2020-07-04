import pygame

pygame.init()
pygame.mixer.music.load('foo.ogg')
pygame.mixer.music.play(0)


screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))

        pygame.display.flip()
        clock.tick(60)
