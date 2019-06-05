import random
random_number=int(random.randint(1,20))

def get_value():
    global guess_number
    guess_number=int(input("Guess a number between 1 to 20:"))
    return(guess_number)

guess_number = get_value()

while True:
    if guess_number > random_number:
            print("My number is lower than {}".format(guess_number))
            get_value()
    elif guess_number<random_number:
            print("My number is greater than {}".format(guess_number))
            get_value()
    elif random_number == guess_number :
            print("congratulation.your guess {} was right!".format(guess_number))
            break

    

