import random

print ("pick a number from 1 to 100 you have 7 guesses")

hidden_number = random.randint(0,100)

#randint = random intager.

for i in range(7) :  
    #this is the start of repeat lines 11-19.
    firstnumber1 = int(input("Guess a number between  0-100"))
    if firstnumber1 == hidden_number:
        print ("yup you somehow got it!")
        quit ()
    elif hidden_number > firstnumber1:
        print ("um no... try again. Higher")
    elif hidden_number < firstnumber1:
        print ("no man, its lower than that.")
        #end of repeat lines 10-19 bye.
print("nope you failed c'mon lets play again.")
