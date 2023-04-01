# 문제 링크 ; 

def solution(s):
    try:
        int(s)
    except:
        return False
      
    return len(s) == 4 or len(s) == 6  # 문제 조건 잘읽자. ::: 문자열 s의 길이가 4 혹은 6이고



# 아! try - except 이거 생각을 못했네
# def alpha_string46(s):
#     try:
#         int(s)
#     except:
#         return False
        
        
 # isdigit() 도 있음 ! 
 # def alpha_string46(s):
 #    return s.isdigit() and len(s) in (4, 6)
