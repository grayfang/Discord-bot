def load_scores():
    scores = {}
    with open("scores.txt", "r") as file:
        for line in file:
            name, score = line.strip().split(": ")
            scores[name] = int(score)
        print(f"Loaded scores from file: {scores}")
    return scores

def save_scores(scores):
    with open("scores.txt", "w") as file:
        for name, score in scores.items():
            file.write(f"{name}: {score}\n")

def get_scores():
    scores = {}
    with open("scores.txt", "r") as file:
        for line in file:
            name, score = line.strip().split(": ")
            scores[name] = int(score)
        print(f"Loaded scores from file: {scores}")
    return scores

def print_scores():
    scores = get_scores()
    output = "\n".join([f"{name}: {score}" for name, score in scores.items()])
    return f"```{output}```"

