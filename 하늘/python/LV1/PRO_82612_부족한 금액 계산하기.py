# 문제 링크 :  

def solution(price, money, count):
    answer = 0
    add =  0            
    for _ in range(count):
        
        add +=1
        answer += price * (add)
    
    result = answer - money
    
    if  result < 0 : 
        return 0
    else : 
        return result 
      
  # 문제 조건을 잘 읽자. "" 단, 금액이 부족하지 않으면 0을 return 하세요. ""
