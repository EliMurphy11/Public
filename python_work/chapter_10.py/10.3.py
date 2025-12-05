# Prompt for user's name and append it to guests.txt

def main():
    name = input("What's your name? ").strip()
    if not name:
        print("No name entered.")
        return

    guests_path = "guests.txt"
    try:
        with open(guests_path, "a", encoding="utf-8") as f:
            f.write(name + "\n")
        print(f"Thanks, {name}. Your name was added to {guests_path}.")
    except OSError as e:
        print("Could not write to file:", e)

if __name__ == "__main__":
    main()
#jfilepath: /Users/reginamurphy/Public/python_work/chapter_10.py/10.2.py