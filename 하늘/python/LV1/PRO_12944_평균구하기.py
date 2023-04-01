# 문제 링크 :  

def solution(arr):
    answer = 0
    for i in arr:
        answer +=i
    answer = answer / len(arr)
    return answer
    
  # 그냥 sum()하면 될것을 ㅎ
  # def average(list):
  #  return (sum(list) / len(list))
