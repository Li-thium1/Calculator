import sys
import pygame
width = 800
height = 1000

pygame.init()

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Taschenrechner")

clock = pygame.time.Clock()

font = pygame.font.Font("BitcountGridSingle_Roman-Regular.ttf",110)

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

#colors
key_color_num = (50, 50, 68)
key_color_num_hover = (70,70,88)
key_color_num_click = (35,  35,  53)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    
    screen.fill((20, 20, 30))
    
    layout = [
        ["C", "<", "%", "/"],
        ["7", "8", "9",  "*"],
        ["4", "5", "6",  "-"],
        ["1", "2", "3",  "+"],
        ["0",  ".", "="]
    ]

    for reihe_index, reihe in enumerate(layout):
        for spalte_index, zeichen in enumerate(reihe):
            x = margin + spalte_index * (key_width + margin)
            y = margin + textfeld + reihe_index * (key_height + margin)
            
            #special size for equal( = )
            if zeichen == "=":
                key_width = key_width * 2 + margin
            
            
            #hitbox of current block
            hitbox = pygame.Rect(x,y,key_width,key_height)
            
            if pygame.key.get_pressed()[int(zeichen)]:
                print(zeichen)
             

            # num color when hovered
            if hitbox.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
                pygame.draw.rect(screen,key_color_num_hover,(x - 7,y - 7,key_width + 14,key_height + 14))
            # num normal condition
            else:
                pygame.draw.rect(screen,key_color_num,(x,y,key_width,key_height))
            # num color when clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if left mousebutton
                if event.button == 1:

                    if pygame.mouse.get_pos()[0] > x and pygame.mouse.get_pos()[0] < x + key_width and pygame.mouse.get_pos()[1] > y and pygame.mouse.get_pos()[1] < y + key_height:
                        pygame.draw.rect(screen,key_color_num_click,(x -7 ,y -7 ,key_width + 14 ,key_height + 14))


            width_num, height_num = font.size(zeichen)
            dx_num = ( key_width - width_num ) // 2
            dy_num = ( key_height - height_num ) // 2 

            x_num = x + dx_num
            y_num = y + dy_num

            taste = pygame.Rect(x, y, key_width, key_height)
            tasten.append((taste, zeichen))

            text = font.render(zeichen,True,(230, 230, 240))

            screen.blit(text, (x_num , y_num ))

            #reset key width
            key_width = (width - (columns+1) * margin) // columns
    

    """while i <= 3:
        
        i += 1"""


   





    pygame.display.flip()
    clock.tick(60)
    