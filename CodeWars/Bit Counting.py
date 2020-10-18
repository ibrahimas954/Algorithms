def count_bits(n):
	if n == 0:
		return 0

	if n > 0:
	   counter = 0
	   while (n):
	   	 n &= (n-1)
	   	 counter += 1
	return counter

print(count_bits(9))