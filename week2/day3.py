"""
*문제
s는 여러 괄호들로 이루어진 String 인자입니다.
s가 유효한 표현인지 아닌지 true/false로 반환해주세요.

종류는 '(', ')', '[', ']', '{', '}' 으로 총 6개 있습니다. 
아래의 경우 유효합니다.
한 번 괄호를 시작했으면, 같은 괄호로 끝내야 한다.
괄호 순서가 맞아야 한다.

예를 들어 아래와 같습니다.  

s = "()"
return true

s = "()[]{}"
return true

s = "(]"
return false

s = "([)]"
return false

s = "{[]}"
return true
"""
def is_valid(string):
	closed_bracket = {'(': ')', '{': '}', '[': ']'}
	stack = []
	
	for idx in range(len(string)):
	 if string[idx] in closed_bracket.keys():
	 	stack.append(string[idx])
	 else:
	 	if len(stack) == 0:
	 		return False
	 	elif (closed_bracket[stack[-1]] == string[idx]):
	 		stack.pop()
	 	else:
	 		return False
	if len(stack) != 0:
		return False
	 
	return True
