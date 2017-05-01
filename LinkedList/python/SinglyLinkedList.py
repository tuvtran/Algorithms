class Node(object):
  def __init__(self, value=None, nextNode=None):
    self.__value = value
    self.__next = nextNode

  def getValue(self):
    return self.__value

  def getNext(self):
    return self.__next

  def setValue(self, v):
    self.__value = v

  def setNext(self, n):
    self.__next = n

  def __str__(self):
    return str(self.__value) + " -- " + str(self.__next)

class SinglyLL(object):
  def __init__(self):
    self.head = Node()
    self.tail = self.head
    self.size = 0

  def __len__(self):
    return self.size

  def add(self, item, index=0):
    # add to head
    if index < 0 or index > len(self):
      return RuntimeError('Index out of bound')
    if index == 0:
      self.head.setNext(Node(item, self.head.getNext()))
      if self.head == self.tail:
        self.tail = self.head.getNext()
    # add to tail
    elif index == len(self) - 1:
      self.tail.setNext(Node(item))
      self.tail = self.tail.getNext()
    else:
      p = self.head.getNext()
      for i in xrange(index - 1):
        p = p.getNext()
      p.setNext(Node(item, p.getNext()))

    self.size += 1

  def remove(self, index=0):
    item = None
    if index < 0 or index >= len(self):
      return RuntimeError('Index out of bound')
    # remove the head
    if index == 0:
      item = self.head.getNext()
      self.head.setNext(self.head.getNext().getNext())
    # remove the tail
    elif index == len(self) - 1:
      pointer = self.head.getNext()
      while pointer.getNext().getNext():
        pointer = pointer.getNext()
      item = pointer.getNext()
      pointer.setNext(None)
      self.tail = pointer
    else:
      pointer = self.head.getNext()
      for i in xrange(index - 1):
        pointer = pointer.getNext()
      item = pointer.getNext()
      pointer.setNext(pointer.getNext().getNext())

    self.size -= 1
    return item.getValue()

  def get(self, index):
    '''
    Get item at index
    '''
    item = None
    if index < 0 or index >= len(self):
      return RuntimeError("Index out of bound")
    else:
      pointer = self.head.getNext()
      for i in xrange(index):
        pointer = pointer.getNext()
      item = pointer
    return item.getValue()

  def search(self, item):
    '''
    Search for item and return the index
    '''
    if not self.head.getNext():
      return RuntimeError("List is empty. Cannot search")
    else:
      pointer = self.head.getNext()
      index = 0
      while (pointer.getValue() != item):
        pointer = pointer.getNext()
        index += 1
      return index

  def __str__(self):
    return str(self.head.getNext())

if __name__ == "__main__":
  ll = SinglyLL()
  ll.add("Ram")
  ll.add("Rem")
  ll.add("Emily")
  ll.add("Viceroy")
  ll.add("Subaru", len(ll) - 1)
  ll.add("Lulu", 2)
  ll.add("Dan", 4)

  print ll

  print "Remove first element"
  print "Removed: " + ll.remove()
  print ll

  print "Remove last element"
  print "Removed: " + ll.remove(len(ll) - 1)
  print ll

  print "Remove at index 1"
  print "Removed: " + ll.remove(1)
  print ll

  print "Item at index 3 is",
  print ll.get(3)

  print "Search for Emily"
  print ll.search("Emily")

  print "Search for Dan"
  print ll.search("Dan")

  print "Search for Rem"
  print ll.search("Rem")