#!/usr/bin/python3

"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

IPv4 addresses are represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255 inclusive, separated by dots, e.g., 172.16.254.1.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;

For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
isIPv4Address(inputString) = false.

There is no first number.
"""

def isIPv4Address(inputString):
    arr = inputString.split('.')
    if len(arr) != 4:
        return False

    for num in arr:
        if num.isdigit():
            int_n = int(num)
            if int_n < 0 or int_n > 255:
                return False
        else:
            return False
    return True

if __name__ == "__main__":
    inputString = "172.16.254.1"
    print(isIPv4Address(inputString))
