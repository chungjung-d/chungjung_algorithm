#숨바꼭질 3 [GOLD 5]

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

queue = deque()
is_find = False
visited = [-1]*100002

queue.append(n)
visited[n] = 0

if(n==m):
    print(0)
    sys.exit(0)

if(n>m):
    print(n-m)
    sys.exit(0)

while(queue):

    current = queue.popleft()
    if(current == m):
        print(visited[current])
        break

    if (current*2 >= 0 and current*2 < 100001 and current*2 < 2*m-n+1):
        if(visited[current*2] == -1):
            visited[current*2] = visited[current]
            queue.appendleft(current*2)

    dx = [-1,1]
    for i in dx:
        k = current + i
        if(k>=0 and k<100001):
            if(visited[k] == -1):
                visited[k] = visited[current]+1
                queue.append(k)
