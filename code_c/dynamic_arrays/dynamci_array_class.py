print("hello world")
import ctypes

class DynamicArray(object):
    def __init__(self):
        self.n=0
        self.capacity=1
        self.A=self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self,k):
        if not 0 <= k < self.n:
            return IndexError('k is out of bound') 
        return self.A[k]
    
    def append(self,ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity)

