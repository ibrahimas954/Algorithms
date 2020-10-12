import math
import os
import random
import re
import sys

def angryProfessor(k, a):
   counter = 0
   for i in a:
      if i <= 0:
       counter += 1

   if counter < k:
      return "YES"
   else:
      return "NO"


