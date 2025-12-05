# write a function that stores information about a car in a dictionary
def car_info(make, model, **options):
    car = {'make': make.title(), 'model': model.title()}
    for key, value in options.items():
        car[key] = value
    return car
# call the function to make a car with different features
car1 = car_info('subaru', 'outback', color='blue', tow_package=True)
car2 = car_info('tesla', 'model s', color='red', autopilot=True, battery='long range')
car3 = car_info('ford', 'mustang', color='black', convertible=True, year=2021)
# print each return value to show that the dictionary is storing the car information correctly
print(car1)
print(car2)
print(car3) 
