# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from ..tree import BTree


class Tree(BTree):

    def __init__(self, val):
        super().__init__(val)
        # balance factor
        self.parent, self.bf = None, 0

    def depth(self):
        """
        计算树高，顺便修改平衡因子
        :return: 树高
        """
        if not self: return 0
        h_left = Tree.depth(self.left)
        h_right = Tree.depth(self.right)
        self.bf = h_left - h_right
        return 1 + max(h_left, h_right)


class AVLTree:

    def __init__(self, nums=None):
        self.root = None
        if nums:
            for e in nums:
                self.insert(e)

    def insert(self, e):
        if not self.root:
            self.root = Tree(e)
            return None
        eye = self.__ins(e)
        if not eye: return None
        self.adjust(eye)

    def delete(self, e):
        pass

    def adjust(self, node):
        if node.bf == 2:
            self.__ll(node) if node.left.bf == 1 else self.__lr(node)
        else: self.__rl(node) if node.right.bf == 1 else self.__rr(node)
        # 再次调整平衡因子
        self.root.depth()

    def __ins(self, e):
        """
        向AVL树中插入e，不进行调整
        :param e:
        :return: 和e最临近的不平衡点
        """
        pre, tmp = self.root, self.root
        while tmp:
            pre = tmp
            tmp = tmp.left if e < tmp.val else tmp.right
        node = Tree(e)
        node.parent = pre
        if e < pre.val: pre.left = node
        else: pre.right = node
        # 实际是调整各个节点的平衡因子
        self.root.depth()
        while abs(pre) <= 1: pre = pre.parent
        return pre

    def __del(self, e):
        pass

    def __ll(self, a):
        """
        TODO: 还有几个节点的父节点没有调整
        :param a:
        :return:
        """
        b = a.left
        a.left, b.right = b.right, a
        if a is self.root:
            a.parent, b.parent = b, None
            self.root = b
        else:
            c = a.parent
            if a is c.left:
                c.left = b
            else: c.right = b
            a.parent, b.parent = b, c

    def __lr(self, a):
        b, c = a.left, a.left.right
        a.left, b.right, c.right, c.left = c.right, c.left, a, b
        if a is self.root:
            pass

    def __rl(self, a):
        pass

    def __rr(self, a):
        pass
