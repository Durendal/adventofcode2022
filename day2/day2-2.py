data = [i.strip() for i in open('input.txt').readlines()]
sumval = 0
results = {
  'A': {
    'X': 3,
    'Y': 4,
    'Z': 8,
  },
  'B': {
    'X': 1,
    'Y': 5,
    'Z': 9,
  },
  'C': {
    'X': 2,
    'Y': 6,
    'Z': 7,
  }
}
for row in data:
  opp, me = row.split()
  sumval += results[opp][me]
print(sumval)

