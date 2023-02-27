import random

foods = []

def load_foods():
    global foods
    with open("foods.txt", "r") as file:
        for line in file:
            food = line.strip()
            foods.append(food)
        print(f"Loaded foods from file: {foods}")

def get_random_food():
    global foods
    return random.choice(foods)

def add_food(food):
    with open("foods.txt", "a") as food_file:
        food_file.write(f"\n{food}")
        print(f"Added {food} to the food list")
