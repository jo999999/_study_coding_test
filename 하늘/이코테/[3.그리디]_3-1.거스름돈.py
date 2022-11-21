# 나의 답안
n = 1260
cnt = 0

while n !=0:
  if n >= 500:
    n -= 500
    cnt +=1
  elif n >= 100:
    n -= 100
    cnt +=1
  elif n >=50:
    n -= 50
    cnt +=1
  else:
    n -=10
    cnt +=1

    
# 이코테 답안    
n = 1260
cnt = 0
types = [500, 100, 50, 10]

for coin in types:
  cnt += n//coin # 해당 화폐로 거슬러 줄 수 있는 동전 수 세기 (몫)
  n %= coin # 나머
print(cnt)
