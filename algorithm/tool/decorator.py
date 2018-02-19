# -*- coding: utf-8 -*-
# !/usr/bin/env python3


def decorate_sort(func):
    def inner(nums):
        return func(nums[:])
    return inner


def decorate_search(func):
    def inner(nums, e):
        return func(nums[:], e)
    return inner
