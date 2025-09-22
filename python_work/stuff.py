
print("the car is about to collide with your car")
see_it_in_time = True
response = "1 second"
response = "5 seconds"
response = input("how fast did you see it?(1 second/5 seconds): ") .strip().lower()
if see_it_in_time and response == "1 second":
    print("swerve")

elif see_it_in_time and response in ("5 seconds", "4 seconds", "3 seconds", "2 seconds"):
    print("hit the brakes")
elif see_it_in_time and response in ("0 seconds"):
    print("you are dead")
