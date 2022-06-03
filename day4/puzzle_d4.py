inputs = ""
boards = []
boards_done = []

def create_boards():
  with open("input.txt") as file:
    global inputs
    global boards
    global boards_done

    inputs = file.readline().split(" ")
    print(inputs)
    file.readline()
    idx = 0
    last_line = inputs
    while last_line:
      boards.append([file.readline().split(), 
                     file.readline().split(), 
                     file.readline().split(), 
                     file.readline().split(),
                     file.readline().split()])
      boards_done.append([[False,False,False,False,False],
                          [False,False,False,False,False],
                          [False,False,False,False,False],
                          [False,False,False,False,False],
                          [False,False,False,False,False]])
      last_line = file.readline()
      idx +=1

def winner_board():
  global boards_done
  # check rows
  for idx in range(len(boards_done)):
    for i in range (5):
      if boards_done[idx][i][0] and boards_done[idx][i][1] and boards_done[idx][i][2] and boards_done[idx][i][3] and boards_done[idx][i][4]:
        return idx
  #check columns
  for idx in range(len(boards_done)):
    for i in range(5):
      if boards_done[idx][0][i] and boards_done[idx][1][i] and boards_done[idx][2][i] and boards_done[idx][3][i] and boards_done[idx][4][i]:
        return idx
  
  return None

def print_boards():
  global boards_done
  for idx in range(len(boards_done)):
    all_elem_are_true = True
    for i in range(5):
      print("[")
      for j in range(5):
        print(boards_done[idx][i][j], end='')
      print("]")

def part1():
  idx = 0
  for idx in range(int(len(inputs)/5)):
    for b_idx in range(len(boards)):
      for j in range(5):
        for i in range(5):
          try:
            position = boards[b_idx].index(inputs[idx+i])
            boards_done[idx][j][position] = True
          except ValueError:
            print("", end="")

create_boards()

print(part1)