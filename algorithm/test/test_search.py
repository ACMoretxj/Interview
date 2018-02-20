# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from algorithm.search import bisearch, BSTree
from bisect import bisect
from random import randint, shuffle


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.cases = [([], 0),
                      ([1, 2, 3, 4, 5], 1),
                      ([1, 2, 3, 4, 5], 5),
                      ([1, 2, 3, 4, 5], -1),
                      ([1, 2, 2, 2, 3], 2),
                      (sorted([randint(1, 1000) for _ in range(256)]), randint(1, 1000)),
                      (sorted([-randint(1, 1000) for _ in range(256)]), -randint(1, 1000))]

    def test_binary_search(self):
        flag = True
        for case in self.cases:
            i1 = bisect(case[0], case[1]) - 1
            i2 = bisearch(case[0], case[1])
            if i1 == -1 and i2 == -1: continue
            if case[0][i1] == case[1]:
                if i1 != i2:
                    flag = False
                    break
            elif i2 != -1:
                flag = False
                break
        self.assertTrue(flag)

    def test_binary_search_tree(self):
        flag = True
        for case in self.cases:
            nums, e = case[0][:], case[1]
            shuffle(nums)
            bst = BSTree(nums)
            if bst.find(e) != (e in nums):
                flag = False
                break
        self.assertTrue(flag)


if __name__ == '__main__':
    unittest.main()
