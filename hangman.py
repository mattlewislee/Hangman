import random
words = ['apple', 'hello', 'phase', 'plant', 'prune', 'pasta', 'doggy', 'puppy']
target = random.choice(words)
guessed_letters = set()

correct_guess = False
fails = 0
max_attempts = 6
current_status = '_' * len(target)
while not correct_guess:
    new_letter = input()[0]
    if new_letter in guessed_letters:
        print('you have tried',  new_letter)
       	continue
    guessed_letters.add(new_letter)
    if new_letter in target:
        print('good guess!')
        current_status = ''.join([char if char in guessed_letters else '_' for char in target])
        if not '_' in current_status:
            print('You got it!')
            correct_guess = True
    else:
        fails += 1
        print(max_attempts - fails, 'goes left')
    print(current_status)
    if fails == max_attempts:
        print('game_over :(')
        break