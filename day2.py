# TIP CALCULATOR 

# PRIMITIVE DATA TYPES

# 1. Strings
# 2. Numbers 1_22_300 = 122300
    # -integers
    # - floats
# 3. Boolean


# length = len(input("What's your name bubba?\n"))
# print("The dude's name has " +  length + " alphabets!")

# Above code doesn't work because length is an integer and we are trying to concatenate it with strings.

# We check the type of a variable with the type() method.
# We convert the value of a variable from integer to string with the str(variable name) function, from integer to float with the float() function, from string to int with the int() function.

# Splitting a string containing a 2 digit number and displaying its sum.

# numStr = input("Enter a two digit number.\n")
# numSum=0
# for num in numStr:
#     numSum = int(num) + numSum
# print(numSum)

# MATHEMATICAL OPERATORS
# PEMDAS
# - Parenthesis ()
# - Exponents **
# - Multiplication *
# - Division /
# - Addition +
# - Subtraction - 

# BMI CALCULATOR
# BMI = Weight(kgs)/Height**2(meters) 

# weight = float(input("what is your weight in kgs? \n"))
# height = float(input("what is your height in meters?\n"))

# bmi = weight/height**2
# # finalBMI = "{:.2f}".format(bmi)
# finalBMI = round(bmi, 2)
# print(finalBMI)

# Number manipulation
# Floor Division - Rounds of the number to the lower digit and returns an int.
# - print((5//3))
# F strings are like template literals in JavaScript

score = 0
height= 1.8
isWinning = True

print(f"your score is {score} and your height is {height} and your winning state is {isWinning}" )

