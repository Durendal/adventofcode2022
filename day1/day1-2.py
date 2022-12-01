
data = open('input1.txt', 'r').read()
data = [i for i in data.split("\n\n")]
data = [j.split("\n") for j in data]
del data[-1][-1]
sums = [sum([int(j) for j in data[i] if j != '']) for i in range(len(data))]
t = 0
for i in range(3):
  s = max(sums)
  t += s
  sums.remove(s)
  
print(t)

