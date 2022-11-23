def solution(absolutes, signs): 
    for i in range(len(signs)):
        if signs[i] == True:
            absolutes[i] = abs(absolutes[i])    
        else: 
            absolutes[i] = -abs(absolutes[i])
            
    return sum(absolutes)
    
    # abs() method
    
    # zip() 이라는것도 있네
    # def solution(absolutes, signs):
    # answer=0
    # for absolute,sign in zip(absolutes,signs):
    #    if sign:
    #        answer+=absolute
    #    else:
    #        answer-=absolute
    # return answer
