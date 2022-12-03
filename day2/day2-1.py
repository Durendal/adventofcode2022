data = [i.strip() for i in open('input.txt').readlines()]
sumval = 0
results = {
  'A': {
    'X': 4,
    'Y': 8,
    'Z': 3,
  },
  'B': {
    'X': 1,
    'Y': 5,
    'Z': 9,
  },
  'C': {
    'X': 7,
    'Y': 2,
    'Z': 6,
  }
}
for row in data:
  opp, me = row.split()
  sumval += results[opp][me]
print(sumval)

