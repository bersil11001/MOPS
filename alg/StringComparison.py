
from alg.TokenTypeComparison import comparison as base_comparison
from cgitb import reset
from posixpath import split

def split(list, k: int):
    result = []

    for start in range(len(list) - k + 1):
        r = ''
        for i in range(k):
            r += list[start + i]
        result.append(r)
        
    return result

def hashs(list):
    return [hash(list[i]) for i in range(len(list))]
    
def min_index(list, start, length):
    result = start
    min_value = list[result]
    for i in range(start+1, start+length):
        value = list[i]
        if value <= min_value:
            min_value = value
            result = i
    return result


def mins(list, w:int):
    result = []
    g_index = -1
    for start in range(len(list) - w + 1):
        index = min_index(list, start, w)
        if index != g_index:
            g_index = index
            result.append(list[index])
    return result

def compress(list, k, w):
    list = split(list, k)
    list = hashs(list)
    list = mins(list, w)
    return list

def comparison(first, second, k = 5, w = 4):
    first = compress(first, k, w)
    second = compress(second, k, w)

    return base_comparison(first, second)
