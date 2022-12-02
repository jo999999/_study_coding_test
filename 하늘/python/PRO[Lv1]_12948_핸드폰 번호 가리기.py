def solution(phone_number):
    answer = ''
    back = phone_number[-4:]
    for i in range(len(phone_number[:-4])):
        answer += '*'
    answer +=back
    
    return answer

# 더 쉬운 풀이
#def hide_numbers(s):
#    return "*"*(len(s)-4) + s[-4:] 문자열 곱셈.
