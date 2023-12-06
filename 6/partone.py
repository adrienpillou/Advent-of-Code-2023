import re

with open("in.txt") as file:
    x = file.read()
    x = x.split("\n")

time_range = [int(v) for v in re.findall("\d+", x[0])]
distance_range = [int(v) for v in re.findall("\d+", x[1])]

ways_count = list()
for n, t in enumerate(time_range):
    i = 0
    ways = list()
    for i in range(t):
        boat_speed = i
        d = i * (t - i)
        if d > distance_range[n]:
            ways.append(d)
    ways_count.append(len(ways))

s = 1
for w in ways_count:
    s *= w

print(s)

