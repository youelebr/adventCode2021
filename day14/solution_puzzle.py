from collections import Counter

with open("input.txt") as file:
    data = file.read().splitlines()
    
template = data[0]
 
rules = [line.replace(" ","").split("->") for line in data[2:]]
 
gen_rules = {rule[0]: [rule[0][0]+rule[1],rule[1]+rule[0][1]] for rule in rules}
 
count_pairs = Counter()
for i in range(len(template)-1):
    count_pairs[template[i:i+2]]+=1

for _ in range(40):
    new_count = Counter()
    for key,val in count_pairs.items():
        new_count[gen_rules[key][0]]+=val
        new_count[gen_rules[key][1]]+=val
    count_pairs=new_count
    
count_char=Counter()
for pair,val in count_pairs.items():
    count_char[pair[0]]+=val
    count_char[pair[1]]+=val

print((count_char.most_common()[0][1]+1)//2- (count_char.most_common()[-1][1]+1)//2)