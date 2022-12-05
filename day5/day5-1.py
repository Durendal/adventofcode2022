# Answer - GRTSWNJHH
# Sort Data and instructions
data_map, instructions = open('input.txt', 'r').read().split("\n\n")
data_map, _ = data_map.split("\n ")
instructions = [i for i in instructions.split("\n") if i != '\n' and i != '']
clean = [['' for _ in range(8)] for _ in range(9)] 

# Clean up data, transpose matrix
for i, row in enumerate(data_map.split("\n")):
  row = row.replace("    ", " [ ] ").replace("\n", "").replace("  ", " ").split("] [")
  for j, col in enumerate(row):
    clean[j][i] = col.replace("[", "").replace("]", "").strip()

# Remove empty string elements
clean = [list(filter(('').__ne__, i[::-1])) for i in clean]

# Process instructions
for i in instructions:
  _, n, _, fr, _, to = i.split(" ")
  for j in range(int(n)):
    clean[int(to)-1].append(clean[int(fr)-1].pop())
      
print(*[i[-1] for i in clean],sep="")
