# Answer - GRTSWNJHH
# Sort Data and instructions
data_map, instructions = open('input.txt', 'r').read().split("\n\n")
data_map, _ = data_map.split("\n ")
instructions = [i for i in instructions.split("\n") if i != '\n' and i != '']
clean = [['' for _ in range(8)] for _ in range(9)] 

# Clean up data, transpose matrix
for i, row in enumerate(data_map.split("\n")):
  for j, col in enumerate(row.replace("    ", " [ ] ").replace("\n", "").replace("  ", " ").split("] [")):
    clean[j][i] = col.replace("[", "").replace("]", "").strip()

# Remove empty string elements
clean = [list(filter(('').__ne__, i[::-1])) for i in clean]

# Process instructions
for i in instructions:
  _, n, _, fr, _, to = i.split(" ")
  clean[int(to)-1].extend([clean[int(fr)-1].pop() for _ in range(int(n))])
      
print(*[i[-1] for i in clean],sep="")
