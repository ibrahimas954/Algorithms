def unique_in_order(iterable):
    pre_item = None
    result = []
    for item in iterable:
        if item != pre_item:
            result.append(item)
            pre_item = item
    return result



    previous_element = None
    result_arr = []
    
    for element in iterable:
        if element != previous_element:
            result_arr.append(element)
            previous_item = element
    return result_arr