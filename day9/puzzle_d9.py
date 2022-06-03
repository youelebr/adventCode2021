map = []
BOLD = '\033[1m'
WARNING = '\033[93m'
ENDC = '\033[0m'
DEBUG = 0
def split(word):
    #          lvl     visited  min bassin_id
    return [[int(char), False, True, 0] for char in word]

with open("input.txt") as f:
  for line in f.readlines():
    map.append(split(line.strip('\n')))

list_of_minimums = []

# solve part1
def check_min(position_i, position_j):
  map[position_i][position_j][1] = True
  if position_i < len(map)-1:
    if (map[position_i][position_j][0] >= map[position_i+1][position_j][0]):
      map[position_i][position_j][2] = False
      check_min (position_i + 1, position_j)
  if position_j < len(map[position_i])-1:
    if (map[position_i][position_j][0] >= map[position_i][position_j+1][0]):
      map[position_i][position_j][2] = False
      check_min (position_i, position_j + 1)
  if position_i > 0:
    if (map[position_i][position_j][0] > map[position_i-1][position_j][0]):
      map[position_i][position_j][2] = False
  if position_j > 0:
    if (map[position_i][position_j][0] > map[position_i][position_j-1][0]):
      map[position_i][position_j][2] = False


for i in range(len(map)):
  for j in range(len(map[i])):
    if map[i][j][1] == False:
      check_min(i, j)


count = 0
for i in range(len(map)):
  for j in range(len(map[i])):
  #   if map[i][j][1] == False:
  #     print(f"{WARNING}{map[i][j][0]}{ENDC}",end='')
  #   elif map[i][j][2] == True:
  #     count += 1 + map[i][j][0]
  #     print(f"{BOLD}{map[i][j][0]}{ENDC}",end='')
  #   else:
  #     print(map[i][j][0],end='')
  # print('')
    if map[i][j][2] == True:
      count += 1 + map[i][j][0]
print(count)

# solve part2
def draw_bassin(position_i, position_j, bassin_id):
  counter = 1
  assert map[position_i][position_j][3] == 0
  map[position_i][position_j][3] = bassin_id # should be a minimum
  if position_i > 0:
    if (map[position_i-1][position_j][0] != 9 
        and map[position_i-1][position_j][3] != bassin_id):
      counter += draw_bassin (position_i - 1, position_j, bassin_id)

  if position_i < len(map)-1:
    if (map[position_i+1][position_j][0] != 9
        and map[position_i+1][position_j][3] != bassin_id):      
      counter += draw_bassin (position_i + 1, position_j, bassin_id)

  if position_j > 0:
    if (map[position_i][position_j-1][0] != 9
        and map[position_i][position_j-1][3] != bassin_id):
      counter += draw_bassin (position_i, position_j - 1, bassin_id)

  if position_j < len(map)-1:
    if (map[position_i][position_j+1][0] != 9
        and map[position_i][position_j+1][3] != bassin_id):      
      counter += draw_bassin (position_i, position_j + 1, bassin_id)
  return counter

bassin_id = 1
bassins = []
for i in range(len(map)):
  for j in range(len(map[i])):
    if map[i][j][2] == True:
      bassins.append(draw_bassin(i,j, bassin_id))
      bassin_id += 1

# draw bassins
if DEBUG > 0:
  for i in range(len(map)):
    for j in range(len(map[i])):
      if map[i][j][3] != 0:
        print(f"{WARNING}{map[i][j][0]}{ENDC}",end='')
      else:
        print(map[i][j][0],end='')
    print('')

if DEBUG > 0:
  print(bassins)

total = 1
for i in sorted(bassins, reverse=True)[:3]:
  total *= i
print(total)