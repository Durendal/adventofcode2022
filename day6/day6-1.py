data = open('input.txt', 'r').read()
a = [i for i in range(len(data)-4) if len(set(data[i:i+4])) == 4]
print(a[0]+4)
