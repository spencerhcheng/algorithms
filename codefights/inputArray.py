#!/usr/bin/python3

"""
On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-105 ≤ inputArray[i] ≤ 105.
"""

def arrayChange(inputArray):
    len_arr = len(inputArray)
    moves = 0

    for idx in range(1, len_arr):
        """
        if values the same, increment idx and moves by 1
        """
        if inputArray[idx] == inputArray[idx - 1]:
            inputArray[idx] += 1
            moves += 1
        """
        if values are different, apply the difference to
        value at idx and increase movements by difference
        """
        if inputArray[idx] < inputArray[idx - 1]:
            diff = abs(inputArray[idx - 1] - inputArray[idx])
            inputArray[idx] += diff + 1
            moves += diff + 1
    return inputArray, moves 

if __name__ == "__main__":
    inputArray = [1, 1, 1]
    print(arrayChange(inputArray))
