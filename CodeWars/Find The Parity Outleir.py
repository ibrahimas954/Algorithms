def find_outlier(integers):
    evens = []
    odds = []

    for i in integers:
        if i %2 == 1:
            odds.append(i)
        if i %2 == 0:
             evens.append(i)

    if len(odds) < len(evens):
       print(odds[0])
    elif len(odds) > len(evens):
        print(evens[0])




arrr = [2, 4, 0, 100, 4, 11, 2602, 36]
find_outlier(arrr)