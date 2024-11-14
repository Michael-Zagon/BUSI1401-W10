#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This program calculates income tax

def main():

    # Input
    user_mstatus = input("Please indicate your relationship status (Single or Married): ")
    user_income = float(input("Please input your income: "))

    # Process
    if user_mstatus == "Single":
        if user_income <= 32000:
            tax = user_income * 0.9
        else:
            tax = 3200 + (user_income - 32000)*0.75
    elif user_mstatus == "Married":
        if user_income <= 64000:
            tax = user_income * 0.9
        else:
            tax = 6400 + (user_income - 64000)*0.75

    # Output
    print("Your tax to pay: ", tax)
        
if __name__ == "__main__":
    main()

print("\nDone")