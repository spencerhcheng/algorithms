#!/usr/bin/python3

"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""
def addBorder(picture):
    padding = '*' * (len_picture[0] + 2)

    for idx in range(len(picture)):
        picture[idx] = '*' + picture[idx] + '*'
    picture.insert(0, padding)
    picture.append(padding)
    return picture 

if __name__ == "__main__":
    picture = ["abc", "ded"]
    print(addBorder(picture))
