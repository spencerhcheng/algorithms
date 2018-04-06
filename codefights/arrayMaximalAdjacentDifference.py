#!/usr/bin/python3

"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 10,
-15 ≤ inputArray[i] ≤ 15.

[output] integer

The maximal absolute difference.
"""

def maxDiff(arr):
    max_diff = float('-inf')

    for idx in range(1, len(arr)):
        max_diff = max(max_diff, abs(arr[idx] - arr[idx - 1]))
    return max_diff

if __name__ == "__main__":
    arr = [2, 4, 1, 0]
    print(maxDiff(arr))
