import random
import time

def display_intro():
    print("🎮 Welcome to the Interactive Hand Game Simulator 🎮")
    print("--------------------------------------------------")
    print("Rules:")
    print("👉 Rock beats Scissors")
    print("👉 Scissors beats Paper")
    print("👉 Paper beats Rock")
    print("--------------------------------------------------")

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("❌ Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def main():
    display_intro()
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice.capitalize()}")
        time.sleep(0.5)
        print(f"Computer chose: {computer_choice.capitalize()}\n")
        time.sleep(0.5)

        winner = determine_winner(user_choice, computer_choice)

        if winner == "draw":
            print("It's a draw! 🤝")
        elif winner == "user":
            print("You win this round! 🏆")
            user_score += 1
        else:
            print("Computer wins this round! 💻")
            computer_score += 1

        print(f"\nScoreboard -> You: {user_score} | Computer: {computer_score}")
        print("--------------------------------------------------")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! 👋")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()