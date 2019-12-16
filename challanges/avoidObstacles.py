'''
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.

Check out the image below for better understanding:
https://codesignal.s3.amazonaws.com/tasks/avoidObstacles/img/example.png?_tm=1551432749641
'''

x = [1, 4, 10, 6, 2]
ix = lambda k, xs: [i for (y, i) in zip(xs, range(len(xs))) if k == y]

def avoidObstacles(arr):
    sorted(arr)
    m,n,last=1,1,arr[len(arr)-1]
    while m <= last:
        if(len(ix(m,arr) == 0)):
            n




avoidObstacles(x)
