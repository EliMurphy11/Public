people_poll = {"roberto, sharalanda, shoobydooah, shanaynay, shaniqua, georgeicus, jamal, latasha, latoya, latrell, latonya, latrice, latisha, latavia"}
favorite_languages = {
    "roberto": "python",
    "sharalanda": "c++",
    "shoobydooah": "ruby",
    "shanaynay": "java",
}
for name in people_poll:
    if name in favorite_languages.keys():
        print(f"thank you {name} for taking the poll")
    else:
         print(f"{name} please take the poll")
name = input("enter your name: ").strip().lower()
if name in favorite_languages.keys():
    print(f"thank you {name} for taking the poll")
else:
   print(f"your response has already been entered you clanka")
   

