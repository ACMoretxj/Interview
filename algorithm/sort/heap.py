# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from ..tool import decorate_sort


def __sink(nums, i, siz=None):
    if siz is None: siz = len(nums)
    j = i * 2 + 1
    if j >= siz: return None
    if j < siz - 1:
        if nums[j + 1] > nums[j]:
            j += 1
    if nums[j] > nums[i]:
        nums[i], nums[j] = nums[j], nums[i]
    __sink(nums, j, siz)


def __float(nums, i):
    pass


@decorate_sort
def __sink_heap(nums):
    for i in range(len(nums) // 2 - 1, -1, -1):
        __sink(nums, i)
    n = len(nums) - 1
    while n > 0:
        nums[0], nums[n] = nums[n], nums[0]
        __sink(nums, 0, n)
        n -= 1
    return nums


heap = __sink_heap
