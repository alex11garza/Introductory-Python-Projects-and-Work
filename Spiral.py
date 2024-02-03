#  File: Spiral.py
#  Student Name: Alex Garza
#  Student UT EID: ang3489
import sys


# Input: n
# Output:
def get_dimension(in_data):
    pass
    '''##### ADD CODE HERE #####'''
    return int(in_data.readline())

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    pass
    '''##### ADD CODE HERE #####'''
    if n %2 == 0:
        n += 1
    spiral = [[0] *n for _ in range(n)]
    movements = [(0, 1), 
                (1, 0), 
                (0, -1), 
                (-1, 0)]
    movement_start:int =0; row:int = n //2; colum:int = n //2; start:int = 1
    spiral[row][colum] = start
    for a in range(1,n,2):
        for _ in range(4):
            movement = movements[movement_start]; movement_start = ((movement_start +1) %4)
        for _ in range(a):
            row = movement[0]; colum = movement[1]
            start +=1; spiral[row][colum] = start
    return spiral


# Input: handle to input file
#        the number spiral
# Output: printed adjacent sums
def print_adjacent_sums(in_data, spiral):
    pass
    '''##### ADD CODE HERE #####'''
    for a in in_data:
        start:int = int(a)
        adjacent_sum = sum_adjacent_numbers(spiral, start); print(adjacent_sum)


# Input: the number spiral
#        the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    pass
    '''##### ADD CODE HERE #####'''
    len_spiral = len(spiral)
    for row in range(len_spiral):
        for colum in range(len_spiral):
            if spiral[row][colum] == n:
                adjacent_sum:int =0
                for b in range(-1,2):
                    for c in range(-1,2):
                        next_row = row +1; new_colum = colum +1
                        if 0 <= next_row < len_spiral and 0 <= new_colum < len_spiral:
                            adjacent_sum +=spiral[next_row][new_colum]
                return adjacent_sum
    return 0 



# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # set the input source - change to False before submitting
    debug = False
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin

    # process the lines of input
    size = get_dimension(in_data)

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)
    # use following line for debugging only
    # print_spiral(spiral)

    # process adjacent sums
    print_adjacent_sums(in_data, spiral)


if __name__ == "__main__":
    main()
