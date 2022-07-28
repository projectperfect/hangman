from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

from hangman_art import logo
print(logo)

from hangman_art import stages
    print(stages[lives])