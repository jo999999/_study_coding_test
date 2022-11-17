def solution(n):
    lst = [int(i) for i in str(n)]
    lst = sorted(lst, reverse = True)
    answer = ''
    for i in lst:
        answer +=str(i)
    answer = int(answer)
    return answer

# 더 쉬운 풀이
#def solution(n):
#   ls = list(str(n))
#   ls.sort(reverse = True)
#    return int("".join(ls))
