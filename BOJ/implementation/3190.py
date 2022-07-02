#뱀 [GOLD 5]

import sys
from collections import deque
map_size = int(sys.stdin.readline().strip())
apple_size = int(sys.stdin.readline().strip())
apple = []
turn_list = [0]*(map_size*map_size+2)
deq = deque()

map_of_problem = [[0]*(map_size+1) for _ in range(map_size+1)]

for i in range(apple_size):
    col,row = map(int,sys.stdin.readline().split())
    temp = [row-1,col-1]
    map_of_problem[col-1][row-1] = 1
    apple.append(temp)

turn_time = int(sys.stdin.readline().strip())
for i in range(turn_time):
    time,turn = sys.stdin.readline().split()
    time = int(time)
    turn_list[time] = str(turn)

count = 0
current_row = 0
current_col = 0
map_of_problem[0][0] = -1
len_snake = 1
deq.append([0,0])

currnet_dir = 0
dir_x = [1,0,-1,0]  # 0:오른쪽 / 1:위 / 2:왼쪽 / 3:아래
dir_y = [0,-1,0,1]
while(True):

    next_row = current_row + dir_x[currnet_dir]
    next_col = current_col + dir_y[currnet_dir]
    deq.append([next_col, next_row])

    if (next_col >= map_size or next_row >= map_size or next_row <0 or next_col<0):
        count = count + 1
        break

    if(map_of_problem[next_col][next_row] == -1):
        count = count + 1
        break

    count = count + 1

    if(turn_list[count]=='D'):
        currnet_dir = currnet_dir - 1
        if(currnet_dir == -1):
            currnet_dir = 3
    if(turn_list[count]=='L'):
        currnet_dir = currnet_dir + 1
        if(currnet_dir == 4):
            currnet_dir = 0

    if(map_of_problem[next_col][next_row] == 0):   ## 사과가 없을떄
        map_of_problem[next_col][next_row] = -1
        tail = deq.popleft()
        map_of_problem[tail[0]][tail[1]] = 0

    if (map_of_problem[next_col][next_row] == 1):
        map_of_problem[next_col][next_row] = -1

    current_col = next_col
    current_row = next_row

    # for i in map_of_problem:
    #     print(i)
    #
    #
    # print()
    # print(next_row, next_col)
    # print(count)
    # print()

print(count)