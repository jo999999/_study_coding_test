# 연속한 자연수로 표현
def solution(n):
    answer = 1
    ## 앞에서부터 순차적으로 돌아볼까
    for start in range(1, (n//2)+1): 
        sum=0
        for i in range(start,n):
            sum+=i
            if sum == n:
                answer +=1
                break
                
            if sum > n: ## 합이 n보다 커지면 반복문 안돌아도 되니까 (효율성 test)
                break

    return answer
