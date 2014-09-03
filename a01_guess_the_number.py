from random import randrange
min_value = 1
max_value = 100
secret_number = randrange(min_value, max_value + 1)
trials = 0
guess = 0
print("Input your guess: ")
while guess != "":
    try:
        guess = input()
        guess_int = int(guess)
    except:
        print("Please, input a number between" + str(min_value) + " and " + str(max_value))
        continue
    if guess_int < min_value or guess_int > max_value:
        print("Please, input a number between" + str(min_value) + " and " + str(max_value))
        continue
    trials += 1
    if secret_number > guess_int:
        print("The secret number is higher! Try once more: ")
    elif secret_number < guess_int:
        print("The secret number is lower! Try once more: ")
    else:
        print("Congratulations! " + guess + " is correct number!")
        print("You have made " + str(trials) + " trials.")
        break

