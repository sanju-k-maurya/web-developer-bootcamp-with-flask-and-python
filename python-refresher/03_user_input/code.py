# -- Taking user input --

name = input("Enter your name: ")
print(name)

# -- Doing maths on input --

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8

print(f"{square_feet} square_feet is {square_meters: .2f} square meters.")