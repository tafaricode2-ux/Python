import pygame
pygame.init()

screen = pygame.display.set_mode((400,500))
GREEN = (0,225,0)
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
    pygame.draw.circle(screen,(0,125,255),(200,200),50)
    pygame.draw.circle(screen,GREEN,(100,100),70,10)
    pygame.display.flip()
