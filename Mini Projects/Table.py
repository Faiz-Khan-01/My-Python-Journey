# This program takes input and make a multiplicative table of it.abs

number = int(input("Enter your number \n\n"))
print()

for i in range (1, 11) :
    print(f"{number} x {i} = {number * i}")