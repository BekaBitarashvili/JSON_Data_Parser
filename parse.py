#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    n = len(s)
    count = 0
    for i in range(1, n):
        d = {}
        for j in range(n - i + 1):
            subs = list(s[j:j + i])
            subs.sort()
            subs = ''.join(subs)
            if subs in d:
                count += d[subs]
                d[subs] += 1
            else:
                d[subs] = 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
