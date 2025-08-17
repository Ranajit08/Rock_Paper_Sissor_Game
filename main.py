import random
import time

score = 0
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

for _ in range(int_round):
    user = input("Choose (Rock, Paper, Sissor) : ").strip().lower()
    if user in ["rock","paper","sissor"]:
        print("bot choosing...")
        time.sleep(1)
        global score
        if user == random_item:
            print("You win")
            score += 1
            print(score)

        else: 
            print("You loose")

    else:
        print("choose in (Rock, Paper, Sissor)")
    

   
print(f"Your scored {score}")