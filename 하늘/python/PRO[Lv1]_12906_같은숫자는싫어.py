
def solution(arr):
    lst = [] 
    
    lst.append(arr[0])
    for i in range(1,len(arr)):
        if lst[-1] != arr[i]:
            lst.append(arr[i]) 

    return lst
