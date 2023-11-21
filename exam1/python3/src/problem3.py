'''
Distribution file for the tricky problem.
'''

from typing import List

def replace(lst):
    for i, _ in enumerate(lst):
        if lst[i] == "J":
            lst[i] = 10
        elif lst[i] == "Q":
            lst[i] = 11
        elif lst[i] == "K":
            lst[i] = 12
        elif lst[i] == "A":
            lst[i] = 13
        else:
            lst[i] = int(lst[i])
    return lst


def tricky(hand1: List[str], hand2: List[str]) -> str:
    '''
    Play a game of Tricky as described in the problem statement.

    Args:
        hand1: List of cards in hand 1.
        hand2: List of cards in hand 2.

    Returns:
        'PLAYER 1 WINS' if player 1 wins, 'PLAYER 2 WINS' if player 2 wins, or 
        'TIE' if the game is a tie. Please refer to the problem statement for
        winning conditions.
    '''
    i = 0
    count = 0
    hand1 = replace(hand1)
    hand2 = replace(hand2)

    while i < len(hand1):
        if hand1[i] > hand2[i]:
            count = count + 1
        elif hand1[i] < hand2[i]:
            count = count - 1
        i = i + 1
    if count > 0:
        return "PLAYER 1 WINS"
    elif count < 0:
        return "PLAYER 2 WINS"
    else:
        return "TIE"