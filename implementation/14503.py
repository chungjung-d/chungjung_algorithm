#[Gold 5] 로봇청소기

import sys

col,row = map(int,sys.stdin.readline().split())

r,c,d = map(int,sys.stdin.readline().split())

map_of_room = []
count = 0


for i in range(col):
    temp_map = list(map(int,sys.stdin.readline().split()))
    map_of_room.append(temp_map)

#왼쪽으로 돌 경우 -1을 하면 된다.

dircetion_row = [-1,0,1,0]
dircetion_col = [0,1,0,-1]

def rotate_left(current_dir : int):
    if(current_dir == 0):
        return 3
    else:
        return current_dir-1

def verify_clean(current_col, current_row, current_dir):

    is_clean_all = True

    for i in range(4):
        n_col = current_col + dircetion_col[i]
        n_row = current_row + dircetion_row[i]
        if(map_of_room[n_row][n_col]==0):
            is_clean_all = False
            break

    if(is_clean_all == False):
        return False

    if(is_clean_all == True):
        backward_dir = (current_dir+2)%4
        #뒤로 갔을떄 벽이 있을 경우
        if(map_of_room[current_row+dircetion_row[backward_dir]][current_col+dircetion_col[backward_dir]] == 1):
            print(count)
            sys.exit(0);
        else:
            return True

while(True):
    # print(r,c)
    if(map_of_room[r][c] == 0):
        map_of_room[r][c] = 2
        count = count + 1

    next_d = rotate_left(d)
    next_row = r + dircetion_row[next_d]
    next_col = c + dircetion_col[next_d]

    if(map_of_room[next_row][next_col]==0):
        r = next_row
        c = next_col
        d = next_d
        # print("continue")
        continue

    if (map_of_room[next_row][next_col] != 0):
        verify = verify_clean(c,r,d)
        # print("verify")
        # print(verify)
        if(verify == False):
            d = next_d
        if(verify == True):
            reverse_d = (d+2)%4
            next_row = r + dircetion_row[reverse_d]
            next_col = c + dircetion_col[reverse_d]
            r = next_row
            c = next_col
