import os, sys;
from colorama import init, Back;

init()

global X #columns
global Y #rows

def ClearConsole():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('darwin'):
        os.system('clear')

def Draw(x, y, color):
    print("\033[%d;%dH" % (y, x)+color+" ")

def NumberToColor(number):
    if number == 0:
        return Back.LIGHTWHITE_EX
    if number == 1:
        return Back.LIGHTCYAN_EX
    if number == 2:
        return Back.LIGHTMAGENTA_EX
    if number == 3:
        return Back.BLACK
    if number == 4:
        return Back.RED
    if number == 5:
        return Back.GREEN
    if number == 6:
        return Back.YELLOW
    if number == 7:
        return Back.BLUE
    if number == 8:
        return Back.WHITE
    else:
        return Back.BLACK
    
def endWorld():
    global X
    print("\033[%d;%dH" % (20 + Y,1))

#States

player = [[1,9],[1,10],[1,11]]
select_hand = [2,10]
direction = 1 # 1 = right , 0 = left
count_wood = 0
count_stone = 0

Y = 3 # rows
X = 2 # columns

world=[
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6],

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6],

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,6,6,6],

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,5,0,0,0,6,0,6,0],

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,5,5,5,0,0,0,0,0,0],

[0,0,0,0,5,0,0,0,0,0,5,0,0,0,0,0,5,0,5,5,5,5,5,5,5,0,0,0,0,0],

[0,0,0,5,5,5,0,0,0,5,5,5,0,0,0,5,5,5,0,0,0,4,0,0,0,0,0,0,0,0],

[0,0,5,5,5,5,5,0,5,5,5,5,5,0,5,5,5,5,5,0,0,4,0,0,5,0,0,0,5,0],

[0,0,0,0,4,0,0,0,0,0,4,0,0,0,0,0,4,0,0,0,0,4,0,5,5,5,0,5,5,5],

[0,0,0,0,4,0,0,8,0,0,4,0,0,0,0,0,4,0,0,0,0,4,0,0,4,0,0,0,4,0],

[0,0,0,0,4,0,8,8,8,0,4,0,0,0,0,8,4,0,0,0,0,4,0,0,4,0,0,0,4,0],

[0,0,0,0,4,0,8,8,8,0,4,8,0,0,8,8,4,0,0,8,0,4,0,0,4,0,0,0,4,8],

[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7,7,7,5,5],

[3,3,3,3,8,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,7,7,7,3,3],

[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,8,3,8,7,7,7,3,3],

[3,3,3,3,3,3,8,3,3,8,3,3,3,3,3,3,3,3,3,3,3,3,8,3,3,7,7,7,3,3],

[3,8,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,8,3,3,7,7,7,3,3],

[3,3,3,3,8,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,8,3,3,3,3,3,3,3],

[3,3,3,3,3,3,8,3,3,3,3,3,3,3,8,3,3,3,3,3,3,3,3,3,3,3,3,3,8,3],

[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]

]

# Functions

def DrawWorld():
    global X
    global Y
    global world
    for y in range(0, len(world)):
        for x in range(0, len(world[y])):
            Draw(X + x, Y + y, NumberToColor(world[y][x]))
            x += 1
        y += 1


def DrawWorldEmpty():
    i=0
    print("Welcome to the world of Minecraft 2D XYZ: ")
    print("0123456789012345678901234567890")
    while i < 20:
        print(str((i+1)%10)+"                              ")
        i += 1

def DrawPlayer():
    Draw(select_hand[0]+X, select_hand[1]+Y, NumberToColor(2))
    for part in player:
        Draw(part[0]+X, part[1]+Y, NumberToColor(1))

def MovePlayer(action):
    global direction
    if action == "right":
        if 29 == player[0][0]:
            return "ERROR, you can't go further"
        
        else: ## player[0][0] < 29
            if direction==0: # if player watching to the left
                direction=1
                select_hand[0]=select_hand[0]+2

            else: # if player watching to the right
                player[0][0]=player[0][0]+1
                player[1][0]=player[1][0]+1
                player[2][0]=player[2][0]+1
                select_hand[0]=select_hand[0]+1
            return "Right"

    elif action == "left":
        if 0 == player[0][0]:
            return "ERROR, you can't go further"
        
        else:
            if direction==1:
                direction=0
                select_hand[0]=select_hand[0]-2
            else:
                player[0][0]=player[0][0]-1
                player[1][0]=player[1][0]-1
                player[2][0]=player[2][0]-1
                select_hand[0]=select_hand[0]-1
            return "Left"
        
    elif action == "top":
        if player[0][1] > 0:
            player[0][1] -= 1
            player[1][1] -= 1
            player[2][1] -= 1
            select_hand[1] -= 1

            return "Top"

        else:
            return "ERROR, you can't go further"

    elif action == "down":
        if player[0][1] < 12:
            player[0][1] += 1
            player[1][1] += 1
            player[2][1] += 1
            select_hand[1] += 1

            return "Down"

        else:
            return "ERROR, you can't go further"

def CollectBlocks():
    global count_wood
    global count_stone

    if world[select_hand[1]][select_hand[0]] == 8:
        world[select_hand[1]][select_hand[0]] = 0
        count_stone += 1

    if world[select_hand[1]][select_hand[0]] == 4:
        world[select_hand[1]][select_hand[0]] = 0
        count_wood += 1

def DestroyBlocks():
    if world[select_hand[1]][select_hand[0]] == 3:
        world[select_hand[1]][select_hand[0]] = 0

    if world[select_hand[1]][select_hand[0]] == 4:
        world[select_hand[1]][select_hand[0]] = 0

    if world[select_hand[1]][select_hand[0]] == 5:
        world[select_hand[1]][select_hand[0]] = 0

    if world[select_hand[1]][select_hand[0]] == 6:
        world[select_hand[1]][select_hand[0]] = 0

    if world[select_hand[1]][select_hand[0]] == 7:
        world[select_hand[1]][select_hand[0]] = 0

    if world[select_hand[1]][select_hand[0]] == 8:
        world[select_hand[1]][select_hand[0]] = 0