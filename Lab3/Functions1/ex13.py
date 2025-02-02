import random
play = True
name = input("Hello! What is your name? ")
def game():
    global play
    global name
    x = random.randint(1, 21)
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
    count = 0
    while(True):
        u = input()
        if u.lower()=='q':
            print(f"Ok good bye, {name}")
            play = False
            break
        else:
            u = int(u)
        if(u<x):
            print("Your guess is too low.\nTake a guess.")
            count+=1
        elif u>x:
            print("Your guess is too high.\nTake a guess.")
            count+=1
        else:
            count+=1
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break

while(play == True):
    game()

    