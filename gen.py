import random
from random import choice

from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)

def generatePath(H,V,rooms):
    V_ROOM_COUNT=V
    H_ROOM_COUNT=H

    #clear the map 
    map = []

    # make an array to store the path points for special items. 
    # A big key needs to spawn in this path
    path = []
    
    # initialize / fill the map array with 0's
    for y in range(V_ROOM_COUNT):
        map.append([])
        for x in range(H_ROOM_COUNT):
            rand=0#random.randint(7,10)
            map[y].append(rooms[rand])
            #map[y].append(MapData.fill)

    posX = 0
    posY = 0

    # select a random position in the first row
    startPosition = random.randint(0,H_ROOM_COUNT-1)
    # mark it with an S
    #map[0][startPosition] = MapData.mapStart # "S"
    map[0][startPosition] = "─S─" # rooms[5]
    path.append((0,startPosition))

    # set our current x-position to the startPosition 
    posX = startPosition

    # variable between 1 to 3, to store the direction of the next room
    nextRoom = 0 # 1 left, 2 right, 3 bottom
    # Implementing at least one move per row, to make generation more interesting and preventing long drops
    movedOnce = False
    #movedOnce = True
    # variable to stop the while loop
    finished  = False

    while not finished:
        # very small delay between every iteration to prevent a crash
        #yield(get_tree().create_timer(timer_val), "timeout")
        # first move in every row
        if not movedOnce and posY < V_ROOM_COUNT - 1:
            # check if the current position is in one of the corners
            if posX > 0 and posX < H_ROOM_COUNT - 1:
                # if not choose a random move; 1 left or 2 right
                nextRoom = random.randint(1,2)
                match nextRoom:
                    case 1:
                        posX -= 1
                    case 2:
                        posX += 1

            # if you are in one of the corners, there is only one move you can do
            elif posX == 0:
                posX += 1
            elif posX == H_ROOM_COUNT -1:
                posX -= 1

            # setting the next room to a 1 (left-right room)
            map[posY][posX] =  rooms[1]
            path.append((posY,posX))

            # after one Move per row you could go down a layer
            movedOnce = True


    # second, third... move
        elif movedOnce and posY < V_ROOM_COUNT - 1:
            # if you are in one of the corners you must go down
            if posX == 0 or posX == H_ROOM_COUNT - 1:
                # changing the current room into a 2 (left-right-bottom room)
                map[posY][posX] =rooms[2]
                path.append((posY,posX))
                # then set to a 'top corner piece'
                # However, if the piece above this potential corner piece is already a top corner piece
                # then this piece needs to be a three way T(LR)B  
                if posX==0:
                    map[posY][posX] =rooms[8]
                if posX == H_ROOM_COUNT - 1:
                    map[posY][posX] =rooms[7]
                      
                # go down a row
                path.append((posY,posX))
                posY += 1

                # the next room below the current room must be a 3 (left-right-top room)
                map[posY][posX] = rooms[3]
                # OR a 'bottom corner piece'
                if posX==0:
                    map[posY][posX] =rooms[9]
                if posX == H_ROOM_COUNT - 1:
                    map[posY][posX] =rooms[10]  
            
                

                # making sure you have to do at least one move per row
                path.append((posY,posX))
                movedOnce = False


            # else you are in the center and could do a move to the side
            else:
                # to the side (1) or down (2)
                nextRoom = random.randint(1,2)
                
                # move sideways
                if nextRoom == 1:
                    # check if the room left to the current position is free
                    if map[posY][posX-1] == rooms[0]:
                        # move to the left side
                        posX -= 1
                        # setting the next room to a 1 (left-right room)
                        map[posY][posX] =  rooms[1]
                        path.append((posY,posX))
                        # At this point we should loop / call a function to add room items?

                    # else the room to the right must be free
                    else:
                        # move to the right side
                        posX += 1
                        # setting the next room to a 1 (left-right room)
                        map[posY][posX] =  rooms[1]
                        path.append((posY,posX))
                        # At this point we should loop / call a function to add room items?
                
                # move down
                else:
                    # changing the current room into a 2 (left-right-bottom room)
                    map[posY][posX] = rooms[2]


                    # go down a row
                    path.append((posY,posX))
                    posY += 1

                    # the next room below the current room must be a 3 (left-right-top room)
                    map[posY][posX] = rooms[3]

                    # making sure you have to do at least one move per row
                    path.append((posY,posX))
                    movedOnce = False


        # last step (bottom row)
        else:
            # check if the current position is in one of the corners
            if posX > 0 and posX < H_ROOM_COUNT - 1:
                # if not choose a random move; 1 left or 2 right 3 place the exit
                nextRoom = random.randint(1,3)
                # need to check if room was already set to 3
                # if map[posY][posX] == rooms[3]:
                #     pass
                #     print(f"room set to {rooms[3]}  at x:{posX+1},y:{posY+1}  ")
                #     #nextRoom=4
                #     map[posY][posX] = rooms[3]
                #     posX += 1
            #else:
                match nextRoom:
                    case 1:
                        posX -= 1
                        # setting the next room to a 1 (left-right room)
                        # need to check if room was already set to 3
                        if map[posY][posX] == rooms[3]:
                            map[posY][posX] = rooms[3]
                        else:
                            map[posY][posX] = rooms[1]
                        path.append((posY,posX))
                    case 2:
                        posX += 1
                        # setting the next room to a 1 (left-right room)
                        #map[posY][posX] = MapData.mapLRT # rooms[1]
                        if map[posY][posX] == rooms[3]:
                            map[posY][posX] = rooms[3]
                        else:
                            map[posY][posX] = rooms[1]
                        path.append((posY,posX))
                    case 3:
                        #map[posY][posX] = MapData.mapEnd # "E"
                        map[posY][posX] = "─E─" #rooms[6]
                        #end the loop
                        path.append((posY,posX))
                        finished = True
                            
            # if you are not in one of the corners place the exit
            else:
                #map[posY][posX] =  MapData.mapEnd # "E"
                map[posY][posX] =   "─E─" #rooms[6]

                #end the loop
                path.append((posY,posX))
                finished = True


    # print the map out 
    # for d in range(V_ROOM_COUNT):
    #     print(map[d])

    # Remove duplicates
    path=(list(dict.fromkeys(path)))

    return map,path


