n = int(input())
x,y = 1,1
plans = input().split() # << 이렇게 그냥 해줘도 된다 // = list(map(str, input().split()))

# L R U D 에 따른 이동
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U','D']

for plan in plans: 
  # 이동후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간 벗어나는 경우 무시!! --- 아래처럼 제약 걸어주면 되는구나
  if nx <1 or ny <1 or nx > n or ny >n :
    continue # 바로 아래 코드를 실행하지 않고 건너뜀
  # 이동수행
  x, y = nx, ny

print(x,y)
