import math
import os
import random
import re
import sys

def beautifulDays(i, j, k):
    arr = []
    count = 0

    while i <= j:
      arr.append(i)
      i += 1

    for element in arr:
     rev_num = str(abs(element))
     rev_num = rev_num.strip()
     rev_num = int(rev_num[::-1])

     #output = int(rev_num)
     if (element - rev_num) / k == int((element - rev_num) / k ):
        count += 1
    print(count)


beautifulDays(20,23,6)
