from stack import Stack


def towers_of_hanoi(n):
    '''Solves tower of hanoi by setting up stacks, then calling recursive'''
    def recursive(n, source, dest, spare):
        nonlocal s
        if n == 0:
            dest.push(source.pop)
            s.append('Move Disc #{}'.format(n))
        else:
            recursive(n-1, source, spare, dest)
            dest.push(source.pop)
            s.append('Move Disc #{}'.format(n))
            recursive(n-1, source, dest, spare)
        if type(n) is not int:
            raise TypeError('argument must be of type <int>')

    s = []
    stack_one = Stack([i for i in range(n - 1)])
    stack_two = Stack()
    stack_three = Stack()
    recursive(n-1, stack_one, stack_two, stack_three)
    return s
