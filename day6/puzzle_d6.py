jellyfishes_dict = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
# nb_of_day = 80
nb_of_day = 256

with open("input.txt") as f:
  jellyfishes_tmp = list(map(int, f.readline().split(",")))  

for i in range(len(jellyfishes_tmp)):
  jellyfishes_dict[jellyfishes_tmp[i]] += 1

for d in range(nb_of_day):
  jellyfishes_dict[0], jellyfishes_dict[1], jellyfishes_dict[2], jellyfishes_dict[3], jellyfishes_dict[4], jellyfishes_dict[5], jellyfishes_dict[6], jellyfishes_dict[7], jellyfishes_dict[8] = jellyfishes_dict[1], jellyfishes_dict[2], jellyfishes_dict[3], jellyfishes_dict[4], jellyfishes_dict[5],jellyfishes_dict[6], jellyfishes_dict[7]+jellyfishes_dict[0], jellyfishes_dict[8], jellyfishes_dict[0]

print(sum(jellyfishes_dict.values()))