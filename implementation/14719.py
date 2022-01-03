#빗물 [GOLD 5]

import sys

def max_left(areas,left,flag_idx):

    if(left == 0):
        return

    max_number = max(areas[0:left])
    max_num_index = areas[0:left].index(max_number)
    flag_idx.append(max_num_index)

    max_left(areas,max_num_index,flag_idx)

def max_right(areas,right,w,flag_idx):

    if(right == w):
        return

    max_number = max(areas[right:w])
    max_num_index = -1
    for index,i in enumerate(areas[right:w]):
        if(i==max_number):
            max_num_index = index

    max_num_index = max_num_index+right
    flag_idx.append(max_num_index)

    max_right(areas,max_num_index+1,w,flag_idx)

h , w = map(int,sys.stdin.readline().split())
area = list(map(int,sys.stdin.readline().split()))

flag_idx = []
max_first = -1
max_last = -1
max_num = max(area)

for index,i in enumerate(area):
    if(i == max_num):
        max_last = index
        if(max_first == -1):
            max_first = index

flag_idx.append(max_last)
flag_idx.append(max_first)

max_left(area,left=max_first,flag_idx=flag_idx)
max_right(area,right=max_last+1,w=w,flag_idx=flag_idx)

sum_num = 0
flag_idx = sorted(flag_idx)
for i in range(1,len(flag_idx)):
    idx1 = flag_idx[i-1]
    idx2 = flag_idx[i]

    ext1 = area[idx1]
    ext2 = area[idx2]

    min_num = min(ext1,ext2)
    for j in range(idx1+1,idx2):
        sum_num = sum_num + min_num - area[j]

print(sum_num)