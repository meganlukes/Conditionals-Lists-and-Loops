import random

# Conditionals
# number = int(input("Give me a number "))
# if number % 2 == 1:
#   print(f"{number} is odd")
# else:
#   print(f"{number} is even")


# BMI Calculator
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


# Check if a year is a leap year
# year = int(input("What year do you want to check? "))
# if year % 4 != 0:
#   print(f"{year} is not a leap year")
# elif (year % 100 == 0) and (year % 400 != 0):
#   print(f"{year} is not a leap year")
# else:
#   print(f"{year} is a leap year")


#Conditional price calculator
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


#Count the number of times certain letters appear in a phrase
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


# Coin flip
# coin = random.random()
# if coin > 0.5:
#   print("heads")
# else:
#   print("tails")


#Lists
# bamboo_species = ["Bambusa chungii Blue Chungii", "Bambusa multiplex Alphonse Karr", "Bambusa multiplex Fernleaf", "Bambusa vulgaris wamin Dwarf Buddha Belly", "Bambusa textilis mutabilis Emerald Bamboo", "Bambusa emeiensis flavidovirens Yin Yang Yellowstripe"]
# print(f"The species currently in our database are {bamboo_species}")
# print("I'll give you a random bamboo species")
# print(f"{bamboo_species[random.randint(0, len(bamboo_species) - 1)]}")
# new_species = input("Give me a list of the new bamboo species, seperated by a comma. ")
# new_species_list = new_species.split(", ")
# bamboo_species = bamboo_species + new_species_list
# print(f"The species currently in our database are now {bamboo_species}")


# Treasure map
# row1 = ["o", "o", "o"]
# row2 = ["o", "o", "o"]
# row3 = ["o", "o", "o"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# spot = input("Where do you want to place the x? ")
# row = int(spot[2]) - 1
# col = int(spot[0]) - 1
# sel_row = map[row]
# sel_row[col] = "x"
# print(f"{row1}\n{row2}\n{row3}")


# Rock paper scissors game
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# player = int(input("Type 1 for rock, 2 for paper, 3 for scissors "))
# computer = random.randint(1, 3)
# print(f"{player} {computer}")
# if player == 1:
#   print(f"{rock}")
# elif player == 2:
#   print(f"{paper}")
# else:
#   print(f"{scissors}")
# if computer == 1:
#   print(f"{rock}")
# elif computer == 2:
#   print(f"{paper}")
# else:
#   print(f"{scissors}")
# if player == computer:
#   print("Tie!")
# else:
#   if player == 1 and computer == 3:
#     print("You win!")
#   elif player == 2 and computer == 1:
#     print("You win!")
#   elif player == 3 and computer == 2:
#     print("You win!")
#   else:
#     print("You lost")

# Average heights for loop
# heights = [180, 124, 16, 173, 189, 169, 146]
# comb_height = 0
# for height in heights:
#   comb_height = comb_height + height
# avg_height = int(comb_height / len(heights))
# print(avg_height)