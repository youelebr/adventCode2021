DEBUG = 0
NBSTEPS = 40

polymer_template = ""
polymerization = {}
with open("input.txt") as f:
  polymer_template = f.readline().strip('\n')
  f.readline()
  for line in f.readlines():
    polymerization[line.split(" -> ")[0]] = line.strip('\n').split(" -> ")[1]


print(polymer_template)
print(polymerization)

for iter in range(NBSTEPS):
  print(iter, len(polymer_template))
  next_polymer = ""
  for idx in range(len(polymer_template)-1):
    next_polymer += polymer_template[idx] + polymerization[polymer_template[idx]+polymer_template[idx+1]]
  next_polymer += polymer_template[-1]
  polymer_template = next_polymer

print("Go counting... ")
max = 0
min = len(polymer_template)
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
  count = polymer_template.count(c)
  if count > max:
    max = count
  if count < min and count != 0:
    min = count

print(min, max, max - min)