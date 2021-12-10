import random
# number = int(input("Give me a number "))
# if number % 2 == 1:
#   print(f"{number} is odd")
# else:
#   print(f"{number} is even")


# print("Let's calculate your BMI")
# kgWeight = float(input("How much do you weigh (in pounds)? ")) * 0.45359237
# mHeight = float(input("How tall are you in inches? ")) * 2.54 / 100
# bmi = round(kgWeight / (mHeight * mHeight), 1)
# print("Your BMI is " + str(bmi) + ".")
# if bmi > 30:
#   print("You are obese")
# elif bmi > 24.9:
#   print("You are at overweight")
# elif bmi > 18.4:
#   print("You are at a healty weight")
# else:
#   print("You are underweight.")


# year = int(input("What year do you want to check? "))
# if year % 4 != 0:
#   print(f"{year} is not a leap year")
# elif (year % 100 == 0) and (year % 400 != 0):
#   print(f"{year} is not a leap year")
# else:
#   print(f"{year} is a leap year")


# print("Welcome to the bamboo garden!")
# lucky = input("Are you here to purchase lucky bamboo? Y or N ")
# if lucky != "N":
#   print("Get out of my nursery!")
# else:
#   size = int(input("That's good. Any serious collector knows lucky bamboo is not a true bamboo. What size bamboo do you want in gallons? 3, 7, or 15? "))
#   field_dug = input("Do you want field dug? It will grow faster than potted. Y or N ")
#   install = input("Do you want us to install it? Y or N ")
#   price = 0
#   if size == 3:
#     price = 35
#   elif size == 7:
#     price = 90
#   else:
#     price == 150
#   if field_dug == "Y":
#     if size == 3:
#       price = price + 15
#     elif size == 7:
#       price = price + 30
#     else:
#       price = price + 60
#   if install == "Y":
#     if size == 3:
#       price = price + 20
#     elif size == 7:
#       price = price + 30
#     else:
#       price = price + 60
#   print(f"That will be {price}. Yes, I know that's rather expensive, but think of it more like a tree.")


# print("Welcome to the Love Calculator!")
# hisName = input("What is his name? ").lower()
# herName = input("What is her name? ").lower()
# allT = hisName.count("t") + herName.count("t")
# allR = hisName.count("r") + herName.count("r")
# allU = hisName.count("u") + herName.count("u")
# allE = hisName.count("e") + herName.count("e")
# allL = hisName.count("l") + herName.count("l")
# allO = hisName.count("o") + herName.count("o")
# allV = hisName.count("v") + herName.count("v")
# total = allT + allR + allU + allE + allL + allO + allV + allE
# print(f"Your score is {total}.")
# if (total > 90) or (total < 10):
#   print("You go together like coke and mentos! \n That doesn't sound like a good thing.")
# elif (total > 40) and (total < 60):
#   print("You are alright together.")
# else:
#   print("Keep looking.")