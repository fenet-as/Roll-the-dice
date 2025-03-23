import random


def rollDice():
    while True:
        t = input('Roll the dice ? (yes or no): ').lower()
        die1 = random.randint(1, 6)
        if t == "yes" :
            print(f"You rolled a {die1}")
        elif t == "no":
            print("Thanks for playing")
            break
        else:
            print("Invalid choice please say yes or no.")

rollDice()
