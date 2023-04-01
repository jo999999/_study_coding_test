# https://school.programmers.co.kr/learn/courses/30/lessons/159994
## 예외를 잡아내는게 참,, 뭐가 문제일까ㅏㅏ
## 문장 길이를 먼저 확인하면 오류가 안난대 ㅠㅠ 하..ㅋㅋㅋ
'''
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
'''

def solution(cards1, cards2, goal):
    answer_lst = []
    if len(set(goal) & set(cards1+cards2)) < len(set(goal)): 
        return 'No' 
    else : 
 ## cards1, cards2 -- 왼쪽으로 시작하면서 다른게 나올때까지 -> 나오면 stop 하고 cards2마저 진행
        for g in goal: 
            
            if len(cards1) >0 and  g == cards1[0]:
                answer_lst.append(cards1[0])
                cards1.pop(0)   
            elif len(cards2) >0 and g == cards2[0]:
                answer_lst.append(cards2[0])
                cards2.pop(0)
 
    if  answer_lst == goal:
        return 'Yes'
    else:
        return 'No' 
