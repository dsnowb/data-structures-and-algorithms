from node import Node
from queue import Queue

class Dog(object):
    def __init__(self):
        self.val = 'dog'


class Cat(object):
    def __init__(self):
        self.val = 'cat'


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
        if not isinstance(val, Dog) and not isinstance(val, Cat):
            raise TypeError('argument must type <Dog> or <Cat>')
        
        if self.back:
            self.back._next = Node(val)
            self.back = self.back._next
        else:
            self.back = Node(val)
            self.front = self.back
        
        return val

    def dequeue(self,val=None):
        '''Remove and appropriate node.'''
        if val and not isinstance(val, Dog) and not isinstance(val, Cat):
            raise TypeError('optional argument must be \'dog\' or \'cat\'')

        if self.front:
            if type(self.front.val) == type(val) or not val:
                cur = self.front
                self.front = self.front._next
                return cur

            if not self.front._next:
                    return None
            
            cur = self.front._next
            prev = self.front
            while cur:
                if type(cur.val) == type(val):
                    prev._next = cur._next
                    return cur
                prev = cur
                cur = cur._next
