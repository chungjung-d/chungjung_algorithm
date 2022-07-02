# [GOLD 1] 외판원 순회3

import sys
import itertools
import math

n = int(sys.stdin.readline().strip())
city_map = []
city_adj_matrix = [[0]*n for _ in range(n)]

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    city_map.append(temp)

comb = itertools.combinations(range(n),2)

for i in comb:
    first = i[0]
    second = i[1]

    first_col = city_map[first][0]
    first_row = city_map[first][1]
    second_col = city_map[second][0]
    second_row = city_map[second][1]

    distance = math.sqrt((first_col-second_col)**2 + (first_row-second_row)**2)
    city_adj_matrix[first][second] = distance
    city_adj_matrix[second][first] = distance

DT = [[None]*(1<<n) for _ in range(n)]
INF = float('inf')

def TSP(current,visited):
    # print(current,visited)
    if(visited == (1<<n)-1):
        return city_adj_matrix[current][0]

    if(DT[current][visited]!=None):
        return DT[current][visited]

    temp = INF
    for i in range(n):
        if(visited & 1<<i == 0):
            temp = min(temp , TSP(i,visited | 1<<i) + city_adj_matrix[current][i])

    DT[current][visited] = temp
    return temp

print(TSP(0,1<<0))
