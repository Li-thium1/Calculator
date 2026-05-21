import sys
import pygame
width = 800
height = 800

pygame.init()

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Taschenrechner")

clock = pygame.time.Clock()

font = pygame.font.Font("BitcountGridSingle_Roman-Light.ttf",110)

text = font.render("9",True,(255,255,255))
rect = text.get_rect()
print(rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    
    screen.fill((0,0,0))

    pygame.draw.rect(screen,(254, 100, 0),(1,28,53,64))
    

    
    
    screen.blit(text, (0,0))




    pygame.display.flip()
    clock.tick(60)