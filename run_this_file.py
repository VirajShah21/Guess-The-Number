import dice
import compare

print('Instructions:')
print('You have 10 tries to guess what the number I am thinking of is')
print('My number is between 1 and 100')
print('Type q to quit')
print()
print()


while True:
    # initialize answer, try counter, and guess
    answer = dice.dice()
    tries = 0
    guess = None
    while guess != answer:
        guess = raw_input('What number am I thinking of: ')
        #checks value if can be converted into an integer 
        #and converts it if possible
        #then uses answer as a guess
        if guess.isdigit():
            guess = int(guess)
            # player tried again
            tries += 1
            # check against answer
            correct = compare.stuff(int(guess),answer)

            # player won, start a new game
            if correct:
                break

            # player ran out of tries, start a new game
            if tries == 10:
                print('Sorry, your 10 tries are up. The number was %s. Lets play again.' % answer)
                break

        #checks value if it contains ANY letters in it
        else:
            if guess.isalpha():
                guess = str(guess)
                # exit if player hits q
                if guess == 'q':
                    print('Bye!')
                    exit()
                else:
                    print('This command is invalid')
