
count = 0
with open("input.txt") as f:
  segments_lines = list(f.readlines())
  
  for line in segments_lines:
    line = line[:-1]
    for segment in line.split("|")[-1].split(" "):
      if len(segment) in [2,4,3,7]: # 1
          count += 1
#part 1
print(count)

original_wires = { 'a': 8, 'b': 6, 'c': 8, 'd': 7, 'e': 4, 'f': 9, 'g': 7, }
with open("input.txt") as f:
  segments_lines = list(f.readlines())
  total = 0
  for line in segments_lines:
    wire_correction = {}
    inputs = line.split("|")[0].split()
    outputs = line.split("|")[-1].split()
    wire_input = {c: sum(c in cset for cset in inputs) for c in "abcdefg"}
    one=0
    seven=0
    for i in range(len(inputs)):
      if len(inputs[i]) == 2:
        one = i
      if len(inputs[i]) == 3:
        seven = i

    for c, l in wire_input.items():
      if l == 6:
          wire_correction['b'] = c
      elif l == 4:
          wire_correction['e'] = c
      elif l == 9:
          wire_correction['f'] = c
      elif l == 8:
        if c in inputs[seven] and c not in inputs[one]:
          wire_correction['a'] = c
        else:
          wire_correction['c'] = c
    
    output = ''
    for n in outputs:
        if len(n) == 2:
            output+='1'
        elif len(n) == 3:
            output+='7'
        elif len(n) == 4:
            output+='4'
        elif len(n) == 7:
            output+='8'
        if len(n) == 5:
            if wire_correction["c"] in n and wire_correction["f"] in n:
                output+='3'
            elif wire_correction["c"] in n:
                output+='2'
            else:
                output+='5'
        elif len(n) == 6:
            if wire_correction["c"] in n and wire_correction["e"] in n:
                output+='0'
            elif wire_correction["c"] in n:
                output+='9'
            else:
                output+='6'
    total += int(output)
  #part 2
  print(total)