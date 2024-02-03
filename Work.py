
#  File: Work.py
#  Student Name: Alex Garza
#  Student UT EID: ang3489

import sys
import time


# Purpose: Determines how many lines of code will be written
#          before the coder crashes to sleep
# Input: lines_before_coffee - how many lines of code to write before coffee
#        prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written
#         before the coder falls asleep
def sum_series(lines_before_coffee, prod_loss) -> int:
    pass
    '''##### ADD CODE HERE #####'''
    lines_written = 0
    while lines_before_coffee > 0:
        lines_written += lines_before_coffee
        lines_before_coffee //= prod_loss
    return int(lines_written)

# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def linear_search(total_lines, prod_loss) -> int:
    pass
    '''##### ADD CODE HERE #####'''
    lines_before_coffee = 1
    while sum_series(lines_before_coffee, prod_loss) < total_lines:
        lines_before_coffee += 1
    return int(lines_before_coffee)

# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def binary_search(total_lines, prod_loss) -> int:
    pass
    '''##### ADD CODE HERE #####'''
    low:int = 0; high:int = total_lines
    while low < high:
        mid = (low + high) // 2
        lines = sum_series(mid, prod_loss)
        if lines < total_lines:
            low = mid + 1
        else:
            high = mid

    return int(low)


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Open input source
    # Change debug to false before submitting
    debug = True
    if debug:
        print("\t", "\t", "Terminal Test", "\n")
        in_data = open("/Users/alexgarza/Desktop/School/UT Summer 2023/CS N313E/Homework.py/work.in")
    else:
        in_data = sys.stdin

    # read number of cases
    line = in_data.readline().strip()
    num_cases = int(line)

    for i in range(num_cases):

        # read one line for one case
        line = in_data.readline().strip()
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        count = sum_series(lines, prod_loss)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(binary_time),
              "seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        count = sum_series(lines, prod_loss)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(linear_time),
              "seconds")
        print()

        # Comparison
        print("Binary Search was",
              "{0:.1f}".format(linear_time / binary_time),
              "times faster.")
        print()
        print()


if __name__ == "__main__":
    main()
