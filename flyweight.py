#!/usr/bin/python
#coding:utf8
#享元模型，复用id，降低内存使用率

import random
from enum import Enum
from tree import Tree,TreeType

def main():
    rnd = random.Random()
    age_min, age_max = 1, 30
    min_piont, max_point = 0, 100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                rnd.randint(min_piont, max_point),
                rnd.randint(min_piont, max_point)
        )
        tree_counter += 1
    
    for _ in range(3):
        t1 = Tree(TreeType.cherry_tree)
        t1.render(rnd.randint(age_min, age_max),
                rnd.randint(min_piont, max_point),
                rnd.randint(min_piont, max_point)
        )
        tree_counter += 1
    
    for _ in range(5):
        t1 = Tree(TreeType.peach_tree)
        t1.render(rnd.randint(age_min, age_max),
                rnd.randint(min_piont, max_point),
                rnd.randint(min_piont, max_point)
        )
        tree_counter += 1
    
    print(Tree.pool)

if __name__ == '__main__':
    main()