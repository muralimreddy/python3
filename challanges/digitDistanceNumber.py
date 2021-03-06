'''
Let the integer n be represented by digits a1, a2, ..., ak (the digits are listed from left to right in the order they appear in the decimal representation of n).
Define bi = |ai + 1 - ai|.
Construct the number from the digits b1, b2, ..., bk - 1 (in that order). Let's call the resulting value a digit distance number for n.
Example

For n = 2744, the output should be
digitDistanceNumber(n) = 530.

b1 = |a2 - a1| = |7 - 2| = 5
b2 = |a3 - a2| = |4 - 7| = 3
b3 = |a4 - a3| = |4 - 4| = 0
For n = 330, the output should be
digitDistanceNumber(n) = 3.

Formally, it is 03 but leading zeroes should be removed.

For n = 333, the output should be
digitDistanceNumber(n) = 0.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive integer consisting of at least two digits.

Guaranteed constraints:
10 ≤ n ≤ 109.

[output] integer

The digit distance number for n.
'''

def digitDistanceNumber(n):
    n = str(n)
    a = int(n[0])
    c=''
    for x in range(len(n)-1):
        b = a
        a = int(n[x+1])
        c = c+(str(b-a))
    return abs(int(c))




print(digitDistanceNumber(2744))