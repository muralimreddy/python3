'''
You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature to it.

Given the starting HTML tag, find the appropriate end tag which your editor should propose.

Example

For startTag = "<button type='button' disabled>", the output should be
htmlEndTagByStartTag(startTag) = "</button>";
For startTag = "<i>", the output should be
htmlEndTagByStartTag(startTag) = "</i>".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string startTag

Guaranteed constraints:
3 ≤ startTag.length ≤ 75.
'''
import re

def htmlEndTagByStartTag(s):
    x = re.split('\W+', s)
    return "</" + x[1] +">"


print(htmlEndTagByStartTag("<button type='button' disabled>"))

print(htmlEndTagByStartTag("<li class='test'>"))
