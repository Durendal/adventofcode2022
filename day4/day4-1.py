data = [i.strip() for i in open('input.txt', 'r').readlines() if i != '\n']
count = 0
for row in data:
  line = row.split(',')
  l1, r1 = map(int, line[0].split("-"))
  l2, r2 = map(int, line[1].split("-"))
  if (l1 >= l2 and r1 <= r2) or (l1 <= l2 and r1 >= r2):
    count += 1
print(count)
