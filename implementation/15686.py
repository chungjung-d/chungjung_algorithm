import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

chicken = []
house = []

for col in range(n):
    temp_map = list(map(int, sys.stdin.readline().split()))
    for row in range(n):
        if (temp_map[row] == 1):
            house.append([col, row])
        if (temp_map[row] == 2):
            chicken.append([col, row])

# row : chicken / col : house
adj_matrix = [[0]*(len(chicken)+1) for _ in range(len(house))]
for ch_index, ch in enumerate(chicken):
    ch_col = ch[0]
    ch_row = ch[1]

    for h_index, h in enumerate(house):
        h_col = h[0]
        h_row = h[1]
        distance = abs(h_col-ch_col) + abs(h_row-ch_row)
        adj_matrix[h_index][ch_index] = distance

comb = itertools.combinations(range(0,len(chicken)),m)
min_val = sys.maxsize
for com_result in comb:
    for house_index , house in enumerate(adj_matrix):
        minimum_value = sys.maxsize
        for chicken_index , i in enumerate(house):
            if(chicken_index in com_result and i<minimum_value):
                minimum_value = i
        adj_matrix[house_index][len(chicken)] = minimum_value

    temp = 0
    for k in adj_matrix:
        temp = temp + k[len(chicken)]

    if(temp<min_val):
        min_val = temp

print(min_val)
