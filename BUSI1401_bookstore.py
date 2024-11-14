#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This program chooses discounts for books at the University bookstore

def main():

    # Input
    user_price = float(input("How expenisve is your order: "))

    # Process
    if user_price < 128:
        discount = 0.8
        discounted_price = user_price * 0.92
    else:
        discount = 0.16
        discounted_price = user_price * 0.84

    # Output

    print("----------------------------------------")
    print("\tUniversity Bookstore Reciept\t")
    print("----------------------------------------")
    print("Price is: \t|\t", user_price,"$")
    print("----------------------------------------")
    print("Discount: \t|\t", discount,"%")
    print("----------------------------------------")
    print("Sub Total \t|\t", discounted_price,"$")
    print("----------------------------------------")


if __name__ == "__main__":
    main()

print("\nDone")