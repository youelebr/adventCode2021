crabs_positions = []
with open("input.txt") as f:
  crabs_positions = list(map(int, f.readline().split(",")))  

max_pos = max(crabs_positions)
## part 1
def part1():
  min_fuel_spend = 9999999999999
  for i in range(max_pos):
    fuel_to_spend = 0
    for j in range(len(crabs_positions)):
      fuel_to_spend += abs(crabs_positions[j] - i)
    if fuel_to_spend < min_fuel_spend:
      min_fuel_spend = fuel_to_spend
  return min_fuel_spend
print(part1())

## part 2
def part2():
  min_fuel_spend = 9999999999999
  for i in range(max_pos):
    fuel_to_spend = 0
    for j in range(len(crabs_positions)):
      t = abs(crabs_positions[j] - i)
      fuel_to_spend += int(t * (t+1) / 2)
    if fuel_to_spend > min_fuel_spend:
      return min_fuel_spend
    min_fuel_spend = fuel_to_spend
  return min_fuel_spend
print(part2())