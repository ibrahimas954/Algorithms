def digital_root(n):   
    str_num = str(n)
    counter = 0

    if len(str_num) == 1:
        return int(str_num)

    for element in str_num:
        counter += int(element)
    str_num = counter

    return digital_root(str_num)

             

print(digital_root(134))

    #number_str = str(n)

    #if len(number_str) == 1:
    #   return int(number_str)
    #count = 0

    #for element in number_str:
    #   count += int(element)
    #number_str = count

    #return digital_root(number_str)
