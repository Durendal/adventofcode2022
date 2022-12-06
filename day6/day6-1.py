data = open('input.txt', 'r').read()
print([i for i in range(len(data)-4) if len(set(data[i:i+4])) == 4][0]+4)
