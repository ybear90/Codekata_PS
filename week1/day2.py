"""
* 문제
reverse 함수에 정수인 숫자를 인자로 받습니다.
그 숫자를 뒤집어서 return해주세요.

x: 숫자
return: 뒤집어진 숫자를 반환!
 
예들 들어,
x: 1234
return: 4321

x: -1234
return: -4321

x: 1230
return: 321
"""

def reverse(x):
    if int(x) == 0:
        return x

    x = int(x)
    result = ''

    if x > 0:
        while x > 0:
            num = x % 10
            result += str(num)
            x = x // 10
        
        return result
        
    x = x * -1
    
    while x > 0:
        num = x % 10
        result += str(num)
        x = x // 10 

    return str(-1 * int(result))
