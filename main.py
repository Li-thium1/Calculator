import sys
import pygame

width = 800
height = 1000

pygame.init()

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Taschenrechner")

clock = pygame.time.Clock()

font = pygame.font.Font("Monocraft.ttf",110)

#key_size
rows = 5
columns = 4
margin = 20
textfeld = 200

key_width = (width - (columns+1) * margin) // columns
key_height =(height - textfeld - (rows+1) * margin) // rows

width_num, height_num = font.size("1")

#colors
key_color_num = (50, 50, 68)
key_color_num_hover = (70,70,88)
key_color_num_click = (35,  35,  53)


pressed_key_on_keyboard = ""
pressed_key_special = 0
layout = [
        ["C", "<", "%", "/"],
        ["7", "8", "9",  "*"],
        ["4", "5", "6",  "-"],
        ["1", "2", "3",  "+"],
        ["0",  ".", "="]
    ]

keyboard_keys = [
    [[pygame.K_DELETE, "C" , "c"], [pygame.K_BACKSPACE , "D" , "d"], ["%"], ["/"]],
    [["7"], ["8"], ["9"],  ["*"]],
    [["4"], ["5"], ["6"],  ["-"]],
    [["1"], ["2"], ["3"],  ["+"]],
    [["0"], [pygame.K_KP_PERIOD, "," , "."] , [pygame.K_RETURN, pygame.K_KP_ENTER,"="]]
]
list_for_calc = []
mouse_pos = (0,0)
key_pressed = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


        if event.type == pygame.KEYDOWN:
            pressed_key_on_keyboard = event.unicode
            pressed_key_special = event.key
            key_pressed = True

    
            
        if event.type == pygame.KEYUP:   
            pressed_key_on_keyboard = "" 
            pressed_key_special = 0
        

    screen.fill((20, 20, 30))

    
    for reihe_index, reihe in enumerate(layout):
        for spalte_index, zeichen in enumerate(reihe):
            
            x = margin + spalte_index * (key_width + margin)
            y = margin + textfeld + reihe_index * (key_height + margin)

            #special size for equal( = )
            if zeichen == "=":
                key_width = key_width * 2 + margin
            
            #hitbox of current block
            hitbox = pygame.Rect(x,y,key_width,key_height)

            # ---- mouse ---- mouse ---- mouse ---- #

            # num color when clicked
            if hitbox.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(screen, key_color_num_click,(x -7 ,y -7 ,key_width + 14 ,key_height + 14))
            # num color when hovered
            elif hitbox.collidepoint(pygame.mouse.get_pos()) and not pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(screen, key_color_num_hover,(x -7,y - 7,key_width + 14,key_height + 14))
            # num normal condition
            else:
                pygame.draw.rect(screen, key_color_num,(x ,y ,key_width ,key_height ))      

            #register the number / operator / function key  --AFTER MOUSECLICK--  just ONCE -----> into list
            if hitbox.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(screen, key_color_num_click,(x -7 ,y -7 ,key_width + 14 ,key_height + 14))
                list_for_calc.append(zeichen)
                print(list_for_calc) 

            
            # ---- keyboard ---- keyboard ---- keyboard ---- #
            
            key = keyboard_keys[reihe_index][spalte_index]
            # special keys
            DEL = keyboard_keys[0][1]
            CLR = keyboard_keys[0][0]
            EQL = keyboard_keys[-1][-1]
            if isinstance(key, list): #eigentlich unnötig aber für meine dukumentation
                if pressed_key_special in key or pressed_key_on_keyboard in key:
                    pygame.draw.rect(screen,key_color_num_click,(x ,y,key_width,key_height ))
            #register the number / operator / function key  --AFTER KEYPRESS--  just ONCE -----> into list
            if (pressed_key_special in key or pressed_key_on_keyboard in key) and key_pressed == True:
                #backspace 
                list_for_calc.append(zeichen)
                print(list_for_calc)
                key_pressed = False



            width_num, height_num = font.size(zeichen)
            dx_num = ( key_width - width_num ) // 2
            dy_num = ( key_height - height_num ) // 2 

            x_num = x + dx_num
            y_num = y + dy_num

            text = font.render(zeichen,True,(230, 230, 240))

            screen.blit(text, (x_num , y_num ))

            #reset key width
            key_width = (width - (columns+1) * margin) // columns
    mouse_pos = (0,0)   
    pygame.display.flip()
    clock.tick(240)
    