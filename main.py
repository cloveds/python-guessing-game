import random

def main():
    gamemode = input("1. Easy (1-10)\n2. Medium (1-100)\n3. Hard (1-1000)\n> ")
    if gamemode == "1":
        max = 10
    elif gamemode == "2":
        max = 100
    elif gamemode == "3":
        max = 1000
    else:
        print("Invalid option")
        exit()
    num = random.randint(1, max)
    guess = int(input(f"Guess a number between 1 and {max}: "))
    if guess > max or guess < 0:
        print("Not within range!")
        exit()
    if guess > num:
        print(f"Too big, the number was {num}")
    elif guess < num:
        print(f"Too small, the number was {num}")
    else:
        print("You got it right!")

if __name__ == "__main__":
    main()