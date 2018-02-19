# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def _prime(n):
    from math import sqrt
    for i in range(n, 1, -1):
        if all(i % j for j in range(2, int(sqrt(i)))):
            return i


class HashTable:

    def __init__(self, init_size=512):
        self.siz = init_size
        self.table = [[] for _ in range(init_size)]
        self.prime = _prime(init_size)

    def put(self, e):
        index = hash(e) % self.prime
        self.table[index].append(e)

    def get(self, e):
        index = hash(e) % self.prime
        return e in self.table[index]


if __name__ == '__main__':
    from random import randint
    ht = HashTable(init_size=32)
    for i in range(100):
        ht.put(randint(1, 100000000000000))
    print([len(h) for h in ht.table])
