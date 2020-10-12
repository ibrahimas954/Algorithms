import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    h = 0
    for i in range(n + 1):
      if i%2:
        h *= 2
      else:
        h += 1
    return h






utopianTree(3)