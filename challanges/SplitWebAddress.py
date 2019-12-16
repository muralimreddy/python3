'''
Address of a website often has the following form: <protocol>://<domain>.com[/<context>] where <protocol>, <domain> and <context> are non-empty strings consisting of lowercase English letters.
Note that there may be no <context> part in an address.

We need an algorithm that splits an address into an array of its parts: <protocol>, <domain> and <context> (if there is one).

Example

For address = "http://codesignal.com", the output should be
splitAddress(address) = ["http", "codesignal"];
For address = "http://stackoverflow.com/questions", the output should be
splitAddress(address) = ["http", "stackoverflow", "questions"].
Input/Output

[execution time limit] 4 seconds (py3)

[input] string address

A valid website address.

Guaranteed constraints:
15 ≤ address.length ≤ 35.

[output] array.string

Address elements <protocol>, <domain> and <context> placed in the given order.
'''

import re

def splitAddress(a):
    x = re.split('\W+', a)
    del x[2]
    return x
'''
    returnList = []
    mylist = address.replace('//','/').replace(':','').split('/')
    for s in mylist:
        if("." in s) :
            returnList.append(s[0: s.index('.')])
        else:
            returnList.append(s)
    return returnList
'''

print(splitAddress("http://codesignal.com/murali"))
