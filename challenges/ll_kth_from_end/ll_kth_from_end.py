from ll_insertions import *

class moreBetterLL(betterLL):
    def kthFromEnd(self, k):
        """Returns node object that is k nodes from the tail, 0 indexed"""
        if type(k) != int:
            raise TypeError('Argument must be type <int>')
        if self.length - k < 1 or k < 0:
            raise IndexError('Linked list contains {} elements'.format(self.length))
        cur = self.head
        for i in range(self.length - k - 1):
            cur = cur._next

        return cur
