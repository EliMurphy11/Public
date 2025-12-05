#  five restaurant foods 
foods = ["pizza", "sushi", "tacos", "pasta", "burgers"]
for food in foods:
    print(food)
new_foods = [ "ramen", "steak"]
foods_removed = ["tacos", "pasta"]
for food in new_foods:
    foods.append(food)
for food in foods_removed:
    foods.remove(food)
print("\nUpdated food list:")
for food in foods:
    print(food)