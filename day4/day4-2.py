data = [i.strip() for i in open('input.txt', 'r').readlines() if i != '\n']
count = 0
for row in data:
  line = row.split(',')
  l1, r1 = list(map(int, line[0].split("-")))
  l2, r2 = list(map(int, line[1].split("-")))
  s1 = set(range(l1, r1+1))
  s2 = set(range(l2, r2+1))
  if s1.intersection(s2): 
    count += 1
print(count)
