def solution(n):
    n = str(n)
    lst = []

    for i in range(0,len(n)):
      lst.append(int(n[i]))
    answer = sum(lst)
        
    return answer


# 더 간단한 풀이 # list comprehension
#def sum_digit(number):
#    return sum([int(i) for i in str(number)])
