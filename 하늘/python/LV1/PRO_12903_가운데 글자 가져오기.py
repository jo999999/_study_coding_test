# 문제 링크 ; 

def solution(s): 
    
    if len(s) % 2 == 1: # 홀수길이
        return s[int(len(s)/2)]
    else:
        return s[int(len(s)/2)-1: int(len(s)/2)+1]
