# 현재 나이트 위치 입력받기
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) +1

# 나이트 이동 가능 8 방향 정의
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1, 2), (-2,1)]

# 8가지 방향에 대해 각 위치로 이동 가능한지 확인

result = 0
for step in steps:
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_col = col + step[1]
  
  # 해당 위치로 이동 가능하면 cnt+=1
  if next_row >= 1 and next_row <=8 and next_col >=1 and next_col <=8:
    result +=1
  
  print(result)
        
