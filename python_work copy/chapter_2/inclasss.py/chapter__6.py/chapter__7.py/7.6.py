# movie theater charge based on age
age = int(input("Enter your age: "))
if age < 3:
    print("Your ticket is free.")
elif 3 <= age <= 12:
    print("Your ticket is $10.")
else:
    print("Your ticket is $15.")
# use a conditional test to stop the loop
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. " 
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
# using break to exit a loop
while True:
    city = input("\nEnter the name of a city you have visited (or 'quit' to end): ")
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
# use an active variable to control a loop
active = True
while active:
    message = input("\nEnter a city you have visited (or 'quit' to end): ")
    if message == 'quit':
        active = False
    else:
        print(f"I'd love to go to {message.title()}!")