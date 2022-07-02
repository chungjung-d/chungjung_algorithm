#[SILVER 1] 동전 2

import sys
n , k = map(int,sys.stdin.readline().split())
coin_list = []
for i in range(n):
    temp = int(sys.stdin.readline().strip())
    coin_list.append(temp)

DT = [10001]*(k+1)
DT[0] = 0

for coin in coin_list:
    for j in range(coin,k+1):
            DT[j] = min(DT[j],DT[j-coin]+1)

if(DT[k]==10001):
    print(-1)
else:
    print(DT[k])
