import re
import itertools

with open("in.txt") as file:
    x = file.read().split("\n")

def list_arrangements(springs, groups):
    groups = [int(v) for v in groups.split(",")]
    marks_index = re.finditer("\?", springs)
    indexes = [i.start() for i in marks_index]
    marks_count = len(indexes)
    chars = [".", "#"]
    combinations = list(itertools.product(chars, repeat=marks_count))
    potential_arrangements = list()
    for combi in combinations:
        test_springs = list(springs)
        for i, char in enumerate(combi):
            test_springs[indexes[i]] = char
        test_springs = "".join(test_springs)
        splitted_test_springs = "".join(test_springs).split(".")
        while '' in splitted_test_springs:
            splitted_test_springs.remove('')
        if len(groups) == len(splitted_test_springs):
            potential_arrangements.append(splitted_test_springs)
    return potential_arrangements

arrangements_count = 0

for l, line in enumerate(x):
    springs, groups = line.split()
    potential_arrangements = list_arrangements(springs, groups)
    groups = [int(v) for v in groups.split(",")]
    for pa in potential_arrangements:
        if [len(v) for v in pa] == groups:
            arrangements_count += 1
    print(f"{l/len(x)}")
print(arrangements_count)