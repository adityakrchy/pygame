print("Lets Start the Game")
word = "Aditya"
guess = ""
guess_limit = 3
no_of_guess = 0
out_of_guess = False

while guess != word and not(out_of_guess):
    if no_of_guess<guess_limit:
        guess = input("Enter Guess: ")
        no_of_guess += 1
    else:
        out_of_guess = True
        

if no_of_guess == guess_limit:
    print("You loose")
else:
    print("You win!!")