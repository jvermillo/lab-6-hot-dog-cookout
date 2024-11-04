# Juniper Vermillo
# CIS 129
# 10/31/2024
# CIS129_JuniperVermillo_Lab6.py
"""Calculate the needed ingredients for a hot dog cookout"""

# For Math Functions
import math

def getTotalHotDogs():
    """Calculate total hot dog amount based on attendance"""
    people = int(input("Enter the number of people attending the cookout: "))
    hotDogs = int(input("Enter the number of hot dogs for each person: "))

    return people * hotDogs # Total hot dog Amount

total = getTotalHotDogs() 

# Package Sizes
DOGS = 10
BUNS = 8

# Calculate Minimum Ingredients Needed
minDogs = math.ceil(total/DOGS)
minBuns = math.ceil(total/BUNS)

# Calculate Amount of Leftover Ingredients
dogsLeft = (DOGS - total % DOGS) % DOGS
bunsLeft = (BUNS - total % BUNS) % BUNS

def showResults():
    """Print minimum ingredients needed and amount of leftover ingredients"""
    print(f"Minimum packages of hot dogs needed: {minDogs}")
    print(f"Minimum packages of hot dog buns needed: {minBuns}")
    print(f"Hot dogs left over: {dogsLeft}")
    print(f"Hot dog buns left over: {bunsLeft}")

def main():
    showResults()

main()