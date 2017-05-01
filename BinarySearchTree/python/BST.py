class TreeNode(object):
  def __init__(self, key, val, left=None, right=None, parent=None):
    self.key = key
    self.payload = val
    self.leftChild = left
    self.rightChild = right
    self.parent = parent

  def hasLeftChild(self):
    return self.leftChild

  def hasRightChild(self):
    return self.rightChild

  def isLeftChild(self):
    return self.parent and self.parent.leftChild == self

  def isRightChild(self):
    return self.parent and self.parent.rightChild == self

  def isRoot(self):
    return not self.parent

  def isLeaf(self):
    return not (self.rightChild or self.leftChild)

  def hasAnyChildren(self):
    return self.rightChild or self.leftChild

  def hasBothChildren(self):
    return self.rightChild and self.leftChild

  def replaceNodeData(self, key, value, lc, rc):
    self.key = key
    self.payload = value
    self.leftChild = lc
    self.rightChild = rc
    if self.hasLeftChild():
      self.leftChild.parent = self
    if self.hasRightChild():
      self.rightChild.parent = self

class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.size = 0

  def length(self):
    return self.size

  def __len__(self):
    return self.size

  def __iter__(self):
    return self.root.__iter__()

  def put(self, key, val):
    '''
    Add a key to the tree
    '''
    # if there is a root, call the private helper function
    if self.root:
      self._put(key, val, self.root)
    # add a new node to the root
    else:
      self.root = TreeNode(key, val)
    self.size += 1

  def _put(self, key, val, currentNode):
    '''
    Add a key to the tree
    if there already exists the root
    '''
    # if key is less than the currentNode's, 
    if key < currentNode.key:
      # traverse the left subtree
      if currentNode.hasLeftChild():
        self._put(key, val, currentNode.leftChild)
      # add the new node to the left subtree
      else:
        currentNode.leftChild = TreeNode(key, val, parent=currentNode)
    else:
      # traverse the right subtree
      if currentNode.hasRightChild():
        self._put(key, val, currentNode.rightChild)
      # add the new node to the right subtree
      else:
        currentNode.rightChild = TreeNode(key, val, parent=currentNode)

  def __setitem__(self, k, v):
    self.put(k, v) 

  def get(self, key):
    # check if there is a root
    if self.root:
      # call the private _get method on the root
      res = self._get(key, self.root)
      if res:
        return res.payload
      else:
        return None
    # else returns None
    else:
      return None

  def _get(self, key, currentNode):
    if not currentNode:
      return None
    elif currentNode.key == key:
      return currentNode
    elif key < currentNode.key:
      # traverse the left subtree if the targeted key is less than the current key
      return _get(key, currentNode.leftChild)
    else:
      # traverse the right subtree otherwise
      return _get(key, currentNode.rightChild)

  def __getitem__(self, key):
    return self.get(key)

  def __contains__(self, key):
    if self._get(key, self.root):
      return True
    else:
      return False

  def delete(self, key):
    '''
    The delete method does the followign thing:
    - check if the tree size > 1
      if yes then start looking for the key and delete it
      if no then check the following two cases
      - if the target key == root's key, then set root to None
      - if target key != then raise a key error
    '''
    if self.size > 1:
      # get the key with get() method
      nodeToRemove = self._get(key, self.root)
      if nodeToRemove:
        # if it exists
        self.remove(nodeToRemove)
        self.size = self.size - 1
      else:
        # if it does not exist
        raise KeyError('Error! Key not in tree')
    elif: self.size == 1 and self.root.key == key:
      self.root = None
      self.size = self.size - 1
    else:
      raise KeyError('Error! Key not in tree')

  def __delitem__(self, key):
    self.delete(key)

  def remove(self, currentNode):
    '''
    There are 3 cases:
    - The node to be deleted has no children => just simply delete the node
    - The node to be deleted has 1 child => promote its child to take its place
    - The node to be deleted has 2 children => find the next successor to take its place
    '''
    # Case 1
    if currentNode.isLeaf(): 
      # if it's the left child of its parent
      if currentNode.isLeftChild():
        currentNode.parent.leftChild = None
      # if it's the right child of its parent
      else:
        currentNode.parent.rightChild = None
    # Case 3
    elif currentNode.hasBothChildren():
      # find the successor
      succ = currentNode.findSuccessor()
      # remove the successor
      succ.spliceOut()
      currentNode.key = succ.key
      currentNode.payload = succ.payload
    # Case 2
    else: # this node has one child
      if currentNode.hasLeftChild():
        if currentNode.isLeftChild():
          currentNode.leftChild.parent = currentNode.parent
          currentNode.parent.leftChild = currentNode.leftChild
        elif currentNode.isRightChild():
          currentNode.leftChild.parent = currentNode.parent
          currentNode.parent.rightChild = currentNode.leftChild
        else:
          currentNode.replaceNodeData(currentNode.leftChild.key,
                          currentNode.leftChild.payload,
                          currentNode.leftChild.leftChild,
                          currentNode.leftChild.rightChild)
      else:
        if currentnode.isleftchild():
          currentnode.rightchild.parent = currentnode.parent
          currentnode.parent.leftchild = currentnode.rightchild
        elif currentnode.isrightchild():
          currentnode.rightchild.parent = currentnode.parent
          currentnode.parent.rightchild = currentnode.rightchild
        else:
          currentnode.replacenodedata(currentnode.rightchild.key,
                            currentnode.rightchild.payload,
                            currentnode.rightchild.leftchild,
                            currentnode.rightchild.rightchild)