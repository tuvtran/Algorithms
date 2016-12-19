class BinMinHeap(object):
  '''
  Implementation of a min heap
  '''
  def __init__(self):
    self.heapList = [0]
    self.size = 0

  def percUp(self, i):
    '''
    Percolate up
    if the child is less than parent, then swap
    repeat
    '''
    while i // 2 > 0:
      # if the child is less than parent
      # then swap
      if self.heapList[i] < self.heapList[i//2]:
        tmp = self.heapList[i//2]
        self.heapList[i//2] = self.heapList[i]
        self.heapList[i] = temp
      i = i // 2

  def insert(self, k):
    '''
    insert element into the heap and maintain
    the heap property by percolating up
    '''
    self.heapList.append(k)
    self.size += 1
    self.percUp(size)

  def percDown(self, i):
    '''
    Percolate down
    swap the root with its smallest child less than the root
    '''
    while (i * 2) <= self.size:
      # the smaller child
      mc = self.minChild(i)
      if self.heapList[i] > self.heapList[mc]:
        tmp = self.heapList[mc]
        self.heapList[mc] = self.heapList[i]
        self.heapList[i] = tmp
      i = mc

  def minChild(self, i):
    '''
    return the position of the smaller child
    '''
    # if that is a leaf node
    if i * 2 + 1 > self.size:
      return i * 2
    else:
      if self.heapList[i*2] < self.heapList[i*2+1]:
        return i * 2
      else:
        return i * 2 + 1

  def delMin(self):
    '''
    delete the min item in the heap
    '''
    retval = self.heapList[1]
    self.heapList = self.heapList[self.size]
    self.size -= 1
    self.heapList.pop()
    self.percDown(1)
    return retval

  def buildHeap(self, alist):
    i = len(alist) // 2
    self.size = len(alist)
    self.heapList = [0] + alist[:]
    while i > 0:
      self.percDown(i)
      i -= 1