# make a list called sandwich_orders and make sure 'pastrami' appears thrice
sandwich_orders = ['turkey', 'pastrami', 'veggie', 'pastrami', 'ham', 'pastrami',]
finished_sandwiches = []
# notify that pastrami is out of stock and remove all occurrences
print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
# make the sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
# display finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
    