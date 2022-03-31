# [GOLD 5] LCS

import sys

word1 = list(map(str,sys.stdin.readline().strip()))
word2 = list(map(str,sys.stdin.readline().strip()))

l1 = len(word1)
l2 = len(word2)

DT = [[0]*(l1+1) for _ in range(l2+1)]

for i in range(0,l2):
    for j in range(0,l1):
        if(word2[i] == word1[j]):
            DT[i+1][j+1] = DT[i][j] + 1
        else:
            DT[i+1][j+1] = max(DT[i][j+1] , DT[i+1][j])

print(DT[i+1][j+1])
