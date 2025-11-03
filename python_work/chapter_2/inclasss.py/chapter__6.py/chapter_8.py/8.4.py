# modify the make_shirt() so that shirts are large by default with a message that reads I love Python
def make_shirt(size='L', message='I love Python'):
    print(f"The shirt size is {size} and it has the message: '{message}' printed on it.")
# call the function without arguments to use default values
make_shirt()
# call the function with custom size and message
make_shirt('M', 'Code is fun!')
# call the function with custom message but default size
make_shirt(message='Stay curious!')