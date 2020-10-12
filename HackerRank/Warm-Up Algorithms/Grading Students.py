def FindIntersection(strArr):

  first_arr = strArr[0].split(", ")
  second_arr = strArr[1].split(", ")
  return_arr = []

  for element in first_arr:
      if element in second_arr:
        return_arr.append(element)

  if len(return_arr) > 0:
    return ",".join(return_arr)
  else:
    return False




test_Array = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
FindIntersection(test_Array)