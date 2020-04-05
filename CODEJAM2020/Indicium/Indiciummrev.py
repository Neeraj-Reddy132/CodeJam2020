# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 06:21:13 2020

@author: neera
"""

import random
from copy import deepcopy
 
 
def rls(n):
    if n <= 0:
        return []
    else:
        symbols = list(range(1, n+1))
        square = _rls(symbols)
        return _shuffle_transpose_shuffle(square)
 
 
def _shuffle_transpose_shuffle(matrix):
    square = deepcopy(matrix)
    random.shuffle(square)
    trans = list(zip(*square))
    random.shuffle(trans)
    return trans
 
 
def _rls(symbols):
    n = len(symbols)
    if n == 1:
        return [symbols]
    else:
        sym = random.choice(symbols)
        symbols.remove(sym)
        square = _rls(symbols)
        square.append(square[0].copy())
        for i in range(n):
            square[i].insert(i, sym)
        return square
 
 
def _to_text(square):
    if square:
        width = max(len(str(sym)) for row in square for sym in row)
        txt = '\n'.join(' '.join("{}".format(sym).rjust(width, " ") for sym in row)
                        for row in square)
    else:
        txt = ''
    return txt
 
 
def _check(square):
    transpose = list(zip(*square))
    assert _check_rows(square) and _check_rows(transpose), \
        "Not a Latin square"
 
 
def _check_rows(square):
    if not square:
        return True
    set_row0 = set(square[0])
    return all(len(row) == len(set(row)) and set(row) == set_row0
               for row in square)
 
 
if __name__ == '__main__':
    T = int(input().strip())
 
    resultArr = []
 
    for x in range(1, T+1):
        n, k = list(map(int, input().strip().split()))
 
        arrayIDX = [n for idx in range(50)]
 
        ltsArr = []
 
        for i in arrayIDX:
            square = rls(i)
            ltsArr.append(square)
            _check(square)
 
        # if possible to have lts of k
        for lts in ltsArr:
            temp = 0
 
            for rIDX in range(len(lts)):
                temp += lts[rIDX][rIDX]
 
            if temp == k:
                result = "POSSIBLE"
                break
            else:
                result = "IMPOSSIBLE"
 
        if result == "POSSIBLE":
            resultArr.append([x, result, _to_text(lts)])
        else:
            resultArr.append([x, result])
 
        print("Case #{}: {}".format(x, result))
 
        if result == "POSSIBLE":
            print(_to_text(lts))