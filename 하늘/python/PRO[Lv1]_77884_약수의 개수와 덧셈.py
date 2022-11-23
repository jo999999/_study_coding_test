def solution(left, right):
 
    num_lst = [i for i in range(left, right+1)]
    check =[]
    for i in num_lst:
        lst = []
        for j in range(1, i+1):
            if i %j ==0:
                lst.append(j)
        check.append(len(lst))
        
    sum_lst = []
    for k, v in zip(num_lst, check):
        if v % 2 ==1 :
            sum_lst.append(-abs(k))
        else:
            sum_lst.append(abs(k))
        
    return sum(sum_lst)
