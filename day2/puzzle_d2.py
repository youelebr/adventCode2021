with open("input.txt") as file:
    data = list(map(str, file.read().splitlines()))

def part1(data: list[str]):
  hor_pos = 0
  depth_pos = 0
  for info in data:
    direction, x = info.split()
    if direction == "forward":
        hor_pos += int(x)
    if direction == "down":
        depth_pos += int(x)
    if direction == "up":
        depth_pos -= int(x)
  return hor_pos * depth_pos


def part2(data: list[str]):
  hor_pos = 0
  depth_pos = 0
  aim = 0
  for info in data:
    direction, x = info.split()
    if direction == "forward":
        hor_pos += int(x)
        depth_pos += aim * int(x)
    if direction == "down":
        aim += int(x)
    if direction == "up":
        aim -= int(x)

  return hor_pos * depth_pos

print(part1(data))
print(part2(data))