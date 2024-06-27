import random

def write_highscore(score):
    with open("Hi_score.txt", "r") as file:
        prev_highscore = file.read()
        if (prev_highscore == ""):
            prev_highscore = 0
        else:
            prev_highscore = int(prev_highscore)
            
    if score > prev_highscore or prev_highscore == "":
        print("Highscore_was", prev_highscore)
        print("New score is", score)

        with open("Hi_score.txt", "w") as file:
            file.write(str(score))

def game():
    print("You playing this game")
    score = random.randrange(1, 60)
    write_highscore(score)


game()