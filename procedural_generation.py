import random
from random import choice



rooms=[
    " - ", # 0  | Nothing / Empty
    " S ", # 1  | Start
    " E ", # 2  | End
    "───", # 3  | LR
    "─┬─", # 4  | LRB
    "─┴─", # 5  | LRT
    "─┼─", # 6  | LRTB
    " ─", # 7   | R Cave
    "─ ", # 8   | L Cave
    "─┐ ", # 9  | LB
    " ┌─", # 10 | RB 
    " └─", # 11 | RT
    "─┘ ", # 12 | LT
    "─┤", # 13  | LTB
    "├─", # 14  | RTB
        ]


def generatePath(H=4,V=4,rooms=rooms):
    V_ROOM_COUNT=V
    H_ROOM_COUNT=H

    #clear / instantiate the map 
    map = []

    # make an array to store the path points for special items. 
    # A big key needs to spawn in this path
    solution_path = []
    
    # initialize / fill the map array with 0's
    for y in range(V_ROOM_COUNT):
        map.append([])
        for x in range(H_ROOM_COUNT):
            map[y].append(rooms[0])


    posX = 0
    posY = 0

    # select a random position in the first row
    startPosition = random.randint(0,H_ROOM_COUNT-1)
    # mark it with an S
    # Mark it with the first item in your rooms array
    #map[0][startPosition] = MapData.mapStart # "S"

    map[0][startPosition] = rooms[1]
    solution_path.append((0,startPosition))

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
            map[posY][posX] =  rooms[3]
            solution_path.append((posY,posX))

            # after one Move per row you could go down a layer
            movedOnce = True


    # second, third... move
        elif movedOnce and posY < V_ROOM_COUNT - 1:
            # if you are in one of the corners you must go down
            if posX == 0 or posX == H_ROOM_COUNT - 1:
                # changing the current room into a 2 (left-right-bottom room)
                map[posY][posX] =rooms[7]
                solution_path.append((posY,posX))
                # then set to a 'top corner piece'
                # However, if the piece above this potential corner piece is already a top corner piece
                # then this piece needs to be a three way T(LR)B  
                if posX==0:
                    map[posY][posX] =rooms[10]
                if posX == H_ROOM_COUNT - 1:
                    map[posY][posX] =rooms[9]
                      
                # go down a row
                solution_path.append((posY,posX))
                posY += 1

                # the next room below the current room must be a 3 (left-right-top room)
                map[posY][posX] = rooms[5]
                # OR a 'bottom corner piece'
                if posX==0:
                    map[posY][posX] =rooms[11]
                if posX == H_ROOM_COUNT - 1:
                    map[posY][posX] =rooms[12]  
            
                

                # making sure you have to do at least one move per row
                solution_path.append((posY,posX))
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
                        map[posY][posX] =  rooms[3]
                        solution_path.append((posY,posX))
                        # At this point we should loop / call a function to add room items?

                    # else the room to the right must be free
                    else:
                        # move to the right side
                        posX += 1
                        # setting the next room to a 1 (left-right room)
                        map[posY][posX] =  rooms[3]
                        solution_path.append((posY,posX))
                        # At this point we should loop / call a function to add room items?
                
                # move down
                else:
                    # changing the current room into a 2 (left-right-bottom room)
                    map[posY][posX] = rooms[4]


                    # go down a row
                    solution_path.append((posY,posX))
                    posY += 1

                    # the next room below the current room must be a 3 (left-right-top room)
                    map[posY][posX] = rooms[5]

                    # making sure you have to do at least one move per row
                    solution_path.append((posY,posX))
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
                        # need to check if room was already set to 3 ?
                        if map[posY][posX] == rooms[5]:
                            map[posY][posX] = rooms[5]
                        else:
                            map[posY][posX] = rooms[3]
                        solution_path.append((posY,posX))
                    case 2:
                        posX += 1
                        # setting the next room to a 1 (left-right room)
                        if map[posY][posX] == rooms[5]:
                            map[posY][posX] = rooms[5]
                        else:
                            map[posY][posX] = rooms[3]
                        solution_path.append((posY,posX))
                    case 3:
                        map[posY][posX] = rooms[2] # End
                        #end the loop
                        solution_path.append((posY,posX))
                        finished = True
                            
            # if you are not in one of the corners place the exit
            else:
                map[posY][posX] = rooms[2] # End

                #end the loop
                solution_path.append((posY,posX))
                finished = True


    # Remove duplicates from path
    solution_path=(list(dict.fromkeys(solution_path)))

    return map,solution_path


if __name__ == "__main__":
    
    print("\nAutogenerate a 4x4 level map and show the solution_path...\n")
    H=4
    V=4
    level,solution_path=generatePath(H,V,rooms)

    for x in range(V):
        for y in range(H):
            current_room =(x,y)
            if current_room in solution_path:
                print(""+level[x][y]+"" ,end="")
            else:
                print(""+ level[x][y]+"",end="")
            if y >=(H-1):
                print()

    print(f"\nStart to End: {solution_path}\n")





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


