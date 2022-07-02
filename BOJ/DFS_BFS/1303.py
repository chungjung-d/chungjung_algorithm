#전쟁 [Silver 1]

import sys
global army_sum

def add_battle_power(current_row,current_col,row,col,army_map,army):

    global army_sum
    army_sum = army_sum + 1

    army_map[current_col][current_row] = 0

    d_row = [0,0,1,-1]
    d_col = [1,-1,0,0]

    for i in range(4):
        n_col = d_col[i] + current_col
        n_row = d_row[i] + current_row
        if(n_row>=0 and n_col>=0 and n_col< col and n_row< row):
            if(army_map[n_col][n_row] == army):
                add_battle_power(n_row,n_col,row,col,army_map,army)


army_map = []

row, col = map(int,sys.stdin.readline().split())
for c in range(col):
    temp_list = sys.stdin.readline().rstrip()
    temp_list = list(temp_list)
    army_map.append(temp_list)

sum_white = 0
sum_black = 0

for c in range(col):
    for r in range(row):
        if(army_map[c][r] == 'W'):
            army_sum = 0
            add_battle_power(r, c,row, col, army_map,'W')
            sum_white = sum_white+army_sum*army_sum
        if (army_map[c][r] == 'B'):
            army_sum = 0
            add_battle_power(r, c, row, col, army_map, 'B')
            sum_black = sum_black + army_sum * army_sum

print(sum_white,sum_black)