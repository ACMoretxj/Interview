# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from algorithm.hash import HashTable


class TestHash(unittest.TestCase):

    def setUp(self):
        from random import randint
        self.n = 1000
        self.nums = [randint(1, 10086) for _ in range(self.n)]

    def test_hash_table(self):
        ht = HashTable()
        for e in self.nums:
            ht.put(e)
        self.assertTrue(all(ht.get(e) for e in self.nums))


if __name__ == '__main__':
    unittest.main()
