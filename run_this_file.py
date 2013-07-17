import dice
import compare

print('Instructions:')
print('You have 10 tries to guess what the number I am thinking of is')
print('My number is between 1 and 100')
print('Type q to quit')
print()
print()


guess = None

while True:
    # initialize answer and try counter
    answer = dice.dice()
    tries = 0
    while guess != answer:
        guess = input('What number am I thinking of: ')

        # exit if player hits q
        if guess == 'q':
            print('Bye!')
            exit()

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
