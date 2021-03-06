#https://www.hackerrank.com/challenges/python-time-delta/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(d1, d2):
    print(d1)
    print(d2)
    f= '%a %d %b %Y %H:%M:%S %z'
    d1 = datetime.strptime(d1, f) 
    d2 = datetime.strptime(d2, f) 
    res = True
    try:
        res = bool(d1) or bool(d2)
        diff = (d2-d1).total_seconds()  
        return abs(int(diff))
    except ValueError:
        sys.exit()
    except year > 3000:
        sys.exit()
    
    # for _ in range(int(input())):
    #     print(delta(input(), input()))
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()
    
