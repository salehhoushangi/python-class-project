#!/usr/bin/python3.6
import random
import os
dimension_value = int(input("inter your dimension\n"))

def show_location(i,row):
    global x
    global y
    y=row
    x=i/2

def scape_door():
    global scap_y,scap_x
    while True:
        scap_y=random.randint(0,dimension_value-1)
        scap_x= int(random.randint(1,dimension_value*2)/2)
        if scap_x%2 != 0 :
            break
    return(scap_x,scap_y)


def dragon_locate():
    global dragon_x,dragon_y
    while True:
        dragon_y=random.randint(0,dimension_value-1)
        dragon_x= int(random.randint(1,dimension_value*2)/2)
        if dragon_x%2 != 0 :
            break
    return(dragon_x,dragon_y)


def draw_box(i,row):
    user_location=1
    for a in range(dimension_value):
            print(" _",end='')
    for row in range(dimension_value):
        print("")
        for i in range (dimension_value*2+1):
            if i%2 == 0 :
                print("|",end='') 

            elif  i == b and user_location==1 and row == d :
                user_location=user_location+1
                print("X",end='')
                show_location(i,row)
            else:
                print("_",end='')
    print("")
    print("you are currently in room({},{})".format(int(x),(y)))
    


def clear_screen():
    os.system('cls' if  os.name == 'nt' else 'clear')

while True:
    d=random.randint(0,dimension_value-1)
    b = random.randint(1,dimension_value*2)
    if b%2 != 0 :
        break
    #return(b,d) 

draw_box(b,d)
dragon_x,dragon_y = dragon_locate()
scape_x,scape_y= scape_door()

while True :
    print('''you can move LEFT , RIGHT , DOWN ,UP
    Enter 'QUIT' to Exit Game. ''')
    direction=input(" >>").lower()
    condition_lost=bool(b == dragon_x and d == dragon_y)
    condition_win=bool(b == scape_x and d == scap_y)
    if direction == "right":
        print(b)
        print(dimension_value)
        if b<=(dimension_value*2):
            clear_screen()
            b=b+2 
            show_location(x,y)
            draw_box(b,d)
        else:
            draw_box(b,d)
            continue
    elif direction == "left":
        if b>1:
            clear_screen()
            b=b-2
            draw_box(b,d)
        else:
            draw_box(b,d)
            continue
    elif direction == "up":
        if d >=0 :
            clear_screen()
            d=d-1
            draw_box(b,d)
        else:
            draw_box(b,d)
            continue
    elif direction == "down":
        if d<=(dimension_value-1):
            clear_screen()
            d=d+1
            draw_box(b,d)
        else:
            draw_box(b,d)
            continue
    elif direction == "quit":
        print("thanks for gaming")
        break
    if (condition_win):
          print("congratulation :) you are winner")
          break
    else:
        if (condition_lost) :
            print("sorry :( you are GameOver!")
            break

