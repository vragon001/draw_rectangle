import pygame
pygame.init()
window=pygame.display.set_mode((690,690))
window.fill((255,255,255))
green=(0,255,0)
pygame.draw.circle(window,green,(300,300),50)
pygame.draw.circle(window,green,(300,500),50,3)
pygame.display.flip()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()