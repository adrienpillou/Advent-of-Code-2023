with open("in.txt") as file:
    x = file.read()
    x = x.split("\n")

elf_cubes = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

sum = 0

for line in x:
    game_id = line.split(":")[0].split()[-1]
    sets = line.split(":")[1]
    subsets = sets.split(";")
    possible = True
    for s in subsets:
        cubes = s.split(",")
        print(cubes)
        for c in cubes:
            count = int(c.split()[0].strip())
            color = c.split()[1].strip()
            if elf_cubes[color] < count:
                possible = False
    if possible:
        sum += int(game_id)

print(sum)