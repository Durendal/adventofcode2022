from queue import Queue

def main():
  insts = Queue()
  [insts.put(i.split()) for i in open('input.txt', 'r').readlines() if i != '\n']
  checks = [20, 60, 100, 140, 180, 220]
  signals = []
  
  adding = False
  
  ins = 0
  cycle = 0
  x = 1
  
  while cycle < 240:
    cycle += 1
    if cycle in checks:
      signals.append(x*cycle)
    if adding:
      x += ins
      adding = False
    else:
      if insts.empty(): break
      inst = insts.get()
      if inst[0] != 'noop':
        adding = True
        ins = int(inst[1])
  
  print(sum(signals))

if __name__ == '__main__':
  main()
