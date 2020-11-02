def valid_parentheses(string):
    check_arr = []
    for element in string:
        if element == '(':
            check_arr.append(element)
        elif element == ')':
            try:
                check_arr.pop()
            except:
                return False
            
    if len(check_arr) == 0:
        return True
    else:
        return False