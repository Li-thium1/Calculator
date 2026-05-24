import sys
import pygame

width = 800
height = 1000

pygame.init()

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("MonoCalc")

clock = pygame.time.Clock()

#key_size
rows = 5
columns = 4
margin = 20
textfeld = 300
font = pygame.font.Font("Monocraft.ttf",95)

key_width = (width - (columns+1) * margin) // columns
key_height =(height - textfeld - (rows+1) * margin) // rows

width_num, height_num = font.size("1")

#colors

def key_hover_color(color):
    return ( color[0] + 20 , color[1] + 20 , color[2] + 20 )

def key_click_color(color):
    return ( color[0] - 15 , color[1] - 15 , color[2] - 15 )
#   num keys
key_color_num = (50, 50, 68)

#   operator keys 
key_color_op = (100, 60, 140)
  
#   function keys
key_color_func = (70, 75, 100)


key_color_special = {

    "C": key_color_func,
    "<": key_color_func,
    "%": key_color_func,

    "/": key_color_op,
    "*": key_color_op,
    "-": key_color_op,
    "+": key_color_op,
    "=": key_color_op,
}

pressed_key_on_keyboard = ""
pressed_key_special = 0
layout = [
        ["C", "<", "%", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0",  ".", "="]
    ]

keyboard_keys = [
    [[pygame.K_DELETE, "C" , "c"], [pygame.K_BACKSPACE , "D" , "d"], ["%"], ["/"]],
    [["7"], ["8"], ["9"],  ["*"]],
    [["4"], ["5"], ["6"],  ["-"]],
    [["1"], ["2"], ["3"],  ["+"]],
    [["0"], [pygame.K_KP_PERIOD, "," , "."] , [pygame.K_RETURN, pygame.K_KP_ENTER,"="]]
]

operators = ["+", "-", "*", "/", "%"]

list_for_calc = []
mouse_pos = (0,0)
key_pressed = False
mouse_pressed = False
calculate = False
printing =  False
display_text = ""


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_pressed = True

        
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
        for spalte_index, zeichen in enumerate(reihe):  # num data is the different 3. under-lists of the big list layout
            x = margin + spalte_index * (key_width + margin)
            y = margin + textfeld + reihe_index * (key_height + margin)

            key_color = key_color_special.get(zeichen , key_color_num )

            #special size for equal( = )
            if zeichen == "=":
                key_width = key_width * 2 + margin
            
            #hitbox of current block
            hitbox = pygame.Rect(x,y,key_width,key_height)

            # ---- mouse ---- mouse ---- mouse ---- #

            # num color when clicked
            if hitbox.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(screen, key_click_color(key_color),(x -7 ,y -7 ,key_width + 14 ,key_height + 14),0,15)
            # num color when hovered
            elif hitbox.collidepoint(pygame.mouse.get_pos()) and not pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(screen, key_hover_color(key_color),(x -7,y - 7,key_width + 14,key_height + 14),0,15)
            # num normal condition
            else:
                pygame.draw.rect(screen, key_color,(x ,y ,key_width ,key_height ),0,15)      

            #register the number / operator / function key  --AFTER MOUSECLICK--  just ONCE -----> into list
            if hitbox.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] and mouse_pressed == True:
                #  DEL 
                if zeichen == "<" and mouse_pressed == True and len(list_for_calc) >= 1:
                    list_for_calc.pop()
                    print(list_for_calc)
                    mouse_pressed = False
                    printing = True
                elif zeichen == "<" and len(list_for_calc) == 0:
                    print(list_for_calc)
                    mouse_pressed = False
                    
                #  CLR 
                elif zeichen == "C":
                    list_for_calc = []
                    print(list_for_calc)
                    mouse_pressed = False
                    printing = True
                # percent
                elif zeichen == "%":
                    list_for_calc.append(" * ")
                    list_for_calc.append("0.01")

                    print(list_for_calc)
                    mouse_pressed = False
                    printing = True
                # calculate / ======
                elif zeichen == "=":
                    print(list_for_calc)
                    calculation = display_text
                    mouse_pressed = False
                    calculate = True
                    

                else:
                    if zeichen in operators:
                        list_for_calc.append( " "+ zeichen + " " )
                        print(list_for_calc)
                        mouse_pressed = False
                    else:
                        list_for_calc.append( zeichen )
                        print(list_for_calc)
                        mouse_pressed = False 
                    printing = True

            
            # ---- keyboard ---- keyboard ---- keyboard ---- #
            
            key = keyboard_keys[reihe_index][spalte_index]
            # special keys
            
            CLR = keyboard_keys[0][0]
            DEL = keyboard_keys[0][1]
            EQL = keyboard_keys[-1][-1]

            if isinstance(key, list): #eigentlich unnötig aber für meine dukumentation
                if pressed_key_special in key or pressed_key_on_keyboard in key:
                    pygame.draw.rect(screen,key_click_color(key_color),(x ,y,key_width,key_height ),0,15)

            # DEL --- DEL --- DEL --- DEL --- DEL
            # DEL deleting 1 after another
            if (pressed_key_special in DEL or pressed_key_on_keyboard in DEL) and key_pressed == True and len(list_for_calc) >= 1:
                list_for_calc.pop()
                print(list_for_calc)

                key_pressed = False
                printing = True

            # DEL special case if len list == 0 -----> no pop() and key_pressed = False ------> so no append of "<" to the list
            if (pressed_key_special in DEL or pressed_key_on_keyboard in DEL) and key_pressed == True and len(list_for_calc) == 0:
                print(list_for_calc)

                key_pressed = False
                
            # CLR --- CLR --- CLR --- CLR --- CLR
            if (pressed_key_special in CLR or pressed_key_on_keyboard in CLR) and key_pressed == True:
                list_for_calc = []
                print(list_for_calc)

                key_pressed = False
                printing = True
            # EQL --- EQL --- EQL --- EQL --- EQL
            if (pressed_key_special in EQL or pressed_key_on_keyboard in EQL) and key_pressed == True:

                key_pressed = False
                calculate = True

            #register the number ((/ operator / function)) key  --AFTER KEYPRESS--  just ONCE -----> into list
            if (pressed_key_special in key or pressed_key_on_keyboard in key) and key_pressed == True:
                #backspace 
                list_for_calc.append(zeichen)
                print(list_for_calc)

                key_pressed = False
                printing == True

            calculation_display = font.render(display_text,True,(230, 230, 240))
            screen.blit(calculation_display, (20 , 0 ))

            


            # drawing numbers , operators and special onto keys
            width_num, height_num = font.size(zeichen)
            dx_num = ( key_width - width_num ) // 2
            dy_num = ( key_height - height_num ) // 2 

            x_num = x + dx_num
            y_num = y + dy_num

            text = font.render(zeichen,True,(230, 230, 240))

            screen.blit(text, (x_num , y_num ))

            #reset key width
            key_width = (width - (columns+1) * margin) // columns
    expression = "".join(list_for_calc)
    #rusult
    if calculate == True and len(list_for_calc) > 0 :
        result = eval(expression)
        print("= " + str(result))
        calculate = False
        list_for_calc = []

        display_text = "= " + str(result)
    # before result
    else:
        if printing == True:
            print(str(expression))
            printing = False
            display_text = str(expression)
            
    
    pygame.display.flip()
    clock.tick(120)
