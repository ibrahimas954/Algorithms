import os
import sys
import time
from datetime import datetime
#
# Complete the timeConversion function below.
#
c = ''
def timeConversion(s):
    if 'AM' in s and s[:2] != '12':

        return "00" + s[2:-2]

    elif 'AM' in s:

     s = s[:-2]
     return str(12 + int(s[:2])) + s[2:]

    else:
        return s[:-2]


x = timeConversion('05:01:00PM')
print(x)