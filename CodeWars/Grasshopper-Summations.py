def summation(num):
	retr_sum = 0
    if num > 0:
    	for i in range(num + 1):
    		retr_sum += i
    print(retr_sum)    

summation(8)