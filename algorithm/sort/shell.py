# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from ..tool import decorate_sort


def __step_insert(nums, step):
    for i in range(0, len(nums), step):
        for j in range(0, i, step):
            if nums[j] > nums[i]:
                tmp = nums[i]
                for k in range(i, j, -step):
                    nums[k] = nums[k - step]
                nums[j] = tmp
                break


@decorate_sort
def shell(nums):
    steps = [7, 5, 3, 1]
    for step in steps:
        __step_insert(nums, step)
    return nums