H=4
V=4

rooms=[
    " - ", # 0
    "───", # 1
    "─┬─", # 2
    "─┴─", # 3
    "─┼─", #  4
    " ─", # 5
    "─ ", # 6
    "─┐ ", # 7
    " ┌─", # 8
    " └─", # 9
    "─┘ ", # 10
        ]


level,path=generatePath(H,V,rooms)




for x in range(V):
    for y in range(H):
        temp =(x,y)
        if temp in path:
            print(Fore.GREEN + level[x][y],end="")
        else:
            # exclude_this = [5,6,7,8,9]
            # exclude_this = [0]
            # my_random_int = choice(list(set(range(1, 10)) - set(exclude_this)))
            # level[x][y]=rooms[my_random_int]
            print(Fore.RED + level[x][y],end="")
        if y >=(H-1):
            print()
    
print(path)




'''
if not in path
    if is edge the 

'''











   #print(Fore.GREEN + level[x][0] + level[x][1] + level[x][2] + level[x][3]) 

# print the map out 

# for h in range(V):
#     print(f'{level[h]}')

# print(level[0][0])   



# for y in range(V):
#    # print("\n")
#     row=[]
#     for x in range(H):
#         row.append(level[y][x])
#         #print(level[y][x])
#     print(row)

# print(level[0][0] + level[0][1] + level[0][2] + level[0][3])
# print(level[1][0] + level[1][1] + level[1][2] + level[1][3])
# print(level[2][0] + level[2][1] + level[2][2] + level[2][3])
# print(level[3][0] + level[3][1] + level[3][2] + level[3][3])
