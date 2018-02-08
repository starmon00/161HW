import math
import random

def main(S, k):
    print(S)
    print(k)
    if k <= len(S):
        counter = 0
        mid = math.floor(len(S)/2)
        distance = math.floor(k/2)
        print(counter)

    


def quickselect(items, item_index):

    def select(lst, l, r, index):

        if r == l:
            return lst[l]

        pivot_index = random.range(l, r)

        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        i = l
        for j in xrange(l+1, r+1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[i], lst[l] = lst[l], lst[i]

        if index == i:
            return lst[i]
        elif index < i:
            return select(lst, l, i-1, index)
        else:
            return select(lst, i+1, r, index)

    if items is None or len(items) < 1:
        return None

    if item_index < 0 or item_index > len(items) - 1:
        raise IndexError()

    return select(items, 0, len(items) - 1, item_index)


