#!/usr/bin/env python3

import json

class Node:
    def __init__(self, parent, val, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.val = val

def main():    
    with open("input.txt") as infile:
        current_sfn = json.loads(infile.readline())
        current_root = Node(None, current_sfn)
        make_tree(current_root)
        for line in infile.readlines():
            next_sfn = json.loads(line)
            next_root = Node(None, next_sfn)
            make_tree(next_root)
            root = Node(None, val=[current_root.val, next_root.val], left=current_root, right=next_root)
            current_root.parent = root
            next_root.parent = root
            is_reduced = False
            while not is_reduced:
                did_explode = True
                while did_explode:
                    did_explode = do_explode(root)
                did_split = do_split(root)
                is_reduced = not did_explode and not did_split
            current_root = root
    print(magnitude(current_root))

def do_explode(node):
    s = []
    depth = 0
    while True:
        if node:
            if depth >= 4 and node.left and node.right and type(node.left.val) == int and type(node.right.val) == int:
                explode(node)
                return True
            s.append((node, depth))
            node = node.left
            depth += 1
        elif s:
            node, depth = s.pop()
            node = node.right
            depth += 1
        else:
            return False    

def do_split(node):
    s = []
    while True:
        if node:
            if type(node.val) == int and node.val >= 10:
                split(node)
                return True
            s.append(node)
            node = node.left
        elif s:
            node = s.pop()
            node = node.right
        else:
            return False   

def split(node):
    oldval = node.val
    newleft = node.val // 2
    newright = newleft + node.val % 2
    node.val = [newleft, newright]
    node.left = Node(node, newleft)
    node.right = Node(node, newright)

def explode(node):
    vl = node.left.val
    vr = node.right.val
    
    if node == node.parent.left:
        right_neighbor = node.parent.right
        while type(right_neighbor.val) != int:
            right_neighbor = right_neighbor.left
        right_neighbor.val += vr

        ancestor = node.parent
        child = node
        while ancestor.parent and child == ancestor.left:
            child = ancestor
            ancestor = ancestor.parent
        if ancestor.left != child:
            left_neighbor = ancestor.left
            while type(left_neighbor.val) != int:
                left_neighbor = left_neighbor.right
            left_neighbor.val += vl

    elif node == node.parent.right:
        left_neighbor = node.parent.left
        while type(left_neighbor.val) != int:
            left_neighbor = left_neighbor.right
        left_neighbor.val += vl

        ancestor = node.parent
        child = node
        while ancestor.parent and child == ancestor.right:
            child = ancestor
            ancestor = ancestor.parent
        if ancestor.right != child:
            right_neighbor = ancestor.right
            while type(right_neighbor.val) != int:
                right_neighbor = right_neighbor.left
            right_neighbor.val += vr
    
    node.left = None
    node.right = None
    node.val = 0

def magnitude(node):
    if type(node.val) == int:
        return node.val
    else:
        return 3 * magnitude(node.left) + 2 * magnitude(node.right)

def make_tree(node):
    node.left = Node(node, val = node.val[0])
    node.right = Node(node, val = node.val[1])
    if type(node.val[0]) == list:
        make_tree(node.left)
    if type(node.val[1]) == list:
        make_tree(node.right)

# helper, not used in solution
def print_sfn(node, depth):
    if node:
        print_sfn(node.left, depth + 1)
        if not node.left and not node.right:
            print(node.val, end='')
            depth -= 1
        print_sfn(node.right, depth + 1)

if __name__ == "__main__":
    main()