
import random
import time

print("Welcome to the Epic RPG Adventure!")
print("You are a hero on a quest to save the kingdom from darkness.\n")

player_health = 100
inventory = []
gold = 0

def pause():
    time.sleep(1)

def encounter_enemy(enemy, enemy_health, reward_gold):
    global player_health, gold
    print(f"\nA wild {enemy} appears! It has {enemy_health} health.")
    while enemy_health > 0 and player_health > 0:
        action = input("Do you want to (1) attack, (2) defend, or (3) run? ")
        if action == "1":
            damage = random.randint(10, 25)
            print(f"You attack the {enemy} for {damage} damage!")
            enemy_health -= damage
        elif action == "2":
            block = random.randint(5, 15)
            print(f"You defend and block {block} damage next turn.")
        elif action == "3":
            if random.random() < 0.5:
                print(f"You successfully ran away from the {enemy}!")
                return False
            else:
                print(f"You failed to escape!")
        else:
            print("Invalid action! The enemy takes advantage.")

        if enemy_health > 0:
            enemy_attack = random.randint(8, 20)
            print(f"The {enemy} attacks you for {enemy_attack} damage!")
            player_health -= enemy_attack
            print(f"Your health: {player_health}")
        pause()
    if player_health > 0:
        print(f"You defeated the {enemy} and found {reward_gold} gold!")
        gold += reward_gold
        return True
    else:
        print("You have been defeated...")
        return False

def find_treasure():
    global gold, inventory
    treasures = ["Magic Sword", "Healing Potion", "Ancient Shield", "Ring of Speed"]
    found = random.choice(treasures)
    print(f"\nYou found a treasure chest! Inside is a {found}.")
    inventory.append(found)
    gold_found = random.randint(10, 50)
    print(f"You also found {gold_found} gold coins!")
    gold += gold_found

def rest():
    global player_health
    heal = random.randint(15, 30)
    player_health = min(100, player_health + heal)
    print(f"\nYou rest and recover {heal} health. Current health: {player_health}")

# Main game loop
for stage in range(1, 6):
    print(f"\n--- Stage {stage} ---")
    event = random.choice(["enemy", "treasure", "rest"])
    if event == "enemy":
        enemy = random.choice(["Goblin", "Orc", "Troll", "Dark Knight", "Sorcerer"])
        enemy_health = random.randint(30, 60)
        reward_gold = random.randint(20, 60)
        survived = encounter_enemy(enemy, enemy_health, reward_gold)
        if not survived:
            break
    elif event == "treasure":
        find_treasure()
    elif event == "rest":
        rest()
    pause()

if player_health > 0:
    print("\nYou reach the final boss: The Shadow Dragon!")
    survived = encounter_enemy("Shadow Dragon", 120, 200)
    if survived:
        print("\nCongratulations! You have defeated the Shadow Dragon and saved the kingdom!")
        print(f"Final health: {player_health}")
        print(f"Gold collected: {gold}")
        print(f"Inventory: {', '.join(inventory)}")
    else:
        print("\nThe Shadow Dragon was too powerful. The kingdom falls into darkness.")
else:
    print("\nYour journey ends here. Better luck next time, hero!")