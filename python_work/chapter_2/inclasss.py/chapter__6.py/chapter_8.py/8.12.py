# write a function that accepts a list of items a person wants on a sandwich
def make_sandwich(*toppings):
    print("Making a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
# call the function three times with different toppings
make_sandwich('lettuce', 'tomato', 'cheese')
make_sandwich('turkey', 'bacon', 'avocado', 'mayonnaise')
make_sandwich('peanut butter', 'jelly')
