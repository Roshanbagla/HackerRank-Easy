#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    count = 0
    total_count = 0
    for i in apples:
        total = i + a
        if total >=s and total <= t:
            count = count + 1 
    print(count)
    for j in oranges:
        total_orange = j + b 
        if total_orange >=s and total_orange <= t:
            total_count = total_count + 1 
    print (total_count)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
