n = int(input())

## while 문 없이 가능했구낭..
cnt = 0
for i in range(n+1): # 0~ n시
  for j in range(60):
    for k in range(60):
      ### 매 시각 내 '3'이 포함됨 -> cnt +=1
      if '3' in str(i)+str(j)+str(k): ## 오 이런식으로
        cnt +=1

print(cnt)
