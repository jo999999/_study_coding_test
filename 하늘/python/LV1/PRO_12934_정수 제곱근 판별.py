# 문제 링크 :  

import math # math.sqrt()이거 이용하면 됨!

def solution(n):
    if math.sqrt(n) == round(math.sqrt(n)):
        answer = (math.sqrt(n)+1)**2
    else:
        answer = -1
    return answer



#def solution(n):
#    for i in range( 0, round(n/2)): # round(n/2) 때문에 런타임 에러 나는듯.
#        if i**2 == n:
#            answer = (i+1)**2
#            break
#        else:
#            answer = -1

 #   return answer
