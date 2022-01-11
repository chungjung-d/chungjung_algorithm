#숨바꼭질 4 [GOLD 4]

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

queue = deque()
visited = [-1]*100002

queue.append(n)
visited[n] = 0

if(n==m):
    print(0)
    print(n)
    sys.exit(0)

if(n>m):
    print(n-m)
    for i in range(n,m-1,-1):
        print(i, end=' ')
    sys.exit(0)

while(queue):

    current = queue.popleft()
    if(current == m):
        break

    dx = [-1,1,current]
    for i in dx:
        k = current + i
        if(k>=0 and k<100001 and k< 2*m-n+1):
            if(visited[k] == -1):
                visited[k] = current
                queue.append(k)

now = m
order = []
while(True):
    order.append(now)
    if(now == n):
        break
    k = visited[now]
    now = k

print(len(order)-1)
for i in reversed(order):
    print(i, end=' ')