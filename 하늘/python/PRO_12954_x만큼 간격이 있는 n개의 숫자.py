def solution(x, n):
    answer = []
    answer.append(x)
    a=x
    for _ in range(n-1):
        a +=x
        answer.append(a)

    return answer

# 더 간단한 방법
# def number_generator(x, n):
#    return [i * x + x for i in range(n)]

