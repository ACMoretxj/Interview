# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# from ..tool import decorate_sort
from algorithm.tool import decorate_sort


def __merge_sort(nums, lo=None, hi=None):
    if lo is None: lo = 0
    if hi is None: hi = len(nums) - 1
    if lo >= hi: return None
    if lo + 1 == hi:
        if nums[lo] > nums[hi]:
            nums[lo], nums[hi] = nums[hi], nums[lo]
        return None

    mid = (lo + hi) // 2
    __merge_sort(nums, lo, mid - 1)
    __merge_sort(nums, mid, hi)

    dest = [0] * (hi - lo + 1)
    i, j, k = lo, mid, 0
    while i < mid and j <= hi:
        if nums[i] <= nums[j]:
            dest[k] = nums[i]
            i += 1
        else:
            dest[k] = nums[j]
            j += 1
        k += 1
    while i < mid:
        dest[k] = nums[i]
        i, k = i + 1, k + 1
    while j <= hi:
        dest[k] = nums[j]
        j, k = j + 1, k + 1
    for i in range(lo, hi + 1):
        nums[i] = dest[i - lo]


@decorate_sort
def merge(nums):
    __merge_sort(nums)
    return nums


if __name__ == '__main__':
    ns = [5, 4, 3, 2, 1]
    print(merge(ns))
