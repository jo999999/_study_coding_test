def solution(n):
    answer = [int(i) for i in str(n)]
    answer.reverse()
    return answer
    
   # #answer =  sorted(answer, reverse=True) 이렇게 해서 통과 안되었는데
   # 암튼 이 문제는 단순 reverse 문제였다고함.
   # sorted(lst, reverse = True) vs lst.reverse() 차이가 뭐지 
   # 아 전자는 오름차/내림차순으로 정렬, 후자는 진짜 그냥 뒤집는거!!!
