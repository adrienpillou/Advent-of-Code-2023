import re

with open("in.txt") as file:
    x = file.read()
    x = x.split("\n")

time_range = [int(v) for v in re.findall("\d+", x[0])]
distance_range = [int(v) for v in re.findall("\d+", x[1])]

ways = list()
for n, t in enumerate(time_range):
    print(f"\n--- {t} ---")
    i = 0
    race_results = list()
    while(t - i >= 0):
        boat_speed = i
        d = boat_speed * (t - i)
        race_results.append(d)
        i += 1
    print(race_results)
    ways_count = 0
    for r in race_results:
        if r > distance_range[n]:
            ways_count += 1
    ways.append(ways_count)

solution = 1
for w in ways:
    solution *= w

print(solution)

