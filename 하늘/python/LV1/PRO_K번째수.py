# 문제 링크 :  

def solution(array, commands):
    answer = []
    for part in commands:
        sort = sorted(array[part[0]-1:part[1]])
        answer.append(sort[part[2]-1])    
    return answer
