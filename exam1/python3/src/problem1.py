'''
Distribution file of the itshotitscold problem.
'''

from typing import List
from typing import Tuple

def itshotitscold(temperatures: List[int]) -> Tuple[int, int, int]:
    '''
    This function takes a list of temperatures. It returns a tuple of
    three integers: the number of times the temperature went down, the
    number of times the temperature remained the same, and the number
    of times the temperature went up.

    Arguments:
        temperatures: a list of integers representing temperatures.

    Returns:
        A tuple of three integers representing the number of times the 
        temperature went down, the number of times the temperature remained the 
        same, and the number of times the temperature went up.

    '''
    i = 1
    up = 0
    down = 0
    same = 0
    while i < len(temperatures):
        if temperatures[i] > temperatures[i-1]:
            up = up + 1
        elif temperatures[i] < temperatures[i-1]:
            down = down + 1
        else:
            same = same + 1
        i = i + 1
    
    return down, same, up
