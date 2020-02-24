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
