# 문제 링크 :  

def solution(d, budget):
    if sum(d) <= budget:
        answer = len(d)
    else:        
        d.sort()
        cnt =0
        for i in range(len(d)): 
            budget -= d[i] ## 여기 위아래 순서땜시 !
            if budget >=0: ##
                cnt+=1 
            else:
                break
    
        answer = cnt
    return answer
  
'''
# 또다른 풀이
def solution(d, budget):
    d.sort()
    cnt = 0

    for i in d :
        budget -= i
        if budget < 0 :
               break
        cnt += 1
    answer = cnt
    return answer
'''
