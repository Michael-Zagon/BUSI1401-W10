#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This is the earthquake program

eqs = input("Please input the earthquake scale: ")
eqs = float(eqs)

if eqs >= 8.0:
    print("Most Structures Fall")
elif eqs >= 7.0: # it imply 7.0 <= eqs < 8.0
    print("Many Buildings Destoryed")
elif eqs >= 6.0:
    print("Many buidling considerably damaged, some collapse")
elif eqs >= 4.5: 
    print("Damage to poorly constructed buildings")
else:
    print("No destruction of buildings")

