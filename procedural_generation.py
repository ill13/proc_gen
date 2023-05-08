import random
from random import choice



rooms=[
    " - ", # 0  | Nothing / Empty
    " S ", # 1  | Start
    " E ", # 2  | End
    "───", # 3  | LR
    "─┬─", # 4  | LRB
    "─┴─", # 5  | LRT
    "─┼─", # 6  | LTRB
    " ─", # 7   | R Cave
    "─ ", # 8   | L Cave
    "─┐ ", # 9  | LB
    " ┌─", # 10 | RB 
    " └─", # 11 | RT
    "─┘ ", # 12 | LT
    "─┤", # 13  | LTB
    "├─", # 14  | RTB
        ]


rooms={
    "Empty":"000",
    "Start":"─S─",
    "End":"─E─",
    "LR":"───",
    "LRB":"─┬─",
    "LTR":"─┴─",
    "LTB":"─┤ ",
    "TRB": " ├─",
    "LTRB":"─┼─",
    "RB":" ┌─",
    "TR":" └─",
    "LB":"─┐ ",
    "LT":"─┘ ",
    "LCave":" X─",
    "RCave":"─X ",
    "Dummy":"DDD"
}

def generatePath(H=4,V=4,rooms=rooms,seed=10):

    random.seed(seed)
    
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
            map[y].append(rooms["Empty"])


    posX = 0
    posY = 0

    # select a random position in the first row
    startPosition = random.randint(0,H_ROOM_COUNT-1)
    # mark it with an S
    map[0][startPosition] = rooms["Start"]
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
            map[posY][posX] =  rooms["LR"]
            solution_path.append((posY,posX))

            # after one Move per row you could go down a layer
            movedOnce = True


    # second, third... move
        elif movedOnce and posY < V_ROOM_COUNT - 1:
            # if you are in one of the corners you must go down
            if posX == 0 or posX == H_ROOM_COUNT - 1:
                # changing the current room into a 2 (left-right-bottom room)
                map[posY][posX] =rooms["LRB"]
                solution_path.append((posY,posX))
                # then set to a 'top corner piece'
                # However, if the piece above this potential corner piece is already a top corner piece
                # then this piece needs to be a three way T(LR)B  
                # top row: These should always be RB or LB 
                if posX==0:
                    map[posY][posX] =rooms["RB"]
                if posX == H_ROOM_COUNT - 1:
                    map[posY][posX] =rooms["LB"]
                      
                # go down a row
                solution_path.append((posY,posX))
                posY += 1

                # the next room below the current room must be a 3 (left-right-top room)
                map[posY][posX] = rooms["LTR"]
                # OR a 'bottom corner piece', if the position is 0 or max
                if posX==0:
                    map[posY][posX] =rooms["TR"]
                if posX == H_ROOM_COUNT - 1:
                    map[posY][posX] =rooms["LT"]  
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
                    if map[posY][posX-1] == rooms["Empty"]:
                        # move to the left side
                        posX -= 1
                        # setting the next room to a 1 (left-right room)
                        map[posY][posX] =  rooms["LR"]
                        solution_path.append((posY,posX))
                        # At this point we should loop / call a function to add room items?

                    # else the room to the right must be free
                    else:
                        # move to the right side
                        posX += 1
                        # setting the next room to a 1 (left-right room)
                        map[posY][posX] =  rooms["LR"]
                        solution_path.append((posY,posX))
                        # At this point we should loop / call a function to add room items?
                
                # move down
                else:
                    # changing the current room into a 2 (left-right-bottom room)
                    map[posY][posX] = rooms["LRB"]


                    # go down a row
                    solution_path.append((posY,posX))
                    posY += 1

                    # the next room below the current room must be a 3 (left-top-right room)
                    map[posY][posX] = rooms["LTR"]

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
                        if map[posY][posX] == rooms["LTR"]:
                            map[posY][posX] = rooms["LTR"]
                        else:
                            map[posY][posX] = rooms["LR"]
                        solution_path.append((posY,posX))
                    case 2:
                        posX += 1
                        # setting the next room to a 1 (left-right room)
                        if map[posY][posX] == rooms["LTR"]:
                            map[posY][posX] = rooms["LTR"]
                        else:
                            map[posY][posX] = rooms["LR"]
                        solution_path.append((posY,posX))
                    case 3:
                        map[posY][posX] = rooms["End"] # End
                        #end the loop
                        solution_path.append((posY,posX))
                        finished = True
                            
            # if you are not in one of the corners place the exit
            else:
                map[posY][posX] = rooms["End"] # End

                #end the loop
                solution_path.append((posY,posX))
                finished = True


    # Remove duplicates from path
    solution_path=(list(dict.fromkeys(solution_path)))


    # Since the solution is complete, we should add the filler rooms here
    # Cycle through all items in map 
    # if we find  LTR or a LRB 
    # then look left, if left ="Empty" the add a random 
    # Or maybe run this procedure again but ignore Start and End?
    map=placeExtraRooms(H,V,rooms,map)


    return map,solution_path


