# [SILVER 2] 다음 펠린드롬 수

import sys
k = str(sys.stdin.readline().strip())
length = len(k)

half_k = k[0:int(length/2)]
reverse_half_k = ''.join(reversed(list(half_k)))
middle=''
if(length%2 == 1):
    middle = k[int(length/2) : int(length/2)+1]

pel_num = int(half_k + middle + reverse_half_k)
k_num = int(k)

if(k_num < pel_num):
    print(pel_num)
    sys.exit(0)

temp = str(int(half_k + middle) + 1)

if(len(temp) == len(half_k+middle)):
    new_half_k = temp[0:int(length/2)]
    new_middle = '' if middle=='' else str((int(middle)+1)%10)
    new_reverse_half_k = ''.join(reversed(list(new_half_k)))

    print(int(new_half_k + new_middle + new_reverse_half_k))
    sys.exit(0)

if(len(temp) == len(half_k+middle)+1):
    length = length+1
    new_half_k = temp[0:int(length / 2)]
    new_middle = '' if ((length)%2 == 0) else '0'
    new_reverse_half_k = ''.join(reversed(list(new_half_k)))
    print(int(new_half_k + new_middle + new_reverse_half_k))
    sys.exit(0)
