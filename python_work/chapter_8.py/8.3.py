# write a function called make_shirt() that accepts a size and the text of a message
def make_shirt(size, message):
    print(f"The shirt size is {size} and it has the message: '{message}' printed on it.")
# call the function with different sizes and messages
make_shirt('M', 'Hello World!')
make_shirt('L', 'Python is awesome!')
make_shirt('S', 'Keep calm and code on.')
# call the function using positional arguments
make_shirt('XL', 'Custom message here.')
# call the function using keyword arguments
make_shirt(message='Stay positive!', size='M')

