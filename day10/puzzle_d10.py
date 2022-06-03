points_map = { ')': 3, ']': 57, '}': 1197, '>': 25137, }

def match_parenthesis(c1, c2):
  if c1 == '(' and c2 == ')': return True
  if c1 == '[' and c2 == ']': return True
  if c1 == '{' and c2 == '}': return True
  if c1 == '<' and c2 == '>': return True
  return False

def matching_parenthesis(c):
  if c == '(': return ')', 1
  if c == '[': return ']', 2
  if c == '{': return '}', 3
  if c == '<': return '>', 4


total_corrupt_points = 0
total_autocomplete_points = []
with open("input.txt") as f:
  for line in f.readlines():
    corrupted_line = False
    pairs_counter = []
    autocomplete_points = 0
    for c in line[:-1]:
      if c in ['(', '[', '{', '<']:
        pairs_counter.append(c)
      else:
        if not match_parenthesis(pairs_counter[-1], c):
          total_corrupt_points += points_map[c]
          corrupted_line = True
          break
        else:
          pairs_counter.pop()
    if not corrupted_line:
      while pairs_counter :
        c, p = matching_parenthesis(pairs_counter[-1])
        pairs_counter.pop()
        autocomplete_points = autocomplete_points * 5 + p
      total_autocomplete_points.append(int(autocomplete_points))

  print(total_corrupt_points)
  print(sorted(total_autocomplete_points, reverse=True)[int(len(total_autocomplete_points)/2)])
