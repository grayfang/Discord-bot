import random

def roll_d20():
    randInt = random.randint(1, 20)
    if randInt == 1:
        return f"You rolled a {randInt}. Ldance."
    elif randInt == 20:
        return f"You rolled a {randInt}. You are based."
    else:
        return f"You rolled a {randInt}."
