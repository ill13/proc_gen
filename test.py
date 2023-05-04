import procedural_generation as gen

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
level,solution_path=gen.generatePath(H,V,rooms)

for x in range(V):
    for y in range(H):
        current_room =(x,y)
        if current_room in solution_path:
            print(Fore.GREEN + ""+level[x][y]+"",end="")
        else:
            print(Fore.RED + ""+ level[x][y]+"",end="")
        if y >=(H-1):
            print()

print(f"\nStart to End: {solution_path}\n")
