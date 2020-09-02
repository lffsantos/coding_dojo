# https://www.hackerrank.com/challenges/python-sort-sort/problem

import math
import os
import random
import re
import sys
from operator import itemgetter

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# FILEPATH = path = f'{BASE_DIR}/athlete_sort/input.txt'

tests_cases = {
    "[7, 1, 0] [10, 2, 5] [6, 5, 9] [9, 9, 9] [1, 23, 12]": [[5, 3], [10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9], [1]],
    "[7, 1, 0, 5] [10, 2, 5, 8]": [[2, 4], [10, 2, 5, 8], [7, 1, 0, 5], [2]],
    "[7, 1, 0] [10, 2, 5] [9, 9, 9] [1, 23, 12]": [[4, 3], [10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [2]]
}

def athlete_sort(lines):
    n, m = lines[0][0], lines[0][0]
    k = lines[-1][0]
    if (n < 1 and m > 1000) or 0 > k > m:
        assert False
    
    content = sorted(lines[1:-1], key=itemgetter(k))
    return ' '.join(map(str, content))


if __name__ == '__main__':
    # result = []
    # with open(FILEPATH, 'r') as reader:
    #     lines = [list(map(int, line.split())) for line in reader]

    # print(lines)
    for k, v in tests_cases.items():
        assert athlete_sort(v) == k

