"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 35.00
# Number of characters.
numChars = 8
# Color of characters.
color = "gold"
# Type of wood.
woodType = "oak"
# Write assignment and if statements here as appropriate.
numChars1 = int(input("Number of Characters: "))
woodType1 = input("Wood Type: ")
color1 = input("Color: ")

if numChars1 > 5:
    charge += (numChars1 - 5) * 4.00
    
if color1 == color:
    charge += 15.00

if color1 == "black":
    charge

if color1 == "white":
    charge
    
if woodType1 == woodType:
    charge += 20.00

if woodType == "pine":
    charge
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
