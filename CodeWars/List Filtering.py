def filter_list(l):
    retr_list = []
    for i in range(len(l)):
        if isinstance(l[i], int) and l[i] > -1:
        	retr_list.append(l[i])
        	
    return retr_list

c = [1,2,'aasf','1','123',123]
print(filter_list(c))