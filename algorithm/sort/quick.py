# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from ..tool import decorate_sort


def __partition(nums, lo, hi):
    tmp, i, j = nums[lo], lo, hi
    while i < j:
        while i < j and nums[j] > tmp: j -= 1
        if i < j: nums[i] = nums[j]
        while i < j and nums[i] <= tmp: i += 1
        if i < j: nums[j] = nums[i]
    nums[i] = tmp
    return i


def __qsort(nums, lo, hi):
    if lo >= hi: return None
    mid = __partition(nums, lo, hi)
    __qsort(nums, lo, mid - 1)
    __qsort(nums, mid + 1, hi)


@decorate_sort
def quick(nums):
    __qsort(nums, 0, len(nums) - 1)
    return nums
