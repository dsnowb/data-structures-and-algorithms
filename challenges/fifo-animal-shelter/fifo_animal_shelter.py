from node import Node
from queue import Queue

class AnimalShelter(Queue):
    '''Fifo data structure composed of Node objects.

    Attributes:
        front: Node at front of queue.
        back: Node at rear of queue, last node queued.
        length: Number of nodes in the queue.

    '''

    def __init__(self):
        '''Initialize queue'''
        self.front = None
        self.back = None

    def enqueue(self,val):
        '''Add val to back of the queue.'''
        if val != 'cat' and val != 'dog':
            raise TypeError('argument must be \'dog\' or \'cat\'')
        
        if self.back:
            self.back._next = Node(val)
            self.back = self.back._next
        else:
            self.back = Node(val)
            self.front = self.back
        
        return val

    def dequeue(self,val=None):
        '''Remove and appropriate node.'''
        if val != 'cat' and val != 'dog' and val:
            raise TypeError('optional argument must be \'dog\' or \'cat\'')

        if self.front:
            if self.front.val == val or not val:
                cur = self.front
                self.front = self.front._next
                return cur

            if not self.front._next:
                    return None
            
            cur = self.front._next
            prev = self.front
            while cur:
                if cur.val == val:
                    prev._next = cur._next
                    return cur
                prev = cur
                cur = cur._next
