from numpy.lib.function_base import delete

DEBUG = 1
map = {}
if DEBUG > 0:
  list_of_solution = []
numberOfSolution = 0

with open("input.txt") as f:
  for line in f.readlines():
    left, right = line.strip('\n').split('-')[0],line.strip('\n').split('-')[1]
    if left not in map:
      map[left] = [right]
    else:
      map[left].append(right)
    if right not in map:
      map[right] = [left]
    else:
      map[right].append(left)

# print('-----------')
# print(map)
# print('-----------')

def browse_graph(node: str, listOfVisitedSmallCave, path, joker):
  global numberOfSolution
  path += node + ","
  for n in map[node]:
    if DEBUG > 1:
      print("Current Node:", node, "see ", n,  "? List of small case visited:", listOfVisitedSmallCave, " previous path= ", path, " To visit:", map[node])
    if n == "end":
      if DEBUG > 0:
        list_of_solution.append(path + "end")
      numberOfSolution += 1
    
    elif n in listOfVisitedSmallCave and joker == False:
      browse_graph(n, listOfVisitedSmallCave[:], path, True)
    
    elif n not in listOfVisitedSmallCave:
      copyOf_lofsc = listOfVisitedSmallCave[:]
      if n[0].islower():
        copyOf_lofsc.append(n)
      browse_graph(n, copyOf_lofsc, path, joker)

browse_graph("start", ["start"], "", False)

if DEBUG > 0:
  for sol in reversed(list_of_solution):
    if sol[-3:] != "end":
      list_of_solution.remove(sol)
  print(len(list_of_solution))
  if DEBUG > 1:
    print(list_of_solution)

print(numberOfSolution)