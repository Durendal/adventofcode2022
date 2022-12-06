data = open('input.txt', 'r').read()
for i in range(len(data)-14):
  if len(set(data[i:i+14])) == 14:
    print(i+14)
    break
