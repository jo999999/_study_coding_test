def solution(arr):

    if len(arr) ==1 or 0:
        return [-1]
    else:
        arr.remove(min(arr)) 
        return arr
        
# list method --- remove()
