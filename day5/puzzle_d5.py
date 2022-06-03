import numpy as np

total =0

# Set up the grid of 0
grid = np.zeros((1000, 1000))

with open("input.txt") as f:
  for line in f.readlines():
    x1 = int(line.split(" -> ")[0].split(",")[0])
    y1 = int(line.split(" -> ")[0].split(",")[1])
    x2 = int(line.split(" -> ")[1].split(",")[0])
    y2 = int(line.split(" -> ")[1].split(",")[1])

    xmin, xmax = min(x1,x2), max(x1,x2)
    ymin, ymax = min(y1,y2), max(y1,y2)
    
    if x1 == x2:
      for y in range(ymin, ymax+1):
        grid[x1][y] += 1
    
    elif y1 == y2:
      for x in range(xmin, xmax+1):
        grid[x][y1] += 1
    else:
      x_step = np.sign(x2 - x1)
      y_step = np.sign(y2 - y1)
      for x, y in zip(range(x1, x2 + x_step, x_step), range(y1, y2 + y_step, y_step)):
          grid[x, y] += 1

  # Sum all elem > 1 in the final grid
  for i in range(1000):
    for j in range(1000):
      if grid[i][j] > 1:
        total += 1

print(total)