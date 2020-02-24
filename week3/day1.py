"""
문제
두 개의 input에는 복소수(complex number)가 string 으로 주어집니다.
복소수란 a+bi 의 형태로, 실수와 허수로 이루어진 수입니다.

input으로 받은 두 수를 곱해서 반환해주세요.
반환하는 표현도 복소수 형태의 string 이어야 합니다.

복소수 정의에 의하면 (i^2)는 -1 이므로 (i^2) 일때는 -1로 계산해주세요.

* 제곱 표현이 안 되어 i의 2제곱을 (i^2)라고 표현했습니다.

예제 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
설명:
(1 + i) * (1 + i) = 1 + i + i + i^2 = 2i
2i를 복소수 형태로 바꾸면 0+2i.

예제 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
설명:
(1 - i) * (1 - i) = 1 - i - i + i^2 = -2i,
-2i를 복소수 형태로 바꾸면 0+-2i.


예제 3:
Input: "1+3i", "1+-2i"
Output: "7+1i"
설명:
(1 + 3i) * (1 - 2i) = 1 - 2i + 3i -6(i^2) = 1 + i + 6,
7+i를 복소수 형태로 바꾸면 7+1i.


가정
input은 항상 a+bi 형태입니다.
output도 a+bi 형태로 나와야 합니다.
"""
def complexNumberMultiply(a, b):
  """
  :type a: str
  :type b: str
  :rtype: str
  """
  input_a = a.split("+")
  input_b = b.split("+")
  
  i = int(input_a[0])
  j = int(input_a[1][:-1])
  k = int(input_b[0])
  l = int(input_b[1][:-1])
  
  return str(i*k-j*l)+"+"+str(i*l+j*k)+"i"
