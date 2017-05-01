class Node(object):
  def __init__(self, value=None, nextNode=None, prev=None):
    self.__value = value
    self.__next = nextNode
    self.__prev = prev

  def getValue(self):
    return self.__value

  def getNext(self):
    return self.__next

  def getPrev(self):
    return self.__prev

  def setValue(self, v):
    self.__value = v

  def setNext(self, n):
    self.__next = n

  def setPrev(self, p):
    self.__prev = p

class DoublyLL(object):
  def __init__(self):
    self.head = Node()
    self.tail = Node()
    self.head.setNext(self.tail)
    self.head.setPrev(self.head)

  def add(self, item, index=0):
    pass

  def remove(self, index=0):
    pass

  def search(self, item):
    pass

  def get(self, index):
    pass
