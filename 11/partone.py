with open("in.txt") as file:
    x = file.read().split("\n")

m = len(x)
n = len(x[0])
empty_rows = [all([x[i][j] == "." for j in range(m)]) for i in range(n)]
empty_cols = [all([x[i][j] == "." for i in range(n)]) for j in range(m)]

empty_rows_indexes = list()
empty_cols_indexes = list()

for i, ec in enumerate(empty_cols):
    if ec:
        empty_cols_indexes.append(i)

for i, er in enumerate(empty_rows):
    if er:
        empty_rows_indexes.append(i)

galaxies = list()

for j, line in enumerate(x):
    for i, c in enumerate(line):
        if c == "#":
            galaxies.append((i, j))

ans = 0
distances = dict()
for i, current_galaxy in enumerate(galaxies):
    distances[current_galaxy] = list()
    for j, other_galaxy in enumerate(galaxies):
        if current_galaxy == other_galaxy:
            continue
        dx = abs(other_galaxy[0] - current_galaxy[0])
        dy = abs(other_galaxy[1] - current_galaxy[1])
        
        for eci in empty_cols_indexes:
            if eci >= current_galaxy[0] and eci <= other_galaxy[0]:
                dx += 2

        for eri in empty_rows_indexes:
            if eri >= current_galaxy[1] and eri <= other_galaxy[1]:
                dy += 2
        
        distance = dx+dy
        distances[current_galaxy].append((j + 1, distance))
        ans += distance

print(ans//2)
        

