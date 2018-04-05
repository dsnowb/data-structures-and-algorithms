PAIRS = {'(':')', '[':']', '{':'}'}

def multi_bracket_validation(input):
    '''Validate grouping characters are valid in a string'''
    if type(input) is not str:
        raise TypeError

    OPENERS = ['(', '[', '{']
    CLOSERS = [')', ']', '}']
    COUNTERS = [0, 0, 0]

    for i in range(len(input)):
        for j in range(len(COUNTERS)):
            if input[i] == OPENERS[j]:
                COUNTERS[j] += 1
            elif input[i] == CLOSERS[j]:
                COUNTERS[j] -= 1
            if COUNTERS[j] < 0: return False

    for counter in COUNTERS:
        if counter != 0:
            return False
    
    return True
