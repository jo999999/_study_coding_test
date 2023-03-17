## 역시 문제를 잘 이해해야 ++ detail한 예외도 잘 잡아내야
# 자료구조 set() 의 & 등을 잘 활용하자!!! 
# 자료구조 list() -- reverse = TRUE/FALSE

## 시간 초과라닝 ㅎ.ㅎ
def solution(X, Y):
    answer = []
    answer_str = ''
    DICT = dict()
    ## X를 일단 기준으로 하자
    X_lst = list([i for i in str(X)])
    Y_lst = list([i for i in str(Y)])
    
    if len(set(X_lst) & set(Y_lst)) ==0 : # 겹치는게 없음
        answer_str = str(-1)
    else : # 겹치는게 있음 -- 짝궁 만들 수 있음
        for i in list(set(X_lst)):  
            if X_lst.count(i) >= Y_lst.count(i): ## detail한 예외도 잘 잡아내야## 와 여기를 생각할 줄 알아야했음!!
                DICT[str(i)] =  Y_lst.count(i) 
            elif X_lst.count(i) < Y_lst.count(i):
                DICT[str(i)] =  X_lst.count(i)
            
        for k,v in DICT.items():
            for _ in range(v):
                answer.append(int(k))
        answer.sort(reverse=True)
        for string in answer:
            answer_str+=str(string)
        if answer_str[0] =='0': ## '00'으로 나오는게 있어서 예외처리
            answer_str = '0'
            
    return  answer_str
