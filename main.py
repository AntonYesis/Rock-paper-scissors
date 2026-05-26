import random

options = ["rock", "scissors", "paper"]

player_score = 0
computer_score = 0
rounds = 3

print("Welcome to the game!")
print("Rock, Paper, Scissors")
print(f"Playing {rounds} rounds\n")

for round_num in range(1, rounds + 1):
    print(f"\n--- Round {round_num} ---")

    player_choice = input("Enter value (rock, scissors, paper): ").lower()

    while player_choice not in options:
        player_choice = input("Error! Enter rock, scissors, or paper: ").lower()

    # Computer's choice
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "scissors" and computer_choice == "paper") or \
            (player_choice == "paper" and computer_choice == "rock"):
        print("You won the round!")
        player_score += 1
    else:
        print("Computer won the round!")
        computer_score += 1

    print(f"Score: Player {player_score} : {computer_score} Computer")

print("\n" + "=" * 30)
print("GAME OVER!")
print(f"Final score: Player {player_score} : {computer_score} Computer")

if player_score > computer_score:
    print("🎉 CONGRATULATIONS! YOU ARE THE WINNER! 🎉")
elif computer_score > player_score:
    print("💻 COMPUTER WINS! Better luck next time! 💻")
else:
    print("🤝 IT'S A TIE! Great game! 🤝")
