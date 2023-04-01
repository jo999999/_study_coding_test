# 문제 링크 ; 

def solution(a, b):
    if a == b:
        return a
    elif a < b:
        answer = 0
        for i in range(a, b+1):
           answer += i
        return answer
    elif a > b:
        answer = 0
        for i in range(b, a+1):
           answer += i
        return answer
      
# min(), max(), sum() 더 간편함
# def adder(a, b):
     # return sum(range(min(a,b),max(a,b)+1))
