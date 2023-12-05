import re

with open("example.txt") as file:
    x = file.read()
    x = x.split("\n")

seeds = [int(v) for v in re.findall("\d+", x[0])]

maps = list()
maps.append(list())
map_index = 0
for line in x[2:]:
    if line == "":
        maps.append(list())
        map_index += 1
    else:
        maps[map_index].append(line)

ranges = list()

for i, m in enumerate(maps):
    for d in m:
        if not d[0].isdigit():
            continue
        destination_range_start, source_range_start, range_length = [int(v) for v in d.split()]
        destination_range = (destination_range_start, destination_range_start + range_length)
        source_range = (source_range_start, source_range_start + range_length)
        ranges.append({"source": source_range, "dest": destination_range})

for ri, r in enumerate(ranges):
    print(f"Range {ri}")
    for si, s in enumerate(seeds):
        if s >= ranges[ri]["source"][0] and s <= ranges[ri]["source"][1]:
            seed_index = s - ranges[ri]["source"][0]
            seeds[si] = ranges[ri]["dest"][0] + seed_index
            print(ranges[ri]["dest"][0] + seed_index)
        else:
            print(s)

print(min(seeds))

