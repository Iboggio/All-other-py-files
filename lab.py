print("Quiz Time")
print("answer either 1,2,or3") 
print("Who is the bald white guy in Fast and Furious?")
print("1.)Vin Diesel")
print("2.)Max Cheng")
print("3.)Nick Boogio")
correct_answers = 0
answer = input("enter your answer:")
if answer == "1":
    print("you are correct")
    correct_answers += 1
elif answer== "2":
    print("incorrect")
else:
    print("incorrect")
print("Will Donald Trump make America great again?")
print("1.)yes")
print("2.)maybe")
print("3.)NO WAY")
answer = input("enter your answer:")
if answer == "3":
    print("correct")
    correct_answers += 1
elif answer== "2":
    print("incorrect")
else :
    print("incorrect")
print("What year is it this year?")
print("1.)2015")
print("2.)2016")
print("3.)2017")
answer = input("enter your asnwer:")
if answer == "2":
    print("correct")
    correct_answers += 1
else:
    print("incorrect")
print("Who is the Prime Minister of Canada?")
print("1.)Justin Trudeau")
print("2.)Justin Bieber")
print("3.)Justin Timberlake")
answer = input("enter your answer")
if answer == "1":
    print("correct")
    correct_answers += 1
else:
    print("incorrect")
print("Whhat country does Max Cheng come from?")
print("1.)Peru")
print("2.)Taiwan")
print("3.)Neverland")
answer = input("enter your answer")
if answer == "2":
    print ("correct")
    correct_answers += 1
else:
    print ("incorrect")

print("You got", correct_answers, "right out of 5")
print("That is ",(correct_answers / 5 * 100),"%",sep='')