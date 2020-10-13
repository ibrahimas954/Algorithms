def is_valid_walk(walk):
    x = 0
    y = 0

    if len(walk) == 10:
        for direct in walk:
            if direct == 's':
                y -= 1
            if direct == 'n':
                y += 1
            if direct == 'w':
                x -= 1
            if direct == 'e':
                x += 1
    else:
        return False

    if x == 0 and y == 0:
        return True
    else:
        return False


arr = ['s','n','w','e','s','n','e','w','n','e']
is_valid_walk(arr)