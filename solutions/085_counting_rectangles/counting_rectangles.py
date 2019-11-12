import math

def triangle(n):
    return int(n * (n+1) / 2)

def numSubrectangles(length, width):
    # triangle number of each multiplied together
    # there are (1*length)+(2*(length-1))+(length*1)+... rectangles
    # for a length * 1 rectangle.  In other words, sum of i for i=1,length
    # in other other words, triangle(length)
    # each rectangle that occurs in a length * 1 rectangle
    # can occur in multiple ways in a length * width rectangle
    # each unique subrectangle from the length * 1 rectangle
    # has multiple different widths and positions that it can occur at
    # by thinking about each rectangle in the enter l * w rectangle
    # as projections of l * w and a l*1 and 1*w rectangle, it's clear
    # that there are triangle(length) rectangles, each of which has
    # triangle(width) configurations in the rectangle (or vice versa)
    # In other words, there are triangle(length) * triangle(width) rectangles
    return triangle(length) * triangle(width)


def findDiff(length, width, n):
    return abs(n - numSubrectangles(length, width))


def findClosestTo(n):
    start = math.floor(1/2*(math.sqrt(8*math.sqrt(n)+1)-1))
    start2 = math.floor(1/2*(math.sqrt(8*math.sqrt(n)+1)+1))
    i = start
    j = start
    closest = (i,j)
    closestDiff = findDiff(i, j, n)

    while i > 0:
        currentDiff = findDiff(i, j, n)
        if currentDiff < closestDiff:
            closest = (i, j)
            closestDiff = currentDiff
        downRowDiff = findDiff(i-1, j, n)
        # if we get closer, move there
        if downRowDiff < currentDiff:
            i -= 1
        # if we get farther, move to the next column
        else:
            j += 1
    return closest[0] * closest[1]


#print(findClosestTo(300))
print(findClosestTo(2 * 10 ** 6))
