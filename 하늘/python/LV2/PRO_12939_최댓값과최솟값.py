def solution(s):
    ## 공백기준으로 잘라서 넣기 
    s += ' ' # 마지막 공백도 추가해 줄 것
    num=[]
    string =''
    
    for i in s:
        if i != ' ':
            string += i
        elif i == ' ':
            num.append(int(string))
            string =''
 
    answer = str(min(num)) + ' '+ str(max(num)) 
 
    return answer

#### list.split(' ') 이 있었는데!
def solution(s): 
    num =s.split(" ") 
    num = [int(i) for i in num]
    return str(min(num)) + ' '+ str(max(num)) 
