def main():
  insts = [i.split() for i in open('input.txt', 'r').readlines() if i != '\n'][::-1]
  checks = [20, 60, 100, 140, 180, 220]
  signals = []
  
  adding = False
  
  acc = 0
  cycle = 0
  x = 1
  
  while cycle < 240:
    cycle += 1
    if cycle in checks:
      signals.append(x*cycle)
    if adding:
      x += acc 
      adding = False
    else:
      if not insts: break
      inst = insts.pop()
      if inst[0] != 'noop':
        adding = True
        acc = int(inst[1])
  
  print(sum(signals))

if __name__ == '__main__':
  main()
