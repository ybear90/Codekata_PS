"""
* 문제
String 형인 str 인자에서 중복되지 않은 알파벳으로 이루어진 제일 긴 단어의 길이를 반환해주세요.

str: 텍스트
return: 중복되지 않은 알파벳 길이 (숫자 반환)

예를 들어,
str = "abcabcabc"
return은 3
=> 'abc' 가 제일 길기 때문

str = "aaaaa"
return은 1
=> 'a' 가 제일 길기 때문

str = "sttrg"
return은 3
=> 'trg' 가 제일 길기 때문
"""
def get_len_of_str(string):
	longest_length = 0
	unique_string = ''
	length = 0
	
	for idx in range(len(string)):
		if string[idx] not in unique_string:
			unique_string += string[idx]
			length += 1
		else:
			unique_string = string[idx]
			length = 1
		if longest_length <= length:
			longest_length = length
	
	for idx in range(len(string)-1, 0, -1):
		if string[idx] not in unique_string:
			unique_string += string[idx]
			length += 1
		else:
			unique_string = string[idx]
			length = 1
		if longest_length <= length:
			longest_length = length
	
	return longest_length