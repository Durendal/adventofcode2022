data = [i.strip() for i in open('input.txt', 'r').readlines()]
sums = [0]*len(data)

for i in range(len(data)):
  separator = len(data[i]) // 2
  m = list(set(data[i][:separator]).intersection(data[i][separator:]))[0]
  sums[i] += ord(m) - ord('A') + 27 if m.isupper() else ord(m) - ord('A') - 31
print(sum(sums))
