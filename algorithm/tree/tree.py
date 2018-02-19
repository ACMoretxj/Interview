# !/usr/bin/env python3
# -*- coding: utf-8 -*-


class Tree:
    pass


class BTree:

    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def nums2tree(nums):
    """
    Construct a binary tree by preorder sequence.
    :param nums: preorder sequence of the tree to be constructed
    :return: the root of appointed binary tree
    """
    if not nums: return None
    val = nums.pop(0)
    if val is None: return None
    node = BTree(val)
    node.left = nums2tree(nums)
    node.right = nums2tree(nums)
    return node
