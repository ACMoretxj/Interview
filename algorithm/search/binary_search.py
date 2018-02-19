# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# from ..tool import decorate_search
from algorithm.tool.decorator import decorate_search


@decorate_search
def bisearch(nums, e):
    if not nums: return -1
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > e: hi = mid
        else: lo = mid + 1
    return lo - 1 if nums[lo - 1] == e else -1


if __name__ == '__main__':
    a = []
    print(bisearch(a, 3))
