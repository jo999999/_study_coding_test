def solution(numbers): 
    num_lst = [i for i in range(10)]
    return sum(set(num_lst) - set(numbers))
