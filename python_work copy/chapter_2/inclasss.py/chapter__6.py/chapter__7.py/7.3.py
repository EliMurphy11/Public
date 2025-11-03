# asking for a numbner and telling if its a multiple of 10
number = int(input("Enter a number, and I'll tell you if it's a multiple of 10: "))
if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")  
    