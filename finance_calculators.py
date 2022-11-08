#program that acts as two different finance calculators
import math
amount = 0
print("""

Welcome to Harry's investment and bond calculator!
_______________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|


""")
#display option to user and ask for input
print("""
Choose either 'investment' or 'bond' from the menu below to proceed:

investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan

""")
caculator_type = input("Enter you choice here: ")
user_choice = caculator_type.lower().strip() # input sanitised using lower and strip method

#loop to catch miss entry of choice but keep program running for user
counter = 0
while counter < 1:
    if (user_choice == "investment") or (user_choice == "bond"):
      counter += 1
    else:
      caculator_type = input("Please enter either 'investment or 'bond' : ")
      user_choice = caculator_type.lower().strip()

#code to determine which calculation to offer with a nested if calculation within investment due to compound or simple interest type
if user_choice == "investment":
    deposit, interest_rate,  = float(input("How much money do you wish to deposit? ")), float(input("What is the interest rate? Please enter a number only: "))/100
    number_of_years = float(input("How many years do you plan on investing? "))
    interest = input("Do you want simple or compound interest on your investment? ")

    #code to calculate either simple or compound interest on investment
    if interest.lower().strip() =="simple":
      amount = deposit*(1 + interest_rate*number_of_years)
    elif interest.lower().strip() == "compound":
      amount = deposit* math.pow((1 + interest_rate),number_of_years)
    else:
      print("Please type either 'simple' or 'compound' next time - Please run the program again.")
    print(f"You would recieve R{round(amount,2)}, from a deposit of R{deposit}, with an interest rate of {math.ceil(interest_rate*100)}% over {number_of_years}, if the interest type was {interest}.")

#code to calculate bond replayment on house over X months
elif user_choice.lower().strip() == "bond":
    house_value, interest_rate = float(input("What is the present value of the house? ")), float(input("What is the interest rate? (e.g. 7%): "))/100, 
    months_to_repay =float(input("What is the number of months you plan on taking to repay the amount?: "))
    monthly_payment = (interest_rate/12) * (1/(1-(1+interest_rate/12)** (-months_to_repay)))*house_value
    print(f"Your monthly payments will be R{round(monthly_payment,2)} over the next {months_to_repay} months, on a bond of R{house_value} with an interest rate of {math.ceil(interest_rate*100)}%.")
else:
    None


