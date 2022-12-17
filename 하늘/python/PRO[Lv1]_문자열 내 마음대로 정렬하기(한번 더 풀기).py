# list sorted() -- key : lambda x: x~ 
# 아이디어 : 사전 정렬 먼저 -> 그후 특정 인덱스 기준 정렬
def solution(strings, n):
    return sorted(sorted(strings), key = lambda x:x[n])

# 같은 풀이 
'''
from operator import itemgetter, attrgetter, methodcaller

def solution(strings, n):
    return sorted(sorted(strings), key=itemgetter(n))
    # 첫째 sorted로 사전순으로 정렬, 둘째로 글자 특정 인덱스 순으로 정렬입니당


'''
