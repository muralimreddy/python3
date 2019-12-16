'''
Implement a function that can reduce a fraction.

Example

For fraction = [2, 6], the output should be
fractionReducing(fraction) = [1, 3];
For fraction = [4, 1], the output should be
fractionReducing(fraction) = [4, 1].


Input: fraction: [2, 6]
Expected Output: [1, 3]

Input: fraction: [4, 1]
Expected Output: [4, 1]

Input: fraction: [5, 10]
Expected Output: [1, 2]
'''
def gcd(m,n):
    return gcd(abs(m-n), min(m, n)) if (m-n) else n

def fractionReducing(f):
    c = list(f)
    c.sort()
    d = gcd(c[0], c[1])
    for i, v in enumerate(f):
        f[i] = v // d
    return f



fraction = [6, 15]
print(fractionReducing(fraction))