
with open("input.txt") as file:
    data = list(map(int, file.read().splitlines()))

def part1(data: list[int]):
  sum = 0
  for idx in range(len(data[1:])):
    if data[idx] < data[idx + 1]:
      sum += 1
  return sum

def part2(data: list[int]) -> int:
    windows = [sum(data[index:index + 3]) for index in range(len(data[1:-1]))]
    return part1(windows)

print(part1(data))
print(part2(data))
