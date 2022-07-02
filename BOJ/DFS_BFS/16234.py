#인구 이동 [GOLD 5]

import sys
import collections
from copy import deepcopy
sys.setrecursionlimit(10**6)

n , l ,r = map(int,sys.stdin.readline().split())

pop_map = []

for i in range(n):
    temp_list = list(map(int,sys.stdin.readline().split()))
    pop_map.append(temp_list)

deque = collections.deque()


visit_array = [[False]*n for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(col,row):

    BFSque = collections.deque()
    visit_array[col][row] = True
    BFSque.append([col,row])
    deque.append([col,row])

    sum_ = 0
    while(BFSque):
        current = BFSque.popleft()
        visit_array[current[0]][current[1]] = True
        sum_ = sum_ + pop_map[current[0]][current[1]]
        for i in range(4):
            ny = current[0] + dy[i]
            nx = current[1] + dx[i]

            if(ny < n and ny>=0 and nx < n and nx>=0 ):
                if(visit_array[ny][nx]==False):
                    dis = abs(pop_map[current[0]][current[1]] - pop_map[ny][nx])
                    if(dis>= l and dis <=r):
                        visit_array[ny][nx] = True
                        BFSque.append([ny,nx])
                        deque.append([ny, nx])

    return sum_

count = 0
next_list = []
new_next_list = []

while(True):

    flag = 0

    temp_map = deepcopy(pop_map)


    if(count == 0):
        for i in range(n):
            for j in range(n):
                next_list.append([i,j])

    for cordinate in next_list:
            i = cordinate[0]
            j = cordinate[1]
            if(visit_array[i][j] == False):
                sum = BFS(i,j)

                length = len(deque)
                if(length>1):
                    # print(deque)
                    flag = 1
                    pop = int(sum/length)
                    while(deque):
                        k = deque.popleft()
                        new_next_list.append(k)
                        temp_map[k[0]][k[1]] = pop
                    #
                    # for t in temp_map:
                    #     print(t)
                else:
                    deque.pop()

    pop_map = temp_map
    visit_array = [[False] * n for _ in range(n)]

    if (flag == 0):
        break

    count = count+1
    next_list = deepcopy(new_next_list)
    new_next_list = []

print(count)