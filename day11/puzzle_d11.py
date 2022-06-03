map = []

def split(word):
    #          lvl     flashed
    return [[int(char), False] for char in word]

with open("input.txt") as f:
  for line in f.readlines():
    map.append(split(line.strip('\n')))

numer_of_flash = 0

def flush_flash():
  for octos in map:
    for octo in octos:  
      octo[1] = False

# Solve part2
def is_synchro():
  for octos in map:
    for octo in octos:  
      if octo[1] == False:
        return False
  return True

# solve part1
def flash(position_i, position_j):
  global numer_of_flash
  if map[position_i][position_j][1]:
    return
  if map[position_i][position_j][0] < 9:
    map[position_i][position_j][0] += 1
    return
  # Octo flash :
  map[position_i][position_j][1] = True
  map[position_i][position_j][0] = 0
  numer_of_flash += 1

  if position_i < len(map)-1:
    flash(position_i+1, position_j)
    if position_j < len(map[position_i])-1:
      flash(position_i+1, position_j+1)
  if position_j < len(map[position_i])-1:
    flash(position_i, position_j+1)
    if position_i > 0:
      flash(position_i-1, position_j+1)
  
  if position_i > 0:
    flash(position_i-1, position_j)
    if position_j > 0:
      flash(position_i-1, position_j-1)
  if position_j > 0:
    flash(position_i, position_j-1)
    if position_i < len(map)-1:
      flash(position_i+1, position_j-1)

for step in range(1000):
  for i in range(len(map)):
    for j in range(len(map[i])):
      flash(i,j)
  if is_synchro():
    print("SYNCHRO step=", step+1)
    break
  flush_flash()

print(numer_of_flash)
