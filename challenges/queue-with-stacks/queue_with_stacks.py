from stack import Stack

class Queue(object):
    '''Implementation of queue with stacks.'''

    def __init__(self):
        '''Create two stack instances, one for enqueuing, one for dequeuing.'''

        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self,val):
        '''Add val to the back of the queue.'''

        if self.in_stack.length:
            self.in_stack.push(val)
        else: 
            while self.out_stack.length:
                self.in_stack.push(self.out_stack.pop().val)

            self.in_stack.push(val)

        return val

    def dequeue(self):
        '''Return val at front of the queue or None if queue empty.'''

        if self.out_stack.length:
            return self.out_stack.pop()

        while self.in_stack.length:
            self.out_stack.push(self.in_stack.pop().val)

        return self.out_stack.pop()
