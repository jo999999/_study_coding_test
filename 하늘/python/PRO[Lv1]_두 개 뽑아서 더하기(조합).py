from itertools import combinations

def solution(numbers):
    answer = []
    lst = list(combinations(numbers, 2))
    for i in lst:
        answer.append(sum(i))
    answer = list(set(answer))
    answer.sort() # 오름차순 (문제조건!)
    return answer
