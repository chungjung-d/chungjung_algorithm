#연산자 끼워넣기 [Silver 1]

import sys
import copy

def op(index,num1,num2):
    if(index == 0):
        return num1+num2
    if(index == 1):
        return num1-num2
    if(index == 2):
        return num1*num2
    if(index == 3):
        return int(num1/num2)

def find(numbers, operators):
    if(len(numbers) == 1):
        global _max , _min
        if(numbers[0]>_max):
            _max = numbers[0]
        if(numbers[0]<_min):
            _min = numbers[0]
        return

    for i in range(4):
        new_num = copy.deepcopy(numbers)
        new_op = copy.deepcopy(operators)
        num1 = new_num.pop(0)
        num2 = new_num.pop(0)
        if(new_op[i]>0):
            new_op[i] = new_op[i]-1
            new_num.insert(0,op(i,num1,num2))
            find(new_num,new_op)

n = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().split()))
operators = list(map(int,sys.stdin.readline().split()))
_max = (-1)*sys.maxsize
_min = sys.maxsize

find(number,operators)

print(_max)
print(_min)