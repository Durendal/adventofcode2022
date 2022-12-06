data = open('input.txt', 'r').read()
for i in range(len(data)-4):
  if len(set(data[i:i+4])) == 4:
    print(i+4)
    break
