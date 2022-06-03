import numpy as np
DEBUG = 0

max_lines: int = 0
max_rows: int = 0
positions = []
folds = []
with open("input.txt") as f:
  for line in f.readlines():
    if "," in line:
      positions.append([int(line.strip('\n').split(',')[1]), int(line.strip('\n').split(',')[0])])
      if max_lines < positions[-1][0]:
        max_lines = positions[-1][0]
      if max_rows < positions[-1][1]: 
        max_rows = positions[-1][1]
    elif "fold along " in line:
      folds.append(line.strip('\n').split("fold along ")[1])

map = np.zeros((max_lines + 1, max_rows + 1), dtype=int)

def fill_map_with_positions():
  for pos in positions:
    map[pos[0]][pos[1]] = 1

def pretty_print():
  count = 0
  for i in range(len(map)):
    for j in range(len(map[i])):
      if map[i][j] > 0:
        count += 1
        print("#", end='')
      else:
        print('.', end='')
    print()
  return count

def fold():
  global map
  for f in folds:
    line_to_fold = int(f.split("=")[1])
    way_to_fold = f.split("=")[0]
    print(way_to_fold, "->", line_to_fold)
    if way_to_fold == "y":
      ii = 0
      for i in reversed(range(line_to_fold+1, len(map))):
        map[ii] += map[i]
        ii += 1
        map = np.delete(map, (i), axis=0)
      map = np.delete(map, (line_to_fold), axis=0)
      if DEBUG > 0:
        pretty_print()
    
    if way_to_fold == "x":
      for map_i in map:
        jj = 0
        for j in reversed(range(line_to_fold+1, len(map[0]))):
          map_i[jj] += map_i[j]

          jj += 1
      for i in reversed(range(line_to_fold, len(map[0]))):
        map = np.delete(map, (i), axis=1)
      if DEBUG > 0:
        pretty_print()
      

fill_map_with_positions()
# pretty_print()
fold()
print(pretty_print())
