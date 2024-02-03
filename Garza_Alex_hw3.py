animal = str(input("What is your favorite animal? "))
for letter in animal:
    print(letter)

num = int(input("Pick a number: "))
for i in range(num + 1):
    print(i, end = " ",)

food = str.lower(input("\n" "Pick an option of Soup, Salad, or Sandwich: "))
while food != str.lower("soup") and food != str.lower("salad") and food != str.lower("sandwhich"):
    print("Sorry that's not an option!")
    food = str(input("Pick an option of soup, salad, or sandwich: "))
print("Okay, you picked", str.capitalize(food))


#Bonus point
import turtle   
t = turtle.Turtle()
shape = str.lower(input("Pick an option of Triangle, Square, or Circle: "))
while shape != str.lower("square") and shape != str.lower ("triangle") and shape != str.lower("circle"):
    print("Sorry that's not an option!")
    shape = str.lower(input("Pick an option of Triangle, Square, or Circle: "))
shape == shape 
amount_of_shape = int(input("How many times would you like to draw your shape: "))
x = 0
if shape == str.lower("square"):
    while (x < amount_of_shape):
        for s in range(4):
            t.forward(50)
            t.right(90)
        t.penup()
        t.forward(100)
        t.pendown()
        x += 1
elif shape == str.lower("triangle"):
    while (x < amount_of_shape):
        for s in range(3):
            t.forward(50)
            t.left(120)
        t.penup()
        t.forward(100)
        t.pendown()
        x += 1
elif shape == str.lower("circle"):
    while (x < amount_of_shape):
        t.circle(50)
        t.penup()
        t.forward(100)
        t.pendown()
        x += 1

else:
    exit(function)