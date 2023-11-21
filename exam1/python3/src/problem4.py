'''
Distribution file of the kmers problem.
'''

from typing import List

def kmers(seq: str, k: int, k_mers: List[str]) -> List[int]:
    '''
    Takes in a sequence of letters, a kmer length, and a list of k-mers and
    returns a list of the counts of each k-mer in the sequence.

    Parameters:
        -   seq (str): A string of letters
        -   k (int): The length of the k-mers
        -   k_mers (list): A list of k-mers

    Returns:
        -   k_mer_counts (list): A list of the counts of each k-mer in the
            sequence. The counts should be in the same order as the k-mers in
            the k_mers list.
    '''
    i = 0
    kmers = {}
    result = []
    while i < len(seq)-(k-1):
        if seq[i:i+k] not in kmers:
            kmers[seq[i:i+k]] = 0
        if seq[i:i+k] in kmers:
            kmers[seq[i:i+k]] += 1
        i += 1
    
    for x in k_mers:
        if x in kmers:
            result.append(kmers[x])
        else:
            result.append(0)

    return result