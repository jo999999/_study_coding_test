# 문제 링크 :  

def solution(x): 
    num = [int(i) for i in str(x)]
    if x % sum(num) ==0 : # 자릿수의 합으로 나눠짐
        return True
    else:
        return False
