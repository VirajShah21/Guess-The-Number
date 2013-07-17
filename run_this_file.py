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
    answer = dice.dice()
    tries = 0
    while guess != answer:
        guess = input('What number am I thinking of: ')
        if guess == 'q':
            print('Bye!')
            exit()
        tries += 1
        correct = compare.stuff(int(guess),answer)

        if correct:
            break

        if tries == 10:
            print('Sorry, your 10 tries are up. The number was %s. Lets play again.' % answer)
            break
