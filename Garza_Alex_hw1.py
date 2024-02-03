#Alex Garza Completed 1/17/2023
print(" Soccer History Quiz")
score = 0 
#Question 1
print ("Question #1: What year did the first World Cup happen?", "A) 1926","B) 1936","C) 1930","D) 1920",sep="\n")
wcyear = input()


if(wcyear.lower() == "a"):
    print ("Incorrect")
elif(wcyear.lower() == "b"):
    print("Incorrect")
elif(wcyear.lower() == "c"):
    print("Correct!")
    score += 1
elif(wcyear.lower() == "d"):
    print("Incorrect")
else:
    print("Not an answer choice")

#Question 2
print ("Question #2: Which Club holds the record for most Champions League tittle?","A) Real Madrid","B) AC Millan","C) Ajax","D) Manchester United",sep="\n")
CLtittles = input()

if(CLtittles.lower() == "a"):
    print ("Correct!")
    score += 1
elif(CLtittles.lower() == "b"):
    print("Incorrect")
elif(CLtittles.lower() == "c"):
    print("Incorrect")
elif(CLtittles.lower() == "d"):
    print("Incorrect")
else:
    print("Not an answer choice")

#Question 3
print ("Question #3: Which club did Zlatan Ibrahimović NOT play for?", "A) Paris Saint German", "B) Ajax ","C) Barcelona", "D) Manchester City",sep="\n")
CLUB = input()

if(CLUB.lower() == "a"):
    print ("Incorrect")
elif(CLUB.lower() == "b"):
    print("Incorrect")
elif(CLUB.lower() == "c"):
    print("Incorrect")
elif(CLUB.lower() == "d"):
    print("Correct!")
    score += 1
else:
    print("Not an answer choice")

#Question 4 "and"
print ("Question #4: Which two clubs have Lionel Messi played for in his career? ", "A) Barcelona", "B) LiverPool","C) Paris Saint German", "D) Inter Maimi",sep="\n")
print("Enter one team at a time")
tclub = input()
ttclub = input()

if(tclub.lower() == "a") and (ttclub.lower() == "c"):
    print ("Correct!")
    score += 1
elif(tclub.lower() == "a") and (ttclub.lower() == "b"):
    print("Incorrect")
elif(tclub.lower() == "a") and (ttclub.lower() == "d"):
    print("Incorrect")
elif(tclub.lower() == "b") and (ttclub.lower() == "a"):
    print("Incorrect")
elif(tclub.lower() == "b") and (ttclub.lower() == "c"):
    print("Incorrect")
elif(tclub.lower() == "b") and (ttclub.lower() == "d"):
    print("Incorrect")
elif(tclub.lower() == "c") and (ttclub.lower() == "a"):
    print("Correct!")
    score += 1
elif(tclub.lower() == "c") and (ttclub.lower() == "b"):
    print("Incorrect")
elif(tclub.lower() == "c") and (ttclub.lower() == "d"):
    print("Incorrect")
elif(tclub.lower() == "d") and (ttclub.lower() == "a"):
    print("Incorrect")
elif(tclub.lower() == "d") and (ttclub.lower() == "b"):
    print("Incorrect")
elif(tclub.lower() == "d") and (ttclub.lower() == "c"):
    print("Incorrect")
else:
    print("Not an answer choice")

#Question 5 "or"
print ("Question #5: In this list of Center Backs, pick one of the two who has won the Ballo d'or Award","A) Carles Puyol","B) Franz Beckenbauer","C) Bobby Moore","D) Fabio Cannavaro", "E) Sergio Ramos " ,sep="\n")
centerback = input()

if(centerback.lower() == "b") or (centerback.lower() == "d"):
    print ("Correct!")
    score += 1
elif(CLUB.lower() == "a"):
    print("Incorrect")
elif(CLUB.lower() == "c"):
    print("Incorrect")
elif(CLUB.lower() == "e"):
    print("Incorrect")
else:
    print("Not an answer choice")


#score "3 different out comes"
if(score == 1) or (score == 2) or (score == 0):
    print("You got " +str(score) + "/5 correct," + " You need to watch more soccer")
elif(score == 3) or (score == 4):
    print("You got " +str(score) + "/5 correct," + " You are a causel soccer fan")
elif(score ==5):
    print("You got " +str(score) + "/5 correct," + " You are a Soccer genius")



