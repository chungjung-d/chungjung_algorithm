#전쟁 [GOLD 5]

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
deq = deque()

array_map = [0]*100002
array_map[n] =1
deq.append([n])

if(n==m):
    print(0)
    print(1)
    sys.exit(0)

if(n>m):
    print(n-m)
    print(1)
    sys.exit(0)

count = 0
num = 0

#print(deq)

while(deq):
    current_list = deq.popleft()
    next_list = []
    new_array = [0] * 100002

    for current in current_list:
        d_current = [1,-1,current]
        for i in d_current:
            n_current = current+i
            if(n_current>=0 and n_current<=100000):
                if (array_map[n_current] == 0):
                    next_list.append(n_current)
                    new_array[n_current] = array_map[current] + new_array[n_current]

    next_list =list(set(next_list))
    deq.append(next_list)
    count = count + 1

    for i in next_list:
        array_map[i] = new_array[i]

    if(m in next_list):
        break

print(count)
print(array_map[m])