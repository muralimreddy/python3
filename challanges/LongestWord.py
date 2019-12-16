import re
def longestWord(t):
    r = re.compile('[,\.!?\[\]]')
    s = r.sub('', t).split()
    b =''
    for k in s:
        if(len(k) > len(b)): b = k
    return b


lw = lambda t: max(re.split('_|\W', t), key = len)



print(longestWord('Ready, steady, go!'))

print(lw('Ready, steady, go!'))