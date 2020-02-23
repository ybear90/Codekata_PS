"""
* 문제
nums는 숫자로 이루어진 배열입니다.
가장 자주 등장한 숫자를 k 개수만큼 return해주세요.

nums = [1,1,1,2,2,3],
k = 2

return [1,2]

nums = [1]
k = 1

return [1]
"""
def top_k(nums, k):
	num_dict = {}
	result_list = []
	
	for num in nums:
		num_dict[num] = num_dict.get(num, 0) + 1
	
	num_list = sorted(num_dict.items(), key=lambda x:x[1], reverse=True)

	for _ in range(k):
		result_list.append(num_list.pop(0)[0])
	
	return result_list
	
	