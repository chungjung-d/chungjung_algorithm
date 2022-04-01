# #동전1 [Gold 5]
#
# import sys
#
# n , k = map(int, sys.stdin.readline().split())
#
# list_coin = []
# for i in range(n):
#     temp = int(sys.stdin.readline().strip())
#     list_coin.append(temp)
#
# DT = [[0]*(k+1) for _ in range(n+1)]
#
# for i in range(1,n+1):
#     DT[i][0] = 1
#
# for i in range(1,n+1):
#     current_coin = list_coin[i-1]
#     for j in range(1,k+1):
#         temp = 0
#         if(j- current_coin >= 0):
#             temp = DT[i][j-current_coin]
#         DT[i][j] = DT[i-1][j]+temp
#
# print(DT[n][k])


# #동전1 [Gold 5]
#
# import sys
# import copy
#
# n , k = map(int, sys.stdin.readline().split())
#
# list_coin = []
# for i in range(n):
#     temp = int(sys.stdin.readline().strip())
#     list_coin.append(temp)
#
# DT = [[0]*(k+1) for _ in range(2)]
#
# DT[1][0] = 1
#
# Temp_DT2 = copy.deepcopy(DT[1])
#
# for i in range(n):
#     current_coin = list_coin[i-1]
#
#     for j in range(1,k+1):
#         temp = 0
#         if(j - current_coin >= 0):
#             temp = DT[1][j-current_coin]
#         DT[1][j] = DT[0][j]+temp
#
#     Temp_DT1 = copy.deepcopy(DT[1])
#     DT = []
#     DT.append(Temp_DT1)
#     DT.append(Temp_DT2)
#
# print(DT[1][k])


#동전1 [Gold 5]

import sys

n , k = map(int, sys.stdin.readline().split())

list_coin = []
for i in range(n):
    temp = int(sys.stdin.readline().strip())
    list_coin.append(temp)

DT = [0]*(k+1)
DT[0] = 1

for current_coin in list_coin:

    for j in range(1,k+1):
        temp = 0
        if(j - current_coin >= 0):
            temp = DT[j-current_coin]
        DT[j] = DT[j]+temp

print(DT[k])
