"""
* 문제
숫자로 이루어진 배열인 nums를 인자로 전달합니다.
숫자중에서 과반수(majority, more than a half)가 넘은 숫자를 반환해주세요. 

예를 들어,
  
nums = [3,2,3]
return 3

nums = [2,2,1,1,1,2,2]
return 2


* 가정
nums 배열의 길이는 무조건 2개 이상
"""
def more_than_half(nums):
	number_dict = {}
	majority_key = None
	majority_num = -1
	
	for num in nums:
		number_dict[num] = number_dict.get(num, 0) + 1
		if number_dict[num] >= majority_num:
			majority_key = num
			majority_num = number_dict[num]
 
	return majority_key			