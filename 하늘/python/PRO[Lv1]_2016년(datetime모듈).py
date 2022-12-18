from datetime import datetime, date

def solution(a, b):
    date_ = date(2016,a,b)
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day  = date_.weekday()
    answer = days[day]
    
    return answer
  
  # 모듈 설명!! : https://codechacha.com/ko/python-what-day-is-it/
