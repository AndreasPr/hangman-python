import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6
print(logo)
display = []

for letter in chosen_word:
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose!')
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])