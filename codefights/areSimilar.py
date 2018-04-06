#!/usr/bin/python3

"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
"""

def areSimilar(a, b):
    mismatch = []

    """
    Record idx position where elements
    btwn lists a and b do not coincide
    """
    for idx in range(len(a)):
        if a[idx] != b[idx]:
            mismatch.append(idx)
    len_m = len(mismatch)

    if len_m == 0:
        return True

    if len_m > 2:
        return False

    """
    Check if elements swapped in one match
    elements in other list
    """
    if len_m == 2:
        return [a[mismatch[0]], a[mismatch[1]]] == [b[mismatch[1]], b[mismatch[0]]]

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [3, 2, 1]
    print(areSimilar(a, b))
