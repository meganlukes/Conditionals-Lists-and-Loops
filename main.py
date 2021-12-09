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
year = int(input("What year do you want to check? "))
if year % 4 != 0:
  print(f"{year} is not a leap year")
elif (year % 100 == 0) and (year % 400 != 0):
  print(f"{year} is not a leap year")
else:
  print(f"{year} is a leap year")