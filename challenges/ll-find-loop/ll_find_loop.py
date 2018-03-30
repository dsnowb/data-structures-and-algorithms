from ll_kth_from_end import moreBetterLL as mbll

class smartLL(mbll):
    """
    Checks self for the presence of a loop, i.e. the tail
    pointer points to a node in the list instead of null
    """
    def hasLoop(self):
        if not self.head:
            return False
        cur_a = self.head
        cur_b = self.head
        while cur_a._next and cur_a._next._next:
            if cur_a._next == cur_b:
                return True
            cur_a = cur_a._next._next
            if cur_a == cur_b:
                return True
            cur_b = cur_b._next
            
        return False
