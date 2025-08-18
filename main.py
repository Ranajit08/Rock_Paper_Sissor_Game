import random
import time
from colorama import init, Fore, Style
from rctc import ctext
from loading import bar

init(autoreset=True)

loading()

while True:
    print("\n")
    print(f"{ctext("⫸ ^_^ WELCOME TO THE GAME ^_^", repeat=3, delay=0.5)}")
    time.sleep(2)
    print(ctext("⫸ How many rounds you want to play: ", repeat=2, delay=0.5))
    round = input("⫸")
    try:
        int_round = int(round)
        break
    except:
        print("❕enter in integer")

game = ["rock", "paper", "sissor"]
random_item = random.choice(game)
score = 0
for i in range(int_round):
    print(Fore.GREEN + Style.BRIGHT + f"ROUND: {i+1}")
    while True:
        user = input("🤔 Choose (Rock, Paper, Sissor) : ").strip().lower()
        if user not in ["rock", "paper", "sissor"]:
            print( Fore.RED + "❗choose in (Rock, Paper, Sissor)❗")
        else:
            print("🤖 bot choosing...")
            break
    time.sleep(1)
    if user == random_item:
        print("🏆 You win")
        score += 1
    else:
        print("💔 You loose")
    print('\n')

if score > 0:
    print(f"😍 You scored {score}")
else:
    print(f"😞 You scored {score}")

    
