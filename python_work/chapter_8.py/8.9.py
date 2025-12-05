# make a list containing a series of short text messages
messages = ['Hello, world!', 'Python is fun.', 'I love coding.', 'Have a great day!']
# print each message
for message in messages:
    print(message)
# move each message to a new list called sent_messages after printing
sent_messages = []
while messages: 
    current_message = messages.pop(0)
    print(f"Sending message: {current_message}")
    sent_messages.append(current_message)
# display all sent messages
print("\nSent messages:")
for sent_message in sent_messages:
    print(sent_message)