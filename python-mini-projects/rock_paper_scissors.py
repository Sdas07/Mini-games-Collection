import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    return input("Choose rock, paper, or scissors: ").lower()

def decide_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win! 🏆"
    else:
        return "You lose! 😢"

print("🎮 Welcome to Rock Paper Scissors!")
user_choice = get_user_choice()
computer_choice = get_computer_choice()

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}")
print("\nResult:", decide_winner(user_choice, computer_choice))
