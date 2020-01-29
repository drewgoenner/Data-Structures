import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is greater or equal to the value of the node, then if there is nothing on the right branch, the leaf becomes the right branch
        if value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
        #otherwise, run insert again on the leaf to the right
            else:
                self.right.insert(value)
        # if the value is less than the value of the node, if there isn't anything on the left branch, the leaf becomes the left branch
        elif value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
        # otherwise, run insert again on the leaf to the left
            else:
                self.left.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if target = the value of the node, return true
        if target == self.value:
            return True
        #if target > the value of the node, move right and repeat
        if target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
        #if target < the value of the node, move left and repeat
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if there isn't a node to the right, return the value of current node
        if self.right == None:
            return self.value
        # otherwise move to the next node to the right and run get_max again
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # run cb on the current node
        cb(self.value)
        # if there is a node to the right, traverse right and run for_each again
        if self.right:
            self.right.for_each(cb)
        # if there's a node to the left, traverse left and run for_each again
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
