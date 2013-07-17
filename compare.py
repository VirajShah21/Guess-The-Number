def stuff(guess,answer):
    if guess > answer:
        print 'Too high, go for a lower guess'
    if guess < answer:
        print 'Too low, go for a higher guess'
    if guess == answer:
        print 'Correct, lets play again'
        
