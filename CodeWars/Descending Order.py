def descending_order(num):
    res = [int(x) for x in str(num)]
    new_arr = []
    for element in range(len(res)):
        remove_big_int = max(res)
        new_arr.append(remove_big_int)
        res.remove(remove_big_int)

    str_new_arr = [str(i) for i in new_arr]
    new_arr = int("".join(str_new_arr))

    return new_arr



x=descending_order(12563)
print(x)