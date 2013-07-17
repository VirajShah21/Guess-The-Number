# Compares guess and answer and prints out the correct response.
# returns True if the guess is correct, and False if the guess is wrong.

def stuff(guess,answer):
    if guess > answer:
        print('Too high, go for a lower guess')
        return False
    if guess < answer:
        print('Too low, go for a higher guess')
        return False
    if guess == answer:
        print('Correct, lets play again')
        return True
        
