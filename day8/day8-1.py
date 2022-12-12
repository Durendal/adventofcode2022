data = [list(i.strip()) for i in open('input1.txt', 'r').readlines()]
counter = 0
for i in range(1, len(data)-1):
  for j in range(1, len(data[i])-1):
    tree = data[i][j]
    left = max(data[i][:j])
    right = max(data[i][j+1:])
    up = max([data[x][j] for x in range(i)])
    down = max([data[x][j] for x in range(i+1, len(data))])
    if tree > left or tree > right or tree > up or tree > down:
      counter += 1
print(counter+(len(data)*2)+(len(data[0])*2)-4)
