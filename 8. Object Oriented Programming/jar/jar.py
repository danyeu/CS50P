class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return ("🍪" * self.size)


    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("cookie overflow")
        else:
            self.size = self.size + n


    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("not enough cookies")
        else:
            self.size = self.size - n


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int):
            raise ValueError("invalid capacity type")
        if capacity < 0:
            raise ValueError("invalid capacity value")
        self._capacity = capacity


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise ValueError("invalid size type")
        if size < 0:
            raise ValueError("invalid size value")
        if size > self.capacity:
            raise ValueError("size exceeds capacity")
        self._size = size