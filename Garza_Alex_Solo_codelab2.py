#Alex Garza Codelab2 Group-Solo 2/10/2023
import random
secret_number = random.randint(0, 100)
guess = int(input("Guess a secret number between 0 and 100: "))
count = 0
while guess != secret_number:
    if guess > 100:
        print("Rememebr to guess a number between 0 and 100")
    #Bonus Point odds and even 
    if guess%2==0 and secret_number%2==0:
        print("You are right to guess even, but " , end="")
    elif guess%2!=0 and secret_number%2!=0:
        print("You are right to guess odd, but " , end="")
    elif guess%2==0 and secret_number%2!=0:
        print("Try guessing an odd number. Also " , end="")
    elif guess%2!=0 and secret_number%2==0:
        print("Try guessing an even number. Also ", end="")
    #This part inbetween the green is the bonus point
    if guess > secret_number:
        print(int(guess), "is to high" )
    else:
        print(int(guess), "is to low")
    guess = int(input("Guess the secret number again: "))
    count += 1 
print(f" Correct! The number was", secret_number,"\n","It took you",count,"tries!")