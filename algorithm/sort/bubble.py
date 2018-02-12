# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from ..tool import decorate_sort


@decorate_sort
def bubble(nums):
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
