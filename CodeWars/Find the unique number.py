def find_uniq(arr):
    arr.sort()

    if arr[0] < arr[len(arr) - 1] and arr[0] < arr[len(arr) - 2]:
             num = arr[0]
    else:
        num = arr[len(arr) - 1]

    return num





test_arr = [ 3, 10, 3, 3, 3 ]
x = find_uniq(test_arr)
print(x)
##max_num = max(arr)
   # empty_arr = []
    #for element in arr:
     #   if max_num = element:
      #     empty_arr.append(element)
       #    arr.remove(element)
    #print(empty_arr,arr)