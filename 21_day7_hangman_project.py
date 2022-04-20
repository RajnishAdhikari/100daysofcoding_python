import random
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)


end_of_game = False 
lives = 6
from hangman_art import logo
print(logo)

display = []
for _ in range(word_length):
    display += "_"


end_of_game = False

while not end_of_game:
    guess = input("Guess a Letter:").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"current position:{position}\nCurrent letter: {letter}\n Guessed letter:{guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
        

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")


    from hangman_art import stages
    print(stages[lives])
        

