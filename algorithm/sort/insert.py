# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from ..tool import decorate_sort


@decorate_sort
def insert(nums):
    for i, n in enumerate(nums):
        from bisect import bisect
        pos, tmp = bisect(nums, n, hi=i), nums[i]
        for j in range(i, pos, -1):
            nums[j] = nums[j - 1]
        nums[pos] = tmp
    return nums
