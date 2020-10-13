def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0

    for i in range(len(apples)):
        if s <= a + apples[i] <= t:
            count_apples += 1
    for i in range (len(oranges)):
        if s <= b + oranges[i] <=t:
            count_oranges += 1
    print(count_apples)
    print(count_oranges)