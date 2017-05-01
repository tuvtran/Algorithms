class Node(object):
  """docstring for Node"""
  def __init__(self, root, left=None, right=None):
    self.root = root
    self.left = left
    self.right = right

  def setLeftChild(self, obj):
    self.left = obj

  def setRightChild(self, obj):
    self.right = obj

  def getLeftChild(self):
    return self.left

  def getRightChild(self):
    return self.right

  def setRootVal(self, val):
    self.root = val

  def getRootVal(self):
    return self.root

class BinaryTree(object):
  def __init__(self, value):
    self.root = Node(value)
    self.size = 1

  
    