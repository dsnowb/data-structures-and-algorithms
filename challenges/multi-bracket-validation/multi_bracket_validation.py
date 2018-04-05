PAIRS = {'(':')', '[':']', '{':'}'}
'''
def multi_bracket_validation(input, term=None):
    for i, char in enumerate(input):
        
        if char in PAIRS.keys():
            res = multi_bracket_validation(input[i+1:], PAIRS[char])
            # if anything is false kick it all the way back up
            if res[0] is False:
                return res if term is not None else False
            else:
                return res if term is not None else True
            i += res[1]
        
        if char == term:
            return (True, i+1)
'''
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




'''
def multi_bracket_validation(input):
    valid = True
    for i, char in enumerate(input):

        for opener,closer in PAIRS.keys():
            if char == opener:
                valid = multi_bracket_validation(input[i+1:])
            
            if char != PAIRS[term]
                return False
        # If not looking for closer and find closer, set False
        if not term and char in PAIRS.values():
            return False

        # If looking for closer...
        if term:

            # If we find the incorrect closer OR we reach the end of input, set False
            if (char in PAIRS.values() or i == len(input) - 1) and char != PAIRS[term]:
                return False

            # If we find the closer
            if char == PAIRS[term]:
                return i + 1
        
        for opener in PAIRS.keys():    
            if char == opener:
                if i + 1 == len(input):
                    return False

                return multi_bracket_validation(input[i+1:], opener)
'''
