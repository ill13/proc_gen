import procedural_generation
import random

from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)

rooms=[
    "--", # 0
    "SS", # 1
    "EE", # 2
    "03", # 3
    "04", #  4
    "05", # 5
    "06", # 6
    "07", # 7
    "08", # 8
    "09", # 9
    "10", # 10
    "11", # 11
    "12", # 12
        ]


# Adding some text padding for presentation
rooms= list(map(lambda orig_string: " " + orig_string + " ", rooms))

H=6
V=6
seed= random.random()

level,solution_path=procedural_generation.generatePath(H,V,seed=seed)

for x in range(V):
    for y in range(H):
        current_room =(x,y)
        if current_room in solution_path:
            print(Back.GREEN + Fore.BLACK +level[x][y],end="")
        else:
            print(Back.YELLOW + Fore.GREEN + level[x][y],end="")
        if y >=(H-1):
            print()

print(f"\nStart to End: {solution_path}\n")
