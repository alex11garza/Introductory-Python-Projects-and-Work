#  File: Interval.py
#  Description: A basic interval class.
#  Student Name: Alex Garza 
#  Student UT EID: ang3489
#  Course Name: CS 313E

import sys

class IntegerInterval(object):
    # constructor with default values
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    # creates a string representation of an Interval
    def __str__(self):
        return f"start: {self.start}, end: {self.end}"

    # returns the length of this interval
    # returns an integer
    def __len__(self):
        return self.end - self.start 

    # test for equality between two intervals
    # returns a Boolean
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    # determines if this interval intersects with another
    # returns a boolean
    def doesIntersect(self, other):
        return self.start < other.end and self.end > other.start

    # determines the length of the intersection between
    # this interval and another
    # returns an integer
    def lenIntersect(self, other):
        if self.doesIntersect(other):
            return min(self.end, other.end) - max(self.start, other.start) 

        return 0

    # determines the intersection between this interval and another
    # returns an interval or None if there is no intersection
    def getIntersect(self, other):
        if self.doesIntersect(other):
            intersect_start = max(self.start, other.start)
            intersect_end = min(self.end, other.end)
            if intersect_start == intersect_end:
                return None
            return IntegerInterval(intersect_start, intersect_end)
        return None

########### Interval class Ends

# do NOT change analyzeIntervals() or main() except for changing debug variable

def analyzeIntervals(line):
    line = line.split(" ")
    interval1 = IntegerInterval(int(line[0]), int(line[1]))
    interval2 = IntegerInterval(int(line[2]), int(line[3]))
    print(f'Interval 1: {interval1}')
    print(f'Interval 2: {interval2}')
    print(f'Interval 1 length: {len(interval1)}')
    print(f'Interval 2 length: {len(interval2)}')
    print(f'Interval 1 equals Interval 2: {interval1 == interval2}')
    print(f'The intervals intersect: {interval1.doesIntersect(interval2)}')
    print(f'Length of intersection: {interval1.lenIntersect(interval2)}')
    print(f'Intersection: {interval1.getIntersect(interval2)}')
    print()

# main() method to read data from the file and analyze each line
def main():

    # open file
    debug = False
    if debug:
        in_data = open('interval.in')
    else:
        in_data = sys.stdin

    # read each line, then analyze
    line = in_data.readline()
    while line != "":
        analyzeIntervals(line)
        line = in_data.readline()

if __name__ == "__main__":
    main()
