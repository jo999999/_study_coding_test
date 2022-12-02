def solution(arr1, arr2):

    answer = []

    for a, b in zip(arr1, arr2):
        l = []
        for x, y in zip(a, b):
            l.append(x + y)
        answer.append(l)

    return answer
  
  # 이중포문과 zip을 활용하면 되었음. 
