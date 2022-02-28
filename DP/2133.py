#타일 채우기 [Gold 5]

import sys

n = int(sys.stdin.readline().strip())

if(n%2 != 0):
    print(0)
    sys.exit(0)

DT = [0] * 31
DT[2] = 3

sum = 0

for i in range(4,31,2):
    sum = sum + DT[i-2]
    DT[i] = 2*sum + DT[i-2] + 2

print(DT[n])
