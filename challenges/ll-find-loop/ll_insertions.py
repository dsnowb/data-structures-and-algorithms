from node import Node
from linked_list import LinkedList as LL

class betterLL(LL):
    def append(self, val):
        """Appends val to tail of linked list"""
        if not self.head:
            self.head = Node(val)
            return self
        cur = self.head
        if not cur._next:
            cur._next = Node(val)
        while cur._next:
            cur = cur._next
        new = Node(val)
        cur._next = new

        self.length += 1
        return self

    def insertBefore(self, val, n_val):
        """Inserts n_val before first occurance of val if val in linked list"""
        if self.head:
            prev = self.head
            if prev.val == val:
                self.head = Node(n_val, prev)
                self.length += 1
                return self
            if prev._next:    
                cur = prev._next
                while cur:
                    if cur.val == val:
                        new = Node(n_val, cur)
                        prev._next = new
                        self.length += 1
                        return self
                    prev = cur
                    cur = cur._next
        return 'Specified value not found.'

    def insertAfter(self, val, n_val):
        """Inserts n_val after first occurance of val if val in linked list"""
        if self.head:
            cur = self.head
            while cur:
                if cur.val == val:
                    new = Node(n_val,cur._next)
                    cur._next = new
                    self.length += 1
                    return self
                cur = cur._next

        return 'Specified value not found.'
