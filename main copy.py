import sys
import pygame
width = 800
height = 1000

pygame.init()

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Taschenrechner")

clock = pygame.time.Clock()

font = pygame.font.Font("BitcountGridSingle_Roman-Light.ttf",110)

#key_size
rows = 5
columns = 4
margin = 20
textfeld = 200

key_width = (width - (columns+1) * margin) // columns
key_height =(height - textfeld - (rows+1) * margin) // rows

width_num, height_num = font.size("1")

print(width_num, height_num)


tasten = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    
    screen.fill((20, 20, 30))
    
    
    """i = 1
    

    hitbox1 = pygame.Rect(margin,margin,key_width,key_height)

    #change size when hovered
    if hitbox1.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
        pygame.draw.rect(screen,(70,70,88),(margin-5,margin-5,key_width+10,key_height+10))    
    else:  # normal color  
        pygame.draw.rect(screen,(50, 50, 68),(margin,margin,key_width,key_height))

    #change color when clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if pygame.mouse.get_pos()[0] > margin and pygame.mouse.get_pos()[0] < margin + key_width and pygame.mouse.get_pos()[1] > margin and pygame.mouse.get_pos()[1] < margin + key_height:
                pygame.draw.rect(screen,(35,  35,  53),(margin-5,margin-5,key_width+10,key_height+10))"""

    layout = [
        ["C", "<", "%", "/"],
        ["7", "8", "9",  "*"],
        ["4", "5", "6",  "-"],
        ["1", "2", "3",  "+"],
        ["0",  ".", "="]
    ] 
    
    

    pygame.display.flip()
    clock.tick(15)