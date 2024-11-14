#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This program stimulates an elevator panel that skips the 13 floor

def main():

    #Input
    user_floor=int(
        input("Which floor would you like to go to? ")
    )

    # Process
    
    if user_floor >= 13:
        real_floor = user_floor -1
    elif user_floor < 13:
        real_floor = user_floor
    else:
        print("Invalid Input")
    
        
    # Output
    print("The elevator will travel to the actual floor of", real_floor)


if __name__ == "__main__":
    main()

print("\nDone")


