"""
* 문제
인자인 height는 숫자로 이루어진 배열입니다.그래프로 생각한다면 y축의 값이고, 높이 값을 갖고 있습니다.
아래의 그래프라면 height 배열은 [1, 8, 6, 2, 5, 4, 8, 3, 7] 입니다.

https://storage.googleapis.com/replit/images/1555380144403_97221ca23fbb92beaae5b6c800ceb5c8.pn

저 그래프에 물을 담는다고 생각하고, 물을 담을 수 있는 가장 넓은 면적의 값을 반환해주세요.

* 가정
배열의 길이는 2이상입니다.
"""
def get_max_area(height):
	max_area = 0
	
	for i in range(len(height)-1):
		for j in range(i+1, len(height)):
			fill_height = min(height[i], height[j])
			fill_area = (j - i) * fill_height
			# print("i: ", i, "j: ", j, "fill_area: ", fill_area)
			max_area = max(max_area, fill_area)
	
	return max_area