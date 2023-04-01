# 문제 링크 ; 

def solution(n):
    lst = []
    for i in range(0,n+1):
        for j in range(0, n+1):
            if i *j == n :
                lst.append(i)
                lst.append(j)
    lst = list(set(lst))
    answer = sum(lst)
    return answer
    
# 괜한 이중 포문 말고 더 간단한 풀이
#
#def solution(n):
#  lst = []
#    for i in range(1, n+1):
#        if n % i == 0: # 나머지가 0
#            lst.append(i)
#   
#    answer = sum(lst)
#    return answer
    
   
