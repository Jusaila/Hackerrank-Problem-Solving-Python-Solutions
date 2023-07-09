#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    left = []
    right = []
    equal = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > equal:
            right.append(arr[i])
        elif arr[i] < arr[0]:
            left.append(arr[i])
        
    return left + [equal] + right

or

def quickSort(arr):
    left = [i for i in arr if i < arr[0]]
    right = [i for i in arr if i > arr[0]]
    equal = [i for i in arr if i == arr[0]]
    return left + equal + right
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
