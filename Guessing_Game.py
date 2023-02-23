import random

intMin = int(input("Input a number that will be the minimum of the range: "))
intMax = int(input("Input a number that will be the maximum of the range: "))
numOfGuesses = 1
randomNumber = random.randint(intMin, intMax)#range of the random number is dependent on user
guess = intMin - 1

while numOfGuesses <= 10 and guess != randomNumber:#while loop to check if 10 chances are spent and guess is still not correct
    try:
        guess = int(input("\nInput your guess on what the random number is: "))
        if guess < intMin or guess > intMax:#checking the guess if within range of the given
            raise Exception
    except:
        if (guess < intMin or guess > intMax) and str(guess).lstrip('-').isdigit():#since isdigit fxn doesnt really see negative in string, we remove '-' using lstrip
            guess = intMin#resets the guess value in order to have the correct error (if string is entered, previous value of guess is used)
            print("Input out of Range\nNumber of guesses remains the same")
        else:
            print("Wrong Input!\nNumber guesses remains the same")
    else:    
        if(guess == randomNumber):
            print("Correct!\nNumber of Guesses: %d\n" % (numOfGuesses))
            break
        elif (guess > randomNumber):
            print("Wrong! Guess is higher than the random number!\n")
        else:
            print("Wrong! Guess is lower than the random number!\n")
        numOfGuesses += 1
            
print("The Randomed Number is: %d" % randomNumber)