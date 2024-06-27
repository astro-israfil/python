import random
computer_moves = ["rock", "paper", "scissor"]
computer_move = random.choice(computer_moves)

user_moves = {"r": "rock", "p": "paper", "s": "scissor"}
user_m = input("Please enter your move 'r' 'p' or 's' :  ")
user_move = user_moves.get(user_m)

if computer_move == user_move:
    print(f"Tie game you choose: {user_move} and computer choose: {computer_move}")
elif computer_move == "rock" and user_move == "scissor":
    print(f"You lose :_) you choose: {user_move} and computer choose: {computer_move} ")
elif computer_move == "scissor" and user_move == "paper":
    print(f"You lose :_) you choose: {user_move} and computer choose: {computer_move}")
elif computer_move == "paper" and user_move == "rock":
    print(f"You lose :_) you choose: {user_move} and computer choose: {computer_move}")
else:
    print(f"You win!!! you choose: {user_move} and computer choose: {computer_move}")
