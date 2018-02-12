# -*- coding: utf-8 -*-
# !/usr/bin/env python3


def decorate_sort(func):
    def inner(nums):
        return func(nums[:])
    return inner
