# creating a code that plays a simple baseball game simulation
import random
import time
print("Welcome to the Baseball Game Simulation!")
teams = ["Red Sox", "Yankees", "Dodgers", "Cubs", "Giants"]
team1 = random.choice(teams)
team2 = random.choice([team for team in teams if team != team1])
print(f"Today's game is between the {team1} and the {team2}!")
score1 = 0
score2 = 0
# make choices that the user can select thatv will affect the outcome of the game
for inning in range(1, 10):
    print(f"\nInning {inning}:")
    time.sleep(1)
    run1 = random.randint(0, 3)
    run2 = random.randint(0, 3)
    score1 += run1
    score2 += run2
    print(f"{team1} scored {run1} runs.")
    print(f"{team2} scored {run2} runs.")
    time.sleep(1)
print("\nFinal Score:")
print(f"{team1}: {score1}")
print(f"{team2}: {score2}")
if score1 > score2:
    print(f"{team1} wins!")
elif score2 > score1:
    print(f"{team2} wins!")
else:
    print("It's a tie!")
        