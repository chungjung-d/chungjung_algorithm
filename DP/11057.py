#오르막 수 [Silver 1]

import sys

n = int(sys.stdin.readline().strip())

DT = [[0]*10 for _ in range(n)]

for i in range(10):
    DT[0][i] = 1

if(n == 1):
    print(10)
    sys.exit(0)

for digit in range(1,n):
    for first_number in range(10):
        DT[digit][first_number] = sum(DT[digit-1][0:first_number+1])

print(sum(DT[n-1])%10007)

