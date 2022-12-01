data = [j.split("\n") for j in [i for i in open('input1.txt', 'r').read().split("\n\n")]]
print(max([sum([int(j) for j in data[i] if j != '']) for i in range(len(data))]))
