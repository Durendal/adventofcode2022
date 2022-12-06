data = open('input.txt', 'r').read()
a = [i for i in range(len(data)-14) if len(set(data[i:i+14])) == 14]
print(a[0]+14)
