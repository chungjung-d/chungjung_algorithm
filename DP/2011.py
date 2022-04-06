import sys


n = str(sys.stdin.readline().strip())
if(len(n) == 1):
    if(int(n) == 0):
        print(0)
    else:
        print(1)
    sys.exit(0)

DT = [0]*(len(n)+1)
DT[0] = 1
if(int(n[-1:]) !=0):
    DT[1] = 1

for i in range(2,len(n)+1):
    string = n[-i:]
    test_case = int(string[:2])
    if(test_case == 0):
        print(0)
        sys.exit(0)

    if(test_case>10 and test_case<=26):
        DT[i] = DT[i-1] + DT[i-2]
    elif(test_case == 10):
        DT[i] = DT[i-2]
    elif(test_case < 10 and test_case >0):
        DT[i] = 0
    else:
        DT[i] = DT[i-1]

print(DT[len(n)]%1000000)