

hexa = {
  "0": "0000",
  "1": "0001",
  "2": "0010",
  "3": "0011",
  "4": "0100",
  "5": "0101",
  "6": "0110",
  "7": "0111",
  "8": "1000",
  "9": "1001",
  "A": "1010",
  "B": "1011",
  "C": "1100",
  "D": "1101",
  "E": "1110",
  "F": "1111"
}

# with open("input.txt") as f:
#   data = f.readline().strip('\n')
data = "8A004A801A8002F478"
data = "".join([hexa[c] for c in data])
print(data)

values = []

def parse_packet(data, pos):
  global values
  print(pos,"/",len(data))
  version = int(data[pos:pos+3],2)
  typeid = int(data[pos+3:pos+6],2)
  print("------------")
  print("version:", data[pos:pos+3], "=", version, " typeid:", data[pos+3:pos+6], "=", typeid)
  pos = pos+6

  if typeid == 4:
    print("read 5bits by five bits until first bit of these five bits is 0")
    value = 0
    while data[pos] == '1':
      pos+=5
    pos+=5
    print("return ", version, pos)
    return version, pos
  else:
    values = []
    ltid = data[pos]
    print("length type id = ", data[pos])
    pos += 1
    if ltid == '0':
      total_length = int(data[pos:pos+15], 2)
      pos += 15
      final_pos = pos + total_length
      while pos != final_pos:
          version, pos = parse_packet(data, pos)
          values.append(version)

    elif ltid == '1':
      nb_subpacket = int(data[pos:pos+11], 2)
      pos += 11
      print("nb_subpacket=",nb_subpacket)
      for _ in range(nb_subpacket):
        version, pos = parse_packet(data, pos)
        values.append(version)

    return version, pos

print(parse_packet(data, 0))
print("values=", values)