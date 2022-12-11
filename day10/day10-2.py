from queue import Queue

def print_map(map: list) -> None:
  for line in map: print(*line, sep="")

def update_map(cycle: int, x: int) -> str:
  return '#' if x-1 <= cycle%40 <= x+1 else '.'

def main():
  insts = Queue()
  [insts.put(i.split()) for i in open('input.txt', 'r').readlines() if i != '\n']
  map = [['' for _ in range(40)] for _ in range(6)]
  
  adding = False
  
  ins = 0
  cycle = 0
  x = 1
  
  for i in range(len(map)):
    for j in range(len(map[i])):
      map[i][j] = update_map(cycle, x)
      cycle += 1
      if adding:
        x += ins
        adding = False
      else:
        if insts.empty(): continue
        inst = insts.get()
        if inst[0] != 'noop':
          adding = True
          ins = int(inst[1])
  
  print_map(map)

if __name__ == '__main__':
  main()
