from node import Node

class Queue(object):
    '''Fifo data structure composed of Node objects.

    Attributes:
        front: Node at front of queue ready to be dequeued.
        back: Node at rear of queue, last node queued.
        length: Number of nodes in the queue.

    '''

    def __init__(self, iterable = []):
        '''Initialize queue and enqueue iterable elements.'''
        self.front = None
        self.back = None
        self.length = 0

        if type(iterable) is dict:
            for k,v in dict.items():
                self.enqueue({k:v})

        try:
            for item in iterable:
                self.enqueue(item)

        except TypeError:
            print('iterable must be of type <iterable>.')
    
    def __repr__(self):
        '''Return Queue object.'''
        return '<{} at {}>'.format(type(self).__name__, hex(id(self)))

    def __str__(self):
        '''Return visualization of queue.'''
        s = '(FRONT)'
        cur = self.front
        if cur:
            while cur._next:
                s += ' {} =>'.format(cur.val)
                cur = cur._next
        return s + ' {} (BACK)'.format(cur)

    def __len__(self):
        '''Return number of items in queue.'''
        return self.length

    def enqueue(self,val):
        '''Add val to back of the queue.'''
        if self.back:
            self.back._next = Node(val)
            self.back = self.back._next
        else:
            self.back = Node(val)
            self.front = self.back

        self.length += 1
        return self.length

    def dequeue(self):
        '''Remove and return node at front of queue.'''
        if self.front:
            cur = self.front
            self.front = self.front._next
            self.length -= 1
            return cur
