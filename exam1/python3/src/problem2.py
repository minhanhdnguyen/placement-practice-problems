'''
Distribution file of the raindrops problem.
'''

from typing import List
from typing import Union

def raindrops(measurements: List[int]) -> Union[int, None]:
    '''
    Computes the average rainfall given a list of measurements. The function
    only considers measurements that are greater than or equal to 0. If only
    negative measurements are given, the function returns None.

    Arguments:
        measurements: A list of measurements.

    Returns:
        The average rainfall as a rounded down integer. If only negative
        measurements are given, the function returns None.
    '''
    lst = []
    for x in measurements:
        if x > 0:
            lst.append(x)
    if lst == []:
        return None
    else:
        return int(sum(lst)/len(lst))
