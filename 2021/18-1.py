import os
import sys
import json
from functools import reduce

filename = __file__[:-5] + '-input'


class SnailFish:
    def __init__(self, parent, l, depth, left_child):
        self.left = None
        self.right = None
        self.data = 0
        self.left_child = left_child

        self.depth = depth
        self.parent = parent

        if type(l) == list:
            self.left = SnailFish(self, l[0], depth+1, True)
            self.right = SnailFish(self, l[1], depth+1, False)
        elif type(l) == int:
            self.data = l
        else:# if we already made it into snailfish
            self.left = l[0]
            self.left.increase_depth()
            self.left.left_child = True
            self.left.parent = self

            self.right = l[1]
            self.right.increase_depth()
            self.right.left_child = False
            self.right.parent = self

    def increase_depth(self):
        self.depth += 1
        if self.left:
            self.left.increase_depth()
        if self.right:
            self.right.increase_depth()

    def split(self):
        if self.left == None and self.right == None:
            if self.data > 9:
                self.left = SnailFish(self, self.data//2, self.depth+1, True)
                self.right = SnailFish(self, (self.data+1)//2, self.depth+1, False)
                self.data = 0
                return True
            return False
        else:
            l_changed = self.left.split()
            if l_changed:
                return True
            r_changed = self.right.split()
            if r_changed:
                return True
            return False



    def explode(self):
        if self.left == None or self.right == None:
            return False

        if self.depth < 4:
            l_changed = self.left.explode()
            if l_changed:
                return  True
            r_changed = self.right.explode()
            if r_changed:
                return True
            return False
        else:
            self.explode_left(self.left.data)
            self.explode_right(self.right.data)

            self.left = None
            self.right = None
            self.data = 0

            return True

    def explode_left(self, val):
        # finding node by first checking if current node is ever the right child in the tree upwards (stop if current node is None)
        # if so jump to the left child and get the right most leaf going downwards
        # and add teh value to that leaf
        curr = self

        #going up
        while curr != None:
            if not curr.left_child and curr.parent != None:
                curr = curr.parent.left
                break
            else:
                curr = curr.parent
        
        if curr == None:
            return False

        #going down
        while curr.right != None:
            curr = curr.right
        
        curr.data += val
        return True

    def explode_right(self, val):
        # finding node by first checking if current node is ever the left child in the tree upwards (stop if current node is None)
        # if so jump to the right child and get the left most leaf going downwards
        # and add teh value to that leaf
        curr = self

        #going up
        while curr != None:
            if curr.left_child and curr.parent != None:
                curr = curr.parent.right
                break
            else:
                curr = curr.parent
        
        if curr == None:
            return False

        #going down
        while curr.left != None:
            curr = curr.left
        
        curr.data += val
        return True
    
    def calc_magnitude(self):
        if self.left and self.right:
            return 3 * self.left.calc_magnitude() + 2 * self.right.calc_magnitude()
        return self.data


with open(filename) as f:
    lines = f.read().splitlines()
    fish = list(map(lambda l: SnailFish(None, l, 0, False), map(json.loads, lines)))

def redu(l, r):
    root = SnailFish(None, (l, r), 0, False)
    reducing = True
    while reducing:
        reducing = root.explode()
        if reducing:
            continue
        reducing = root.split()
    return root

resulting_snailfish = reduce(lambda l, r: redu(l,r), fish)
            



    


print(resulting_snailfish.calc_magnitude())