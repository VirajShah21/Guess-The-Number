import dice ; import compare

print 'Instructions:'
print 'You have 10 tries to guess what the number I am thinking of is'
print 'My number is between 1 and 100'
print
print


guess = None

while True:
    answer = dice.dice()
    while guess != answer:
        guess = input('What number am I thinking of: ')
        compare.stuff(guess,answer)
