import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v2 > v1:
       return "NO"
    else:
        if v2 - v1 == 0:
           return "NO"
        else:
           result = (x1 - x2) % (v2 - v1)
        if result == 0:
           return 'YES'
        else:
           return 'NO'


kangaroo(0,3,4,2)


