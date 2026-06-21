import random

print("🎮 Welcome to Rock, Paper, Scissor Game! 🎮")
choices = ["rock", "paper", "scissor"]
computer = random.choice(choices)

user = input("🪨 📄 ✂️ Enter Rock, Paper or Scissor: ").lower()
print(f"\n💻 Computer chose: {computer}")

if computer == user:
    print("🤝 It's a Draw!")

elif (user == "rock" and computer == "scissor") or (user == "scissor" and computer == "paper") or (user == "paper" and computer == "rock"):
    print("🎉 Congratulations! You Win! 🏆")

else:
    print("😢 Computer Wins!")
    print("💪 Better luck next time!")
