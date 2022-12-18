from itertools import combinations # 조합

def solution(number):
    # 완전 탐색??
    # 3명을 더해서 0이 되어야 삼총사!
    cnt = 0
    for i in list(combinations(number, 3)): # num C 3
        
        if sum(i)==0:
            cnt+=1
    return cnt
    
    
 '''
from itertools import product
from itertools import permutations
from itertools import combinations

 - 하나의 리스트에서 모든 순열/조합 찾기
 
from itertools import permutations # 순열

items = ['1', '2', '3', '4', '5']
list(permutations(items, 2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '1'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '1'), ('3', '2'), ('3', '4'), ('3', '5'), ('4', '1'), ('4', '2'), ('4', '3'), ('4', '5'), ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4')]

from itertools import combinations # 조합
list(combinations(items, 2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]

 
 
 
- 두개 이상의 리스트의 모든 조합 구하기
from itertools import product

items = [['a', 'b', 'c,'], ['1', '2', '3', '4'], ['!', '@', '#']]

list(product(*items))
# [('a', '1', '!'), ('a', '1', '@'), ('a', '1', '#'), ('a', '2', '!'), ('a', '2', '@')...

[출처] https://ourcstory.tistory.com/414
 
 '''
   