def placeExtraRooms(H=4,V=4,rooms=rooms,map=map,seed=10):
    # looping tough the 2D Array

    random.seed(seed)
    
    V_ROOM_COUNT=V
    H_ROOM_COUNT=H

    for y in range(V_ROOM_COUNT):
        for x in range(H_ROOM_COUNT):
            # again a small delay to prevent a crash
            #yield(get_tree().create_timer(timer_val), "timeout")

            #if the current room is "Empty" it could be replaced
            if map[y][x] == rooms["Empty"]:
                #map[y][x] = rooms["LR"]
                # choose a random number between 1 and 10 (change the 3, to change the probabilities; currently 1/3)
                fillRooms = random.randint(1,3)
                print(f" x={x} y={y} case={fillRooms}")
                match fillRooms:
                    # just place a left right room 
                    case 1:
                        map[y][x] = rooms["LR"]
                    # place a LRB room
                    case 2:
                        # if you are on the left edge, don't place a room that can exit to the left
                        if x == 0:
                            map[y][x] = rooms["LCave"]
                        # check if you are not in the bottom row
                        if y < V_ROOM_COUNT - 1:
                            # if not in bottom row check if the room below the current position is already a left right bottom room
                            if map[y+1][x] == rooms["LRB"]:
                                # if the room below is already a 2, change it to a 4 (left-right-bottom-top room)
                                map[y+1][x] = rooms["LTRB"] 
                                # Now set the current room to a LRB
                                map[y][x] = rooms["LRB"] 
                        else:
                            # if you are in the bottom row, just place a 2 (left-right-bottom room)
                            if x == 0:
                                map[y][x] = rooms["LCave"] #
                            else:
                                map[y][x] = rooms["LR"] 
                        
                        #map[y][x] = rooms["Dummy"]
                    # place a LTR room
                    case 3:
                        # check if you are in the top row
                        if y > 0:
                            # if not in top row check if the room above the current position is already a LTR room
                            if map[y-1][x] == rooms["LTR"]:
                                # if the room above is already a LTR, then change that room to a LTRB
                                map[y-1][x] =rooms["LTRB"]
                                # set the current room to a 3
                                map[y][x] = rooms["LTR"] 
                        else:
                            # if you are in the top row, just place an LR
                            map[y][x] = rooms["LR"]

            # Finally, if a room is on either edge and is a LR
            # Then change it to a Cave
            # Shouldn't need to verify this against the solution path
            if x == 0:
                #if map[y][x] == rooms["LR"]:
                if not map[y][x] == rooms["End"]:
                    if map[y][x] == rooms["LR"]:
                        map[y][x] = rooms["LCave"]
            if x == H_ROOM_COUNT - 1:
                if not map[y][x] == rooms["End"]:
                    if map[y][x] == rooms["LR"]:
                        map[y][x] = rooms["RCave"]
            #     
    return map


if __name__ == "__main__":
    
    print("\nAutogenerate a 4x4 level map and show the solution_path...")
    print("Using a random seed\n")
    H=4
    V=4
    level,solution_path=generatePath(H,V,rooms,seed=random.random() )

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