"""
*문제
strs은 단어가 담긴 배열입니다.
공통된 시작 단어(prefix)를 반환해주세요.  

예를 들어
strs = ['start', 'stair', 'step']
return은 'st'

strs = ['start', 'wework', 'today']
return은 ''
"""
def get_prefix(string):
	prefix = ''
	start_idx = 1
	
	if len(string) == 0:
		return ''
	elif len(string) == 1:
		return string[0]
	
	while start_idx <= len(string[0]):
		compare_str = string[0][:start_idx]
		
		for elem in string[1:]:
			if elem[:start_idx] != compare_str:
				return prefix
		
		prefix = compare_str
		
		start_idx += 1
	
	
	return prefix