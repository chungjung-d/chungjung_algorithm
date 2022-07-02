# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums ):
    zero_count = 0
    match_count = 0
    for i in lottos:
        if (i in win_nums):
            match_count = match_count+1
        if i == 0:
            zero_count = zero_count+1

    max_win = 6-(zero_count+match_count)+1 if 6-(zero_count+match_count)+1 <=6 else 6
    min_win = 6-(match_count)+1 if 6-(match_count)+1 <=6 else 6
    answer = [max_win,min_win]

    return answer