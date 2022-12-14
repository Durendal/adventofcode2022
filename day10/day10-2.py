def print_map(map: list) -> None:
  for line in map: print(*line, sep="")

def update_map(cycle: int, x: int) -> str:
  return '#' if x-1 <= cycle%40 <= x+1 else '.'

def main():
  insts = [i.split() for i in open('input.txt', 'r').readlines() if i != '\n'][::-1]
  map = [['' for _ in range(40)] for _ in range(6)]
  
  add = False
  
  acc = 0
  cycle = 0
  x = 1
  
  for i in range(len(map)):
    for j in range(len(map[i])):
      map[i][j] = update_map(cycle, x)
      cycle += 1
      if add:
        x += acc 
        add = False
      else:
        inst = insts.pop()
        if inst[0] != 'noop':
          add = True
          acc = int(inst[1])
  
  print_map(map)

if __name__ == '__main__':
  main()
