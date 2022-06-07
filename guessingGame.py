import random
print("Welcom to the number guessing game!")
number = random.randint(1, 9)
chances = 0
print("Guess a number between 1 and 9:")

while chances < 5:
    guess = int(input("Input your guess:"))

    if guess == number:
        print("You guessed correctly!")
        break

    elif guess < number:
        print("You guessed too low. Guess a number greater than", guess)

    else:
        print("You guessed too high. Guess a number less than", guess)

    chances += 1

if not chances < 5:
    print("How did you not guess it, you had 5 chances. Anyways, the number is", number)