# proc_gen


These are some Python scripts for procedural generation

#### procedural_generation.py 
Is loosely based on Spelunky style map / map path generation for 2d platform games. Primarily its job is to guarantee that a path from [S]tart to [E]nd is viable. 

It's ugly, but it's pretty well documented.

You feed it the [H]orizontal and [V]ertical size of the level you'd like to design and it spits out a text-based picture in the console. The way I used this is that each entry in the map array would correspond to a tilemap based level. 

It also spits out an array with the coordinates of the current path. This array is useful for ensuring that important items are guaranteed to be accessible to players. You wouldn't want the *Big Key, Final Boss, Rare Item* to spawn outside of that array -otherwise the players may never solve or complete the level.

The `procedural_generation.py` script itself has no requirements, however `adv_test.py` will need [Colorama](https://pypi.org/project/colorama/) installed to make the test file look pretty

All you need to do is import the script and run: 

```python

import procedural_generation

level,solution_path=procedural_generation.generatePath()

print(level)
print(solution_path)

```



TO DOs

- Clean up extra comments and debug stuff
- Make it a standalone Python script [main.py]
- More `room` types
- Change `rooms` to a dictionary to make the process easier to understand.
- Better corners and edges
- Better empty room filling / level selections





Map parts:

  ┌── ─┬─ ──┐
  
  │    │    │
  
  ├── ─┼─ ──┤
  
  │    │    │
  
  └── ─┴─ ──┘
