import random
import hangman_stages
word_list = ["apple", "orange", "banana"]
lives = 6
chosen_word = random.choice(word_list)
display = ['_' for _ in chosen_word]
print(display)

game_over = False

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in chosen_word:
        for position, letter in enumerate(chosen_word):
            if letter == guessed_letter:
                display[position] = guessed_letter

    else:
        lives -=1
        if lives == 0:
            game_over = True
            print("You Lose!!")
    print(display)

    if '_' not in display:
        game_over = True
        print("You Win!!")
    print(hangman_stages.stages[lives])
