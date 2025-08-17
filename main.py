import random
import time


game = ["rock","paper","sissor"]
random_item = random.choice(game)

print("\n\nWELCOME TO THE GAME\n")

while True:
    round = input("How many rounds you want to play: ")
    try:
        int_round = int(round)
        break
    except:
        print("❕enter in integer")

score = 0
for i in range(int_round):
    print(f"Round: {i+1}")
    user = input("Choose (Rock, Paper, Sissor) : ").strip().lower()
    if user not in ["rock","paper","sissor"]:
        print("choose in (Rock, Paper, Sissor)")
    else:
        print("bot choosing...")
        time.sleep(1)
        if user == random_item:
            print("You win")
            score += 1
            print(score)

        else: 
            print("You loose")

   
print(f"You scored {score}")
