# answer for
# https://stackoverflow.com/questions/77071301/how-would-i-write-a-program-that-makes-a-pattern-like-the-one-below-based-on-h/77071538#77071538

import math

height = 9
length = height * 3

# calculating the number of tile rows above and below the name row
outside_rows = math.floor(height/2)

# building rows above the name row
for n in range(0,outside_rows):
    tile_sections = 2 * n + 1
    background_length = int((length - tile_sections * 3) / 2)
    print("-" * background_length, "+|+" * tile_sections, "-" * background_length)

# you can print your named row here
print("")

# building rows below the name row
for n in range(outside_rows-1, -1, -1):
    tile_sections = 2 * n + 1
    background_length = int((length - tile_sections * 3) / 2)
    print("-" * background_length, "+|+" * tile_sections, "-" * background_length)

