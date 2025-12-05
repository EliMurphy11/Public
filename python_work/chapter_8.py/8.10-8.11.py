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
    # write a function called send_messages() that prints each text message and moves it to sent_messages
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
# make a list of messages to be sent
messages_to_send = ['Hello, world!', 'Python is fun.', 'I love coding.', 'Have a great day!']
sent_messages = []
# call the function to send messages
send_messages(messages_to_send, sent_messages)
# display all sent messages
print("\nSent messages:")
for sent_message in sent_messages:
    print(sent_message) 