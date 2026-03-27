# Takes the user input 
Length = input("Enter length of Rectangle\n") 
Breadth = input("Enter breadth of Rectangle\n")

# Converts the inputs to float and calculates
Perimeter = 2*(float(Length)+float(Breadth))
Area = float(Length)*float(Breadth)

# Prints the output
print("The Perimeter of Rectangle is :", Perimeter)
print("The Area of Rectangle :", Area)
