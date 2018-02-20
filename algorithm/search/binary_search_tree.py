# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# from ..tree import BTree
from algorithm.tree import BTree


class BSTree:

    def __init__(self, nums):
        print(nums)
        self.nums = nums[:]
        self.root = None
        for n in self.nums:
            self.insert(n)

    def insert(self, e):
        if not self.root:
            self.root = BTree(e)
            return None
        p, q = self.root, self.root
        while p:
            if p.val > e: q, p = p, p.left
            elif p.val < e: q, p = p, p.right
            else: return None
        node = BTree(e)
        if q.val > e: q.left = node
        else: q.right = node

    def find(self, e):
        p = self.root
        while p:
            if p.val > e: p = p.left
            elif p.val < e: p = p.right
            else: return True
        return False
