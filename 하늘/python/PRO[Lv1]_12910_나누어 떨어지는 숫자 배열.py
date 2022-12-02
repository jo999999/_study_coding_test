def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor== 0 :
            answer.append(i)
    answer.sort()
    
    if len(answer) ==0:
        answer.append(-1)
    return answer





# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
# or [-1 ] <<< python은 or 앞이 참일경우 해당 값까지만 , 거짓일경우 뒤에 것까지 호출
