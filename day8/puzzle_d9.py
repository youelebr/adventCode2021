map = []
  
with open("input.txt") as f:
  map.append(list(map(int,list(f.readlines()))))

for i in range(len(map)):
  for j in range(len(map[0])):
    print(map[i][j],end=' ')