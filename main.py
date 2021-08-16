import random

print("welcome to my Number Guessing Game!")

max_num = input("Enter a number: ")
if max_num.isdigit():
    max_num = int(max_num)
    if max_num <= 0:
        print("Enter a number greater than 0")
        quit()
else:
    print("Invalid Input")
    quit()

random_num = random.randint(0, max_num)
count = 0
print("--You'll have a maximum number of 3 guesses in total--")

while True:
    count += 1
    guess = input(f"Make a guess between 0 and {max_num}: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Invalid Input")
        continue
    if guess > max_num:
        print(f"Enter a number below than {max_num}")
    if guess == random_num:
        print(f"You've got it correct in {count} guesses!")
        break

    else:
        print("You've got it Incorrect:/ ")
    if count >= 3:
        print("Game over! ")
        break
