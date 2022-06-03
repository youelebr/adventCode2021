with open("input.txt") as file:
  data = list(map(str, file.read().splitlines()))

def more_or_less_bit(data: list[str], idx: int):
  nbOf0 = 0; nbOf1 = 0
  for elem in data:
    if elem[idx] == '0':
      nbOf0 += 1
    else:
      nbOf1 += 1
  if nbOf0 > nbOf1:
    return '0', '1'
  else:
    return '1', '0'

def part1(data: list[str]):
  gamma = ""; espilon = ""
  for idx in range(len(data[0])):
    m, l = more_or_less_bit(data, idx)
    gamma += m
    espilon += l
  return int(gamma, 2) * int(espilon, 2)

def get_words_starting_with(data: list[str], idx: int, letter: str):
  return [elem for elem in data if elem[idx] == letter]

def part2(data: list[str]):
  idx = 0
  oxygen_generator_list = data
  CO2_scrubber_list = data

  while (len(oxygen_generator_list) > 1 or len(CO2_scrubber_list) > 1) and idx < len(data[0]) :
    oxygen_generator_rating_bc, _  = more_or_less_bit(oxygen_generator_list, idx)
    _, CO2_scrubber_rating_bc = more_or_less_bit(CO2_scrubber_list, idx)
    if len(oxygen_generator_list) > 1:
      oxygen_generator_list = get_words_starting_with(oxygen_generator_list, idx, oxygen_generator_rating_bc)
    if len(CO2_scrubber_list) > 1:
      CO2_scrubber_list = get_words_starting_with(CO2_scrubber_list, idx, CO2_scrubber_rating_bc)
    idx += 1
  return int(oxygen_generator_list[0], 2) * int(CO2_scrubber_list[0], 2)

print(part1(data))
print(part2(data))