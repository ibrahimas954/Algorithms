def accum(s):
    for i in range(len(s)):
        if i == 0:
            return s[i].upper()
        else:
            return s[i] * i


accum("ZpglnRxqenU")

