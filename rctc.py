import random
import time
from colorama import init, Fore

# random cmd text colour
def ctext(text: str, repeat: int, delay: int) -> None:
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]

    for i in range(repeat):
        print(colors[i % len(colors)] + text, end="\r", flush=True)
        time.sleep(delay)
    r_color = random.choice(colors)
    return r_color + text


if __name__ == "__main__":
    ctext()
