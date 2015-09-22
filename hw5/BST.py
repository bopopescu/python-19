#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #5
# October 1, 2014
# BST
#---------------------------------------------------------


class Node:
    #Constructor Node() creates node
    def __init__(self,word):
        self.left = None
        self.right = None
        self.parent = None
        self.word = word
        self.count = 1

class BSTree:
    #Constructor BSTree() creates empty tree
    def __init__(self, root=None):
        self.root = root
    
    #Find word in tree
    def find(self, word):
        return _find(self.root, word)
    
    #Add node to tree with word
    def add(self, word):
        if not self.root:
            self.root = Node(word)
            return
        _add(self.root, word)

    #Print in order entire tree
    def inOrderPrint(self):
        _inOrderPrint(self.root)

    def size(self):
        return _size(self.root)

    def height(self):
        return _height(self.root)
    
    # def height(self):
    #     if not self.root:
    #         return "This tree is empty"
    #     else:    
    #         return _height(self.root)


#Function to add node with word as word attribute
def _add(root, word):
    if root.word == word:
        root.count += 1
        return
    if root.word > word:
        if root.left == None:
            root.left = Node(word)
        else:
            _add(root.left, word)
    else:
        if root.right == None:
            root.right = Node(word)
        else:
            _add(root.right, word)

#Function to find word in tree
def _find(root, word):
    if not root:
        return -1
    elif root.word == word:
        return root
    elif root.word < word:
        return _find(root.right, word)
    elif root.word > word:
        return _find(root.left, word)

#Function to print tree in order
def _inOrderPrint(root):
    if not root:
        return
    _inOrderPrint(root.left)
    print root.word
    _inOrderPrint(root.right)

#Get number of nodes in tree
def _size(root):
    left = 0
    right = 0

    if root:
        if root.left:
            left = _size(root.left)
        if root.right:
            right = _size(root.right)
        
        return 1 + left + right
    else:
        return 0

#Get height of tree
def _height(root):
    if not root or (not root.left and not root.right):
        return 0
    else:
        return 1 + max(_height(root.left), _height(root.right))


















