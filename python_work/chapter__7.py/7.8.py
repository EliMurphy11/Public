# make a list called sandwich_orders
sandwich_orders = ['turkey', 'pastrami', 'veggie', 'pastrami', 'ham',]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
