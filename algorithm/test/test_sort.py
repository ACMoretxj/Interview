# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import unittest
from algorithm.sort import *


class TestSort(unittest.TestCase):

    def setUp(self):
        from random import randint
        self.nums_list = [
            [], [0], [1, 2], [1, 2, 3], [1] * 100,
            [range(1, 100)], [range(99, -1, -1)],
            [randint(1, 200) for _ in range(100)],
            [randint(1, 10) for _ in range(100)]
        ]

    def __check(self, func):
        return all(tuple(func(nums)) == tuple(sorted(nums)) for nums in self.nums_list)

    def test_bubble(self):
        self.assertTrue(self.__check(bubble))

    def test_insert(self):
        self.assertTrue(self.__check(insert))

    def test_shell(self):
        self.assertTrue(self.__check(shell))

    def test_quick(self):
        self.assertTrue(self.__check(quick))

    def test_heap(self):
        self.assertTrue(self.__check(heap))

    def test_merge(self):
        self.assertTrue(self.__check(merge))


if __name__ == '__main__':
    unittest.main()
