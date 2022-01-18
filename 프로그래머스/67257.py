# 프로그래머스[수식 최대화]
import itertools
import sys
import re
import copy

expression = sys.stdin.readline().strip();

numbers = list(map(int, re.split("[+*-]",expression)))
operater_list = list(re.sub(r'[0-9]+', '', expression))
max_num = -1*sys.maxsize


op = list(itertools.permutations(["+","*","-"],3))

for operators in op:
    copy_number = copy.deepcopy(numbers)
    operater_list_copy = copy.deepcopy(operater_list)
    for i in operators:

        while(True):
            flag = True
            for j in range(len(operater_list_copy)):
                if (operater_list_copy[j] == i):
                    if( i == "+"):
                        copy_number[j]= copy_number[j]+copy_number[j+1]
                    if (i == "-"):
                        copy_number[j] = copy_number[j] - copy_number[j + 1]
                    if (i == "*"):
                        copy_number[j] = copy_number[j] * copy_number[j + 1]
                    del copy_number[j+1]
                    del operater_list_copy[j]
                    flag = False
                    break

            if (flag == True):
                break
    max_num = max(max_num,abs(copy_number[0]));

print(max_num)