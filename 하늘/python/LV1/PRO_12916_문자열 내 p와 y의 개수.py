# 문제 링크 ; 

def solution(s):
    s = s.lower()
    p_lst = [i for i in s if i =='p']
    y_lst = [i for i in s if i =='y']
    
    if len(p_lst) == len(y_lst):
        return True
    else:
        return False 
        
        
        
# 더 간결히 푸는 법  # count()함수 이용!!!!!!!!!!
# def solution(s):
#     if s.lower().count('p') == s.lower().count('y'):
#         return True
#     else:
#         return False
