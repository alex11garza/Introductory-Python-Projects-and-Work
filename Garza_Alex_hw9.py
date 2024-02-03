#Alex Garza
# This function checks if a given number is prime or not
def is_prime(num):
    if num < 2:  # If the number is less than 2, it is not a prime number
        return False
    counter = num-1  # Start counter at num-1
    while(counter > 1):  # Loop through all numbers from num-1 to 2
        if num % counter == 0:  # If num is divisible by counter, it is not a prime number
            return False
        counter -= 1  # Decrement counter by 1
    return True  # If the loop completes, num is a prime number

# This function counts the number of prime numbers in a given list
def count_primes(list_with_primes):
    primes = 0
    for x in list_with_primes:
        if(is_prime(x)):  # Call is_prime function to check if x is prime
            primes += 1
    return primes

# This function sorts a given list using the bubble sort algorithm
def bubble_sort(sorting_list):
    n = len(sorting_list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if sorting_list[j] > sorting_list[j + 1] :  # Swap elements if they are in the wrong order
                sorting_list[j], sorting_list[j + 1] = sorting_list[j + 1], sorting_list[j]

# This function calculates the average value of a given list
def get_average(list_to_average):
    total = 0
    for i in list_to_average:
        total = total + i  # Add each element to the total
    return round(total/len(list_to_average))  # Divide the total by the length of the list and round to nearest integer

# This is the main function
def main():
    user_list = []
    user_num = input('Enter a number (type "Done" when finished): ')
    while(user_num.lower() != 'done'):  # Loop until the user enters 'Done'
        try:
            user_num = int(user_num)  # Convert user input to integer
            user_list.append(user_num)  # Add the number to the list
        except ValueError as err:
            print(err,'That was not a number!')  # Handle non-numeric input
        user_num = input('Enter another number (type "Done" when finished): ')
    print('Your list:',user_list)  # Print the user's list
    print('Your list has',count_primes(user_list),'primes')  # Call count_primes function and print result
    print('Average:',get_average(user_list))  # Call get_average function and print result
    bubble_sort(user_list)  # Call bubble_sort function to sort the list
    print('Your list sorted:',user_list)  # Print the sorted list

# Check if this is the main module
if __name__=="__main__":
    main()  # Call the main function (which should always run first)
