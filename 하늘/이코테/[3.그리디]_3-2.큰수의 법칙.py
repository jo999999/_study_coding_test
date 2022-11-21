# 나의 풀이 
n, m, k = map(int, input().split())
lst = list(map(int, input().split()))

lst = sorted(lst, reverse= True)

set_cnt  = m // (k+1) # 
remainder = m % set_cnt

result = set_cnt * (( k*lst[0]) + lst[1]) + remainder * lst[0]
print( result)

# 이코테 답안
