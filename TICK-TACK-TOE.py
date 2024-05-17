import random
possiblenumbers=[1,2,3,4,5,6,7,8,9]
gameboard=[[1,2,3],[4,5,6],[7,8,9]]
row = 3
col=3

def printgameboard():
    for x in range(row):
        print('\n+---+---+---+')
        print("|",end='')
        for y in range(col):
            print("",gameboard[x][y],end=' |')
    print("\n+---+---+---+")


def modifyarray(n,turn):
    n-=1
    if(n==0):
        gameboard[0][0]=turn
    elif(n==1):
        gameboard[0][1]=turn
    elif(n==2):
        gameboard[0][2]=turn
    elif(n==3):
        gameboard[1][0]=turn
    elif(n==4):
        gameboard[1][1]=turn
    elif(n==5):
        gameboard[1][2]=turn
    elif(n==6):
        gameboard[2][0]=turn
    elif(n==7):
        gameboard[2][1]=turn
    elif(n==8):
        gameboard[2][2]=turn


def winner(gameboard):
    if(gameboard[0][0]==gameboard[0][1]==gameboard[0][2]):
        if(gameboard[0][0]=='X'):
            print('X wins')
            return True
        else:
            if(gameboard[0][0]=='O'):
                print('CPU wins')
                return True
            return False


    if(gameboard[1][0]==gameboard[1][1]==gameboard[1][2]):
        if(gameboard[1][0]=='X'):
            print('X wins')
            return True
        else:
            if(gameboard[1][0]=='O'):
                print('CPU wins')
                return True
            return False


    if(gameboard[2][0]==gameboard[2][1]==gameboard[2][2]):
        if(gameboard[2][0]=='X'):
            print('X wins')
            return True
        else:
            if(gameboard[2][0]=='O'):
                print('CPU wins')
                return True
            return False


    if(gameboard[0][0]==gameboard[1][0]==gameboard[2][0]):
        if(gameboard[0][0]=='X'):
            print('X wins')
            return True
        else:
            if(gameboard[0][0]=='O'):
                print('CPU wins')
                return True
            return False

    if(gameboard[0][1]==gameboard[1][1]==gameboard[2][1]):
        if(gameboard[0][1]=='X'):
            print('X wins')
            return True
        else:
            if(gameboard[0][1]=='O'):
                print('CPU wins')
                return True
            return False


    if(gameboard[0][2]==gameboard[1][2]==gameboard[2][2]):
        if(gameboard[0][2]=='X'):
            print('X wins')
            return True
        else:
            if(gameboard[0][2]=='O'):
                print('CPU wins')
                return True
            return False

    if(gameboard[0][0]==gameboard[1][1]==gameboard[2][2]):
        if(gameboard[0][0]=='X'):
            print('X wins')
            return True
        else:
            if(gameboard[0][0]=='O'):
                print('CPU wins')
                return True
            return False

    if(gameboard[2][0]==gameboard[1][1]==gameboard[0][2]):
        if(gameboard[2][0]=='X'):
            print('X wins')
            return True
        else:
            if(gameboard[2][0]=='O'):
                print('CPU wins')
                return True
            return False


li=[]
turn=1
move=0
while(True):
    if(turn==1):
        printgameboard()
        npick=int(input("Enter the block number\n"))
        if npick in li:
            print("Already picked by CPU, choose another slot")
        elif(npick>=1 and npick<=9):
            modifyarray(npick,'X')
            possiblenumbers.remove(npick)
            move+=1
            if winner(gameboard):
                printgameboard()
                break
            if(move==9):
                print('DRAW')
                break
            turn=0
        else:
            print("invalid input")
    else:
        cpu=random.choice(possiblenumbers)
        li.append(cpu)
        if cpu in possiblenumbers:
            modifyarray(cpu,'O')
            possiblenumbers.remove(cpu)
            if winner(gameboard):
                print('CPU WINS')
                break

            turn=1
