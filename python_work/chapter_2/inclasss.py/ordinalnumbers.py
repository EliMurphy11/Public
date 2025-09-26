print("Think of a celebrity. I will try to guess who it is by asking you questions!")

questions = [
    ("Is the celebrity an actor?", "actor"),
    ("Is the celebrity a musician?", "musician"),
    ("Is the celebrity alive?", "alive"),
    ("Is the celebrity male?", "male"),
    ("Is the celebrity female?", "female"),
    ("Is the celebrity known for movies?", "movies"),
    ("Is the celebrity known for sports?", "sports"),
    ("Is the celebrity American?", "american"),
    ("Is the celebrity British?", "british"),
    ("Is the celebrity under 40 years old?", "under40"),
    ("Is the celebrity over 60 years old?", "over60"),
    ("Is the celebrity famous for comedy?", "comedy"),
    ("Is the celebrity a singer?", "singer"),
    ("Is the celebrity a rapper?", "rapper"),
    ("Is the celebrity a politician?", "politician"),
    ("Is the celebrity a YouTuber?", "youtuber"),
    ("Is the celebrity a reality TV star?", "reality"),
    ("Is the celebrity known for fashion?", "fashion"),
    ("Is the celebrity an athlete?", "athlete"),
    ("Is the celebrity an author?", "author"),
]

answers = {}

for i, (q, key) in enumerate(questions, 1):
    ans = input(f"Q{i}: {q} (yes/no): ").strip().lower()
    answers[key] = ans

# Simple guessing logic (for demonstration)
if answers["actor"] == "yes" and answers["male"] == "yes" and answers["alive"] == "yes" and answers["american"] == "yes":
    print("Are you thinking of Leonardo DiCaprio?")
elif answers["musician"] == "yes" and answers["female"] == "yes" and answers["alive"] == "yes" and answers["british"] == "yes":
    print("Are you thinking of Adele?")
elif answers["athlete"] == "yes" and answers["male"] == "yes" and answers["american"] == "yes":
    print("Are you thinking of LeBron James?")
elif answers["politician"] == "yes" and answers["male"] == "yes" and answers["american"] == "yes":
    print("Are you thinking of Barack Obama?")
elif answers["youtuber"] == "yes" and answers["male"] == "yes":
    print("Are you thinking of MrBeast?")
else:
    print("I couldn't guess your celebrity, but you can try again or add more celebrities to my list")