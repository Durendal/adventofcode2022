input = [i.strip().split("\n") for i in open('input.txt', 'r').read().split("\n\n")]
class Monkey:

  def __init__(
    self, 
    objects:  list = [],  
    div:      int  = 0,
    if_true:  int  = 0,
    if_false: int  = 0,
    op:       list = []
  ) -> None:
    self._objects  = objects
    self._div      = div
    self._if_true  = if_true
    self._if_false = if_false
    self._op       = op 
    self._counter  = 0

  def test(self, val: int) -> tuple:
    self._counter += 1
    ans = eval(' '.join(self._op).replace("old", str(val))) // 3
    if ans % self._div == 0:
      return self._if_true, ans 
    else:
      return self._if_false, ans 

monkeys = []

for monkey in input:
  operation = monkey[-4:]
  monkeys.append(Monkey(
    objects=[i.replace(",", "") for i in monkey[1].split()[2:]],
    div=int(operation[-3].split()[-1]),
    if_true=int(operation[-2].split()[-1]),
    if_false=int(operation[-1].split()[-1]),
    op=operation[0].split(' ')[5:],
  ))

for _ in range(20):
  for monkey in monkeys:
    for item in monkey._objects:
      ind, new = monkey.test(item)
      monkeys[ind]._objects.append(new)
    monkey._objects = []
    
ans = sorted([i._counter for i in monkeys])[-2:]
print(ans[0]*ans[1])
