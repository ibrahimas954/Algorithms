def sum_of_n(n):
    new_arr = []
    cout = 0 
    if n < 0:
        cout_indx = -1
        n = n - 1
    else:
        cout_indx = 1
        n = n + 1
        
    for i in range(0,n,cout_indx):
        cout += i
        new_arr.append(cout)
    
    return new_arr