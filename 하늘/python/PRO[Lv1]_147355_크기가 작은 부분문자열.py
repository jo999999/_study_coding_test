def solution(t, p):
    answer = 0
    check_lst = []
    
    for i in range(len(t)-len(p)+1):
        check_lst.append(t[i:i+len(p)])
        
    for j in check_lst:
        if j <=p:
            answer+=1 
    return answer
 
