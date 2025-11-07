import random

questions = [
    ("What is the capital of France?", "paris"),
    ("What is 5 + 7?", "12"),
    ("Who wrote 'Romeo and Juliet'?", "shakespeare"),
    ("What planet is known as the Red Planet?", "mars"),
    ("What is the largest mammal?", "blue whale"),
    ("How many continents are there?", "7"),
    ("What is the boiling point of water in Celsius?", "100"),
    ("Who painted the Mona Lisa?", "da vinci"),
    ("What is the fastest land animal?", "cheetah"),
    ("What is the smallest prime number?", "2"),
    ("What is the chemical symbol for gold?", "au"),
    ("Who is the author of 'Harry Potter'?", "rowling"),
    ("What is the square root of 64?", "8"),
    ("What is the largest ocean?", "pacific"),
    ("What is the hardest natural substance?", "diamond"),
    ("What is the capital of Japan?", "tokyo"),
    ("What is the tallest mountain in the world?", "everest"),
    ("What is the main gas found in the air we breathe?", "nitrogen"),
    ("Who discovered gravity?", "newton"),
    ("What is the longest river in the world?", "nile"),
]

score = 0
count = 0

print("Answer trivia questions! For every correct answer, the count goes up by 5. If you get one wrong, you lose 5. Reach 100 to win!")

while count < 100:
    q, a = random.choice(questions)
    user_answer = input(f"{q} ").strip().lower()
    if user_answer == a:
        count += 5
        score += 1
        print(f"Correct! Count is now {count}.")
    else:
        count = max(0, count - 5)
        print(f"Wrong! Count is now {count}.")
    print(f"Questions answered correctly: {score}")

print("Congratulations! You've reached 100 and won the game!")
