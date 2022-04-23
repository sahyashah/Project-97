import random
Number= random.randint(1,9)
Chances= 0
while Chances < 5:
    Guess=int(input("enter your guess"))
    if Guess==Number:
        print("spot on")
        break
    if not Chances < 5:
        print("You Lose Better Luck Next Time the number was",Number)
