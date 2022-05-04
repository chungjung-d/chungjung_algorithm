# [GOLD 4] 가르침

# import sys
# import itertools
#
# n, k = map(int,sys.stdin.readline().split())
# bin_dict = {'b': 20, 'd': 19, 'e': 18, 'f': 17, 'g': 16, 'h': 15, 'j': 14, 'k': 13, 'l': 12, 'm': 11, 'o': 10, 'p': 9, 'q': 8, 'r': 7,'s': 6, 'u': 5, 'v': 4, 'w': 3, 'x': 2, 'y': 1, 'z': 0 }
#
# word_list = []
# for _ in range(n):
#     word = set(sys.stdin.readline().strip())
#     word.remove('a')
#     word.remove('n')
#     word.remove('t')
#     word.remove('i')
#     word.remove('c')
#
#     bit = 0 << 21
#     for alphabet in word:
#         bit = bit | 1 << bin_dict[alphabet]
#     word_list.append(bit)
#
# k = 0 if k-5 < 0 else k-5
#
# comb_set = itertools.combinations(range(0,21),k)
# max_num = 0
# for word_set in comb_set:
#     bit_word = 0 << 21
#     for i in word_set:
#         bit_word = (bit_word | (1 << i))
#     count = 0
#     for word in word_list:
#         if ( bit_word == (word | bit_word)):
#             count = count + 1
#
#     max_num = max(max_num,count)
#
# print(max_num)


import sys
import itertools

n, k = map(int,sys.stdin.readline().split())

word_list = []
for _ in range(n):
    word = set(sys.stdin.readline().strip())

    bit = 0 << 26
    for alphabet in word:
        bit = bit | 1 << (ord(alphabet)-ord('a'))
    word_list.append(bit)


comb_set = itertools.combinations(range(0,26),k)
max_num = 0
for word_set in comb_set:
    bit_word = 0 << 26
    for i in word_set:
        bit_word = (bit_word | (1 << i))
    count = 0
    for word in word_list:
        if ( bit_word == (word | bit_word)):
            count = count + 1

    max_num = max(max_num,count)

print(max_num)