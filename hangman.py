import random
from pathlib import Path
words = Path('words_list.txt').read_text()

with open('words_list.txt', 'r') as f:
    words = f.readlines()

words_longer_than_four_letters = []
for word in words:
    word = word.rstrip("\n")
    if len(word) > 3:
        words_longer_than_four_letters.append(word)







# target_word = random.choice(words)
#
#
# guessed_letters = set()
#
# correct_guess = False
# fails = 0
# max_attempts = 6
# current_status = '_' * len(target_word)
# while not correct_guess:
#     new_letter = input()[0]
#     if new_letter in guessed_letters:
#         print('you have tried',  new_letter)
#        	continue
#     guessed_letters.add(new_letter)
#     if new_letter in target_word:
#         print('good guess!')
#         current_status = ''.join([char if char in guessed_letters else '_' for char in target_word])
#         if not '_' in current_status:
#             print('You got it!')
#             correct_guess = True
#     else:
#         fails += 1
#         print(max_attempts - fails, 'goes left')
#     print(current_status)
#     if fails == max_attempts:
#         print('game_over :(')
#         break
