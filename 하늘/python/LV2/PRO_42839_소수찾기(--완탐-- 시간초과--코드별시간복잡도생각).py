## 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42839

## 소수찾기 -- 코드 별 시간복잡도 : https://veggie-garden.tistory.com/17
from itertools import combinations, permutations
import time

# 시간측정 살펴볼때
 #   start_time = time.time()
    #### 살펴볼 코드
 #   end_time = time.time()
 #   print("run time: ", end_time - start_time)
    
def concat_str(combi_lst):
    result = []
    for l in combi_lst:
        result.append(int("".join(l)))
    return result

def solution(numbers):
    nums = [ i for i in numbers]
    combi_lst = []
    num_lst = []
     
    # 전체 순열의 경우를 구하고
    for k in range(1,len(numbers)+1): 
        combi_lst += list(permutations(nums, k ))
    combi_lst = list(set(combi_lst)) # + nums
    num_lst = list(set(concat_str(combi_lst)))
 
    # 소수임을 판별  ----- 여기서 시간이 많이 걸렸음(시간복잡도 생각)
    cnt = 0
    for num in num_lst:
        lst =[]
        # n의 모든 약수는 n/2보다 작다. 고로 2부터 n-1까지 확인할 필요가 없다는 뜻이다. 
        for j in range(1,num // 2 + 1) : #(1, num+1):
            if num % j ==0 :
                lst.append(j)
        if len(lst) == 1:
            cnt+=1
 
    return cnt  
