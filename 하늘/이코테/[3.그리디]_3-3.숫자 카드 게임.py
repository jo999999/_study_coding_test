# 각 행마다 가장 작은수 찾은 후 -> 가장 큰 수 찾는 문제
n, m = map(int, input().split())
lst = []
for _ in range(n):
  lst.append(list(map(int, input().split())))

check = []
for i in lst:
  check.append(min(i))
print(max(check))

# 이코테 답안 : 
