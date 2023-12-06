def count_ways(t, d):
    count = 0
    for i in range(t):
        if i * (t - i) > d:
            count += 1
    return count

print(count_ways(48989083, 390110311121360))

