def solution(a, b):
    answer = []
    for j, k in zip(a,b):
        answer.append(j*k) 
        
    return sum(answer)
