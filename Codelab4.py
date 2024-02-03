#Created by Alex Garza, Meecah Glas, Lorena Chiles, Anh-Thu Bui 
#March 23rd 2023
#CS 303E 51865


def max_word_length(words_list):
  #TODO: use a loop to go through all of the words in words_list and determine the longest word length
  #TODO: return the length of the longest word
   #TODO: replace this return line with the correct return value
  longest_word_length = 0 
  for word in words_list:
    if len(word) >longest_word_length:
      longest_word_length = len(word)
  return longest_word_length

def frame_this(list_of_words):
  #TODO: call max_word_lenth to determine the longest word in list_of_words
  #TODO: print the words, each centered on its own line, surrounded by a frame of asterisks (*)
  #TODO: make sure the frame edges are straight, and that there is at least one space between the word and the frame edge
  #TODO: you must handle any length of word, and any number of words in the list
  #TODO: important: do NOT use .center to center the text, use a loop or concatenate
  #TODO: hint: this function DOES NOT return anything
  #TODO: replace this print statement the desired print behavior
  longest_word_length = max_word_length(list_of_words)
  frame_width = longest_word_length + 4
  print("*" * frame_width) #Top of the frame
  for word in list_of_words:
    spaces = longest_word_length +2 - len(word)
    #check this number nvm
    left_space= spaces//2
    right_space= spaces-left_space
    print("*" + " " * left_space + word + " " *right_space + "*" )
  print("*" * frame_width)#Bottom of the frame

def is_prime(num):
  #TODO: 0 and 1 are not prime
  #TODO: all other positive numbers are prime if and only if they are not a multiple of any smaller number (besides 1)
  #TODO: determine if num is prime
  #TODO: return True if it is prime, False if it is not prime
  #TODO: replace this return line with the correct return value3
  if num < 2:
    return False 
  for y in range(2, int(num ** 0.5) + 1):
    if num % y == 0:
      return False 
  return True

def count_primes(list_of_numbers):
  #TODO: loop through each number in list_of_numbers
  #TODO: for each of those numbers, determine if it is prime by calling is_prime
  #TODO: count the total number of primes in the list
  #TODO: return the total count
  #TODO: replace this return line with the correct return value
  count = 0 
  for num in list_of_numbers:
    if is_prime(num):
      count += 1
  return count

def make_list(string_of_text):
  #TODO: string_of_text will be a single string with a series of words separated by a comma
  #TODO: convert string_of_text into a list of strings (hint: use .split to separate by comma)
  #TODO: return the list of strings
  #TODO: replace this return line with the correct return value
  i = string_of_text.split(" , ")
  return i

def main():
  #TODO: create a list of strings that contains all first names of your team members (list_of_names)
  #TODO: call the frame_this function and pass your list of names
  list_of_names = ['Meecah', 'Alex', 'Lorena', 'Anh-Thu']
  frame_this(list_of_names)

  # -------------do not change anything below this line----------#
  words_to_split = 'one, two, three, four hundred'
  words_list = make_list(words_to_split) # should result in the list ['one','two','three','four hundred']
  frame_this(words_list)
  numbers = [1,9,0,2,3,17,6,25,4,5,11,14]
  print('The list of numbers',numbers,'has',count_primes(numbers),'primes.')
  
if __name__=="__main__":
  main()

