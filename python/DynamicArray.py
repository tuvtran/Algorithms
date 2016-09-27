import ctypes

class DynamicArray(object):
  '''
  DYNAMIC ARRAY CLASS (similar to Python list)
  '''

  def __init__(self):
    self.n = 0 # count actual elements (default is 0)
    self.capacity = 1 # default capacity
    self.A = self.make_array(self.capacity)

  def __len__(self):
    '''
    Return the number of elements sorted in array
    '''
    return self.n

  def __getitem__(self, k):
    '''
    Return element at index k
    '''
    if not 0 <= k < self.n:
      return IndexError('K is out of bounds!') # check if k index is in bounds of array

    return self.A[k]

  def append(self, e):
    '''
    Add element to the end of array
    '''
    if self.n == self.capacity:
      self._resize(2*self.capacity) # double capity if not enough

    self.A[self.n] = e # set self.n index to element
    self.n += 1

  def _resize(self, new_cap):
    '''
    Resize internal array to new_cap
    '''
    B = self.make_array(new_cap) # new bigger array

    for k in range(self.n):
      B[k] = self.A[k]

    self.A = B # Call A the new bigger array
    self.capacity = new_cap # reset the capacity

  def make_array(self, new_cap):
    '''
    returns a new array with new_cap capacity
    '''
    return (new_cap * ctypes.py_object)()