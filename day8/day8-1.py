data = [list(i.strip()) for i in open('input.txt', 'r').readlines()]
counter = 0
for i in range(1, len(data)-1):
  for j in range(1, len(data[i])-1):
    tree = data[i][j]
    if (
      tree > max(data[i][:j]) 
      or tree > max(data[i][j+1:]) 
      or tree > max([data[x][j] for x in range(i)]) 
      or tree > max([data[x][j] for x in range(i+1, len(data))])
    ):
      counter += 1
print(counter+(len(data)*2)+(len(data[0])*2)-4)
