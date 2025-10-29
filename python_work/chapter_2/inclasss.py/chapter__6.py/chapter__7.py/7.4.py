# writing a loop that prompts for pizza toppings
requested_toppings = ""
while requested_toppings != 'quit':
    requested_toppings = input("Enter a pizza topping you would like (or 'quit' to finish): ")
    if requested_toppings != 'quit':
        print(f"Adding {requested_toppings} to your pizza.")
print("Your pizza is ready!")
   