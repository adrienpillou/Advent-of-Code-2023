from collections import defaultdict

with open("in.txt") as file:
    x = file.read()
    x = x.split("\n")

elf_cubes = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

games = dict()

sum = 0

for line in x:
    game_id = line.split(":")[0].split()[-1]
    games[game_id] = dict()
    sets = line.split(":")[1]
    subsets = sets.split(";")
    for s in subsets:
        cubes = s.split(",")
        for c in cubes:
            count = int(c.split()[0].strip())
            color = c.split()[1].strip()
            if not color in games[game_id].keys():
                games[game_id][color] = count
            elif games[game_id][color] < count:
                games[game_id][color] = count

for k in games.keys():
    games[k]["power"] = games[k]["red"] * games[k]["green"] * games[k]["blue"]
    print(k, games[k])

for k in games.keys():
    sum += games[k]["power"]

print(sum)