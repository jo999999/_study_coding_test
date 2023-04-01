# 문제 링크 ; 

def solution(s):
    answer = ''
    s = sorted(s, reverse=True)
    for i in s:
        answer +=i
    return answer
