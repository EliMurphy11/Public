
import random

print("Welcome to the Mythical Quest!")
print("You are a brave adventurer on a journey through a land of mythical creatures.")

health = 100
creatures = ["Dragon", "Griffin", "Hydra", "Minotaur", "Phoenix"]
actions = ["fight", "run", "befriend"]

for stage in range(3):
    creature = random.choice(creatures)
    print(f"\nStage {stage + 1}: You encounter a {creature}!")
    print("What will you do?")
    print("1. Fight")
    print("2. Run")
    print("3. Befriend")
    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            print(f"You bravely fight the {creature} and win!")
        else:
            print(f"The {creature} wounds you in battle.")
            health -= random.randint(20, 40)
    elif choice == "2":
        escape = random.choice([True, False])
        if escape:
            print(f"You successfully run away from the {creature}.")
        else:
            print(f"You fail to escape and the {creature} attacks you!")
            health -= random.randint(10, 30)
    elif choice == "3":
        friend = random.choice([True, False])
        if friend:
            print(f"You befriend the {creature}! It helps you on your journey.")
            health += random.randint(5, 20)
        else:
            print(f"The {creature} rejects your friendship and attacks!")
            health -= random.randint(10, 25)
    else:
        print("Invalid choice! The creature takes advantage and attacks you.")
        health -= 15

    print(f"Your health is now {health}.")

    if health <= 0:
        print("You have been defeated on your quest. Game over!")
        break

if health > 0:
    print("\nCongratulations! You survived your mythical quest!")
else:
    print("\nBetter luck next time, adventurer!")