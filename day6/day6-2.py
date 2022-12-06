data = open('input.txt', 'r').read()
print([i for i in range(len(data)-14) if len(set(data[i:i+14])) == 14][0]+14)
