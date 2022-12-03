data = [i.strip() for i in open('input.txt', 'r').readlines()]
sums = [0]*(len(data))
for i in range(0, len(data), 3):
  m = list(set(data[i]).intersection(set(data[i+1])).intersection(set(data[i+2])))[0]
  sums[i] += ord(m) - ord('A') + 27 if m.isupper() else  ord(m) - ord('A') - 31
print(sum(sums))
