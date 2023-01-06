# Tip calculator (DAY 2_MAIN PROJECT)
print("Welcome to the tip calculator: ")
totalBill = float(input("What was the total bill? $ "))
splitBill = int(input("How many people split the bill? "))
percentTip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
grossBill = totalBill/splitBill
tip = (percentTip/100*totalBill)
individualTip = (tip/splitBill)
netBill = str(individualTip+grossBill)
print("Each person should pay " + netBill)

# Name Character Application
userName = input("What is your name?\n")
numChar = str(len(userName))  # Typecasting or type conversion - changing userName variable from int 2 str
print("Gdday, " + userName + ". Your name has " + numChar + " characters.")
# Type check functions enables devs to check datatype of variables print(type(numChar))

# Day 2.1 Coding challenge
userNumber = input("Type a two digit number: ")
digOne = int(userNumber[0])
digTwo = int(userNumber[1])
add = digOne + digTwo
print(add)

# BMI Calculator
weight = int(input("Your weight in kgs: "))
height = float(input("Your height in m: "))
bmi = str(weight/height**2)
print("Your BMI is " + bmi)


