# create a code that simulates a simple Madden NFL game scenario and allows user interaction that affects the outcome
import random
import time
print("Welcome to the Madden NFL Game Simulation!")
teams = ["Patriots", "Chiefs", "Packers", "Rams", "49ers"]
team1 = random.choice(teams)
team2 = random.choice([team for team in teams if team != team1])
print(f"Today's game is between the {team1} and the {team2}!")
score1 = 0
score2 = 0
# make choices that the user can select that will affect the outcome of the game
for quarter in range(1, 5): 
    print(f"\nQuarter {quarter}:")
    time.sleep(1)
    play = input("Choose your play (run/pass/field goal): ").lower()
    if play == "run":
        points = random.randint(0, 7)
        score1 += points
        print(f"{team1} executed a run play and scored {points} points!")
    elif play == "pass":
        points = random.randint(0, 7)
        score1 += points
        print(f"{team1} executed a pass play and scored {points} points!")
    elif play == "field goal":
        points = random.randint(0, 3)
        score1 += points
        print(f"{team1} attempted a field goal and scored {points} points!")
    else:
        print("Invalid play choice. No points scored this quarter.")
    
    # Simulate opponent's turn
    opp_play = random.choice(["run", "pass", "field goal"])
    if opp_play == "run":
        points = random.randint(0, 7)
        score2 += points
        print(f"{team2} executed a run play and scored {points} points!")
    elif opp_play == "pass":
        points = random.randint(0, 7)
        score2 += points
        print(f"{team2} executed a pass play and scored {points} points!")
    elif opp_play == "field goal":
        points = random.randint(0, 3)
        score2 += points
        print(f"{team2} attempted a field goal and scored {points} points!")
    elif opp_play == "field goal":
        points = random.randint(0, 3)
        score2 += points
        print(f"{team2} attempted a field goal and scored {points} points!")
    elif opp_play == "field goal":
        points = random.randint(0, 3)
        score2 += points
        print(f"{team2} attempted a field goal and scored {points} points!")
    
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