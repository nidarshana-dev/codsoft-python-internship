import random

print("=== Rock Paper Scissors Game ===")
print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock")

user_score = 0
computer_score = 0

while True:
    print("\nChoose: Rock, Paper, or Scissors")
    user_choice = input("Your choice: ").lower()
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Type rock, paper, or scissors.")
        continue
    
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    
    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You Win! 🎉")
        user_score += 1
    else:
        print("Computer Wins! 💻")
        computer_score += 1
    
    print(f"\nScore - You: {user_score} | Computer: {computer_score}")
    
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != 'yes':
        print("\n=== Final Score ===")
        print(f"You: {user_score} | Computer: {computer_score}")
        if user_score > computer_score:
            print("You are the Champion! 🏆")
        elif computer_score > user_score:
            print("Computer wins this time! Try again.")
        else:
            print("It's a draw overall!")
        print("Thanks for playing!")
        break
