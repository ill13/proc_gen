# proc_gen


These are some Python scripts for procedural generation

#### `gen.py` 
Is loosely based on Spelunky style map / map path generation for 2d platform games. Primarily its job is to guarantee that a path from [S]tart to [E]nd is viable. 

It's ugly, but it's pretty well documented.

You feed it the [H]orizontal and [V]ertical size of the level you'd like to design and it spits out a text-based picture in the console. The way I used this is that each entry in the map array would correspond to a tilemap based level. 

It also spits out an array with the coordinates of the current path. This array is useful for ensuring that important items are guaranteed to be accessible to players. You wouldn't want the *Big Key, Final Boss, Rare Item* to spawn outside of that array -otherwise the players may never solve or complete the level  

TO DOs

- Clean up extra comments and debug stuff
- Make it a standalone Python script [main.py]
- More `room` types
- Better corners and edges
- Better empty room filling / level selections
