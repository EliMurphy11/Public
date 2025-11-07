
import random

print("Welcome to FUTURE ZOMBIE SURVIVAL!")
print("The year is 2125. Zombies roam the earth. You must survive 100 choices.")
health = 100

choices = [  
    ("You see a group of zombies ahead. Do you (a) hide or (b) run?", "a"),
    ("You find a locked door. Do you (a) pick the lock or (b) break it down?", "a"),
    ("A stranger offers you food. Do you (a) accept or (b) refuse?", "b"),
    ("You hear noises in the dark. Do you (a) investigate or (b) stay put?", "b"),
    ("You find a car with keys inside. Do you (a) drive or (b) walk?", "a"),
    ("Your car runs out of gas. Do you (a) search for gas or (b) abandon the car?", "a"),
    ("You encounter a zombie horde. Do you (a) fight or (b) sneak around?", "b"),
    ("You find a safe house. Do you (a) enter or (b) keep moving?", "a"),
    ("You meet another survivor. Do you (a) trust them or (b) stay cautious?", "b"),
    ("You find a weapon. Do you (a) take it or (b) leave it?", "a"),
    ("You come across a river. Do you (a) swim across or (b) build a raft?", "b"),
    ("You hear a distress signal. Do you (a) respond or (b) ignore it?", "b"),
    ("You find a map. Do you (a) follow it or (b) make your own path?", "a"),
    ("You encounter a wild animal. Do you (a) tame it or (b) avoid it?", "b"),
    ("You find a stash of supplies. Do you (a) take everything or (b) only what you need?", "b"),
    ("You see smoke in the distance. Do you (a) investigate or (b) steer clear?", "b"),
    ("You find an abandoned building. Do you (a) search it or (b) move on?", "a"),
    ("You come across a bridge. Do you (a) cross it or (b) find another way?", "a"),
    ("You hear footsteps behind you. Do you (a) confront them or (b) hide?", "b"),
    ("You find a group of survivors. Do you (a) join them or (b) stay alone?", "b"),
    ("You see food in a store window. Do you (a) break in or (b) look for other sources?", "b"),
    ("You encounter a zombie blocking your path. Do you (a) fight it or (b) find another route?", "b"),
    ("You find a radio. Do you (a) try to contact others or (b) ignore it?", "a"),
    ("You come across a farm. Do you (a) scavenge for food or (b) keep moving?", "a"),
    ("You see a helicopter in the sky. Do you (a) signal it or (b) stay hidden?", "b"),
    ("You find a medical kit. Do you (a) use it now or (b) save it for later?", "a"),
    ("You encounter a locked gate. Do you (a) climb over it or (b) look for another entrance?", "a"),
    ("You hear children crying. Do you (a) help them or (b) avoid the noise?", "a"),
    ("You find a motorcycle. Do you (a) ride it or (b) leave it?", "a"),
    ("You come across a zombie nest. Do you (a) destroy it or (b) avoid it?",
        "b"),
    ("You find a cave. Do you (a) explore it or (b) stay outside?", "b"),
    ("You see a flare in the distance. Do you (a) investigate or (b) ignore it?", "b"),
    ("You find a boat. Do you (a) sail it or (b) stay on land?", "b"),
    ("You encounter a zombie dog. Do you (a) fight it or (b) avoid it?", "b"),
    ("You find a stash of weapons. Do you (a) take them or (b) leave them?","a"),
    ("You see a group of zombies fighting each other. Do you (a) sneak past or (b) attack while they're distracted?", "a"),
    ("You find a bunker. Do you (a) enter or (b) keep moving?", "a"),
    ("You hear a scream. Do you (a) investigate or (b) stay away?", "b"),
    ("You find a garden. Do you (a) gather food or (b) keep moving?", "a"),
    ("You see a zombie climbing a fence. Do you (a) wait for it to come down or (b) climb over while it's distracted?", "b"),
    ("You find a group of friendly survivors. Do you (a) join them or (b) stay alone?", "b"),
    ("You come across a river with a broken bridge. Do you (a) try to repair it or (b) find another way across?", "b"),
    ("You find a stash of clean water. Do you (a) take it or (b) leave it?", "a"),
    ("You see a zombie horde approaching. Do you (a) hide or (b) prepare to fight?", "a"),
    ("You find an old library. Do you (a) search for useful information or (b) keep moving?", "a"),
    ("You encounter a zombie blocking your path. Do you (a) fight it or (b) find another route?", "b"),
    ("You find a radio. Do you (a) try to contact others or (b) ignore it?", "a"),
    ("You come across a farm. Do you (a) scavenge for food or (b) keep moving?", "a"),
    ("You see a helicopter in the sky. Do you (a) signal it or (b) stay hidden?", "b"),
    ("You find a medical kit. Do you (a) use it now or (b) save it for later?", "a"),
    ("You encounter a locked gate. Do you (a) climb over it or (b) look for another entrance?", "a"),
    ("You hear children crying. Do you (a) help them or (b) avoid the noise?", "a"),
    ("You find a motorcycle. Do you (a) ride it or (b) leave it?", "a"),
    ("You come across a zombie nest. Do you (a) destroy it or (b) avoid it?", "b"),
    ("You find a cave. Do you (a) explore it or (b) stay outside?", "b"),
    ("You see a flare in the distance. Do you (a) investigate or (b) ignore it?", "b"),
    ("You find a boat. Do you (a) sail it or (b) stay on land?", "b"),
    ("You encounter a zombie dog. Do you (a) fight it or (b) avoid it?", "b"),
    ("You find a stash of weapons. Do you (a) take them or (b) leave them?", "a"),
    ("You see a group of zombies fighting each other. Do you (a) sneak past or (b) attack while they're distracted?", "a"),
    ("You find a bunker. Do you (a) enter or (b) keep moving?", "a"),
    ("You hear a scream. Do you (a) investigate or (b) stay away?", "b"),''
    ("You find a garden. Do you (a) gather food or (b) keep moving?", "a"),
    ("You see a zombie climbing a fence. Do you (a) wait for it to  ]come down or (b) climb over while it's distracted?", "b"),
    ("You find a group of friendly survivors. Do you (a) join them or (b) stay alone?", "b"),
    ("You come across a river with a broken bridge. Do you (a) try to repair it or (b) find another way across?", "b"),
    ("You find a stash of clean water. Do you (a) take it or (b) leave it?", "a"),
    ("You see a zombie horde approaching. Do you (a) hide or (b) prepare to fight?", "a"),
    ("You find an old library. Do you (a) search for useful information or (b) keep moving?", "a"),
    # Add more unique scenarios as needed...
]

# Repeat scenarios to reach 100 choices
while len(choices) < 100:
    scenario, correct = random.choice(choices)
    choices.append((f"{scenario} (repeat)", correct))

for i, (scenario, correct) in enumerate(choices, 1):
    print(f"\nChoice {i}:")
    print(scenario)
    answer = input("Your choice (a/b): ").strip().lower()
    if answer == correct:
        print("Good choice! You survive this round.")
    else:
        health -= 5
        print("Wrong choice! You lose 5 health.")
    print(f"Current health: {health}")
    if health <= 0:
        print("You have run out of health. Game over!")
        break

if health > 0:
    print("\nCongratulations! You survived all 100 choices in the zombie apocalypse!")
else:
    print("\nYou didn't make it through the apocalypse. Better luck next time!")
