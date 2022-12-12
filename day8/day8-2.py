def check_side(tree, data):
  side = []
  for i in range(len(data)):
    side.append(data[i])
    if tree <= data[i]:
      break
  return side

data = [list(i.strip()) for i in open('input.txt', 'r').readlines()]
views = []
for i in range(len(data)):
  for j in range(len(data[i])):
    tree = data[i][j]
    left = check_side(tree, data[i][:j][::-1])
    right = check_side(tree, data[i][j+1:])
    up = check_side(tree, [data[x][j] for x in range(i)][::-1])
    down = check_side(tree, [data[x][j] for x in range(i+1, len(data))])
    views.append(len(left)*len(up)*len(right)*len(down))

print(max(views))

