# Simple conversation about cinnamon rolls

print("Hi there! Do you like cinnamon rolls?")
answer = input("Your answer: ")

if answer.lower() in ["yes", "y", "sure", "of course"]:
    print("Me too! They're so delicious and sweet.")
    print("Do you prefer them with icing or without?")
    icing = input("With icing or without? ")
    if "with" in icing.lower():
        print("Icing makes them extra tasty!")
    else:
        print("Without icing, you can really taste the cinnamon.")
else:
    print("That's okay! Not everyone likes cinnamon rolls.")
    print("What's your favorite pastry?")
    pastry = input("Favorite pastry: ")
    print(f"{pastry} sounds delicious! I'll have to try it sometime.")