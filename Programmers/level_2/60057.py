# 문자열 압축
import copy
import sys


def solution(s):

    len_s = len(s)
    divide_list = []

    for i in range(1,len_s+1):
        divide_list.append(i)

    min_value = sys.maxsize
    for divide in divide_list:
        duplicate_list = []
        divide_str = ""
        for j in range(0,len_s,divide):
            if not duplicate_list:
                duplicate_list.append(s[j:j+divide])
            else:
                if(duplicate_list[0] == s[j:j+divide]):
                    duplicate_list.append(s[j:j+divide])
                else:
                    count = len(duplicate_list)
                    divide_str = divide_str + str(count) + duplicate_list[0] if count != 1 else divide_str + duplicate_list[0]
                    duplicate_list = []
                    duplicate_list.append(s[j:j+divide])

            if(j==len_s-divide and duplicate_list):
                count = len(duplicate_list)
                divide_str = divide_str + str(count) + duplicate_list[0] if count != 1 else divide_str + duplicate_list[0]


        if(len_s%divide != 0):
            num_ = len_s - (len_s % divide ) + 1
            if(num_ == len_s):
                divide_str = divide_str + s[-1]
            else:
                divide_str = divide_str + s[num_-1:]

        # print(divide_str , divide, len(divide_str))
        min_value = min(min_value , len(divide_str))
    return (min_value)


print(solution("xababcdcdababcdcd"))