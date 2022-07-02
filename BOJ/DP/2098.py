# [GOLD 1] 외판원 순회

import sys

n = int(sys.stdin.readline().strip())
city_map = []

for i in range(n):
    temp_table = list(map(int,sys.stdin.readline().split()))
    city_map.append(temp_table)

VISITED_ALL = (1<<n)-1

DT = [[None]*(1<<n) for _ in range(n)]
INF = float('inf')


def minimum_path(current , visited):
    if(visited == VISITED_ALL):
        return city_map[current][0] if city_map[current][0] != 0 else INF

    if(DT[current][visited] != None):
        return DT[current][visited]

    temp_dist = INF

    for city in range(n):
        if(visited & (1<<city) == 0 and city_map[current][city]!=0):
            temp_dist = min(temp_dist, minimum_path(city,visited | (1<<city)) + city_map[current][city])

    DT[current][visited] = temp_dist

    return temp_dist

print(minimum_path(0,1<<0))



