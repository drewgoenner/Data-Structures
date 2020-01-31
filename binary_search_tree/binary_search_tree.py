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
        #if there is a node, continue moving to the left until you hit the end
        if node:
            self.in_order_print(node.left)
        #print the value of the lowest node
            print(node.value)
        #move back to the right, printing each node until you get to the highest node
            self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #establish the queue and set it's initial
        queue = Queue()
        current = node
        queue.enqueue(current)
        values = ''
        #while the queue exists, drop an item from the queue and print its value
        while queue.size > 0:
            current = queue.dequeue()
            print(current.value)
        #if there is a left branch, travel down it adding to queue
            if current.left:
                queue.enqueue(current.left)
        #same with the right
            if current.right:
                queue.enqueue(current.right)



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #create the stack and set it to the initial node
        stack = Stack()
        current = node
        stack.push(current)
        #while the stack exists, drop items from it and print their value
        while stack.size > 0:
            current = stack.pop()
            print(current.value)
        #if there are nodes left, add them to stack
            if current.left:
                stack.push(current.left)
        #same with right
            if current.right:
                stack.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        #the preorder traversal will start with the initial node, print it, then travel left, printing until the smallest number, then move back and start taking the right branches
        #if empty, return
        if not node:
            return
        #print the value of the node
        print(node.value)
        #move to the left and repeat
        node.pre_order_dft(node.left)
        #move to the right and repeat
        node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        #the postorder traversal will go to the lowest number, print it, then start moving right and printing those numbers
        #if empty, return
        if not node:
            return
        #move all the way to the left
        node.post_order_dft(node.left)
        #start mmoving right and printing the values of each node until the tree is traversed.
        node.post_order_dft(node.right)
        print(node.value)
