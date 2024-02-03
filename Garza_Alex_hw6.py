def get_average(list_of_num):
  total = 0
  for i in list_of_num:
    total = total + i
  avg = total
  avg = avg/len(list_of_num)
  avg = round(avg)
  return avg
  
def main():
  numbers = ['one','two','three']
  try:
    print(get_average(number)) 
  except NameError as error:
    print("Error message:", error)
  
  greeting = 'Hello World'
  for i in range(len(greeting)+1):
    try:
      print(greeting[i]) 
    except IndexError as error:
      print("Error message:", error)

  numbers = []
  try:
    print(get_average(numbers)) 
  except ZeroDivisionError as error:
    print("Error message:", error)
    
  try:
    print(numbers[10]) 
  except IndexError as error:
    print("Error message:", error)
  
  try:
    color = int(input('Enter your favorite color: ')) 
  except ValueError as error:
    print("Error message:", error)
  
if __name__=="__main__":
  main()
