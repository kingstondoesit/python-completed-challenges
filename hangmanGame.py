import random

def get_word_and_hint():
    """
    Returns a randomly selected word and its corresponding hint.
    """
    words_and_hints = {
        "python": "A popular programming language.",
        "hangman": "A classic word-guessing game.",
        "lion" : "Popularly described as the king of the jungle",
        "cheetah" : "fastest animal in the cat family",
        "caat": "A common household pet (misspelled intentionally for the game).",
        "elephant": "The largest land animal."
        #add more keys (words) and hints (values) to the dict
    }
    word = random.choice(list(words_and_hints.keys()))
    hint = words_and_hints[word]
    return word, hint

def hangman(word, hint):
    """
    Handles the Hangman game logic. The computer sets a word, and the player guesses the letters.
    """
    wrong_guesses = 0
    stages = ["", "________", "| |", "| 0", "| /|\\", "| / \\", "| "]
    letters_left = list(word)
    score_board = ['__'] * len(word)
    win = False
    print('Welcome to Hangman')

    while wrong_guesses < len(stages) - 1:
        print('\n')
        print(f"Hint: {hint}")
        guess = input("Guess a letter: ").strip().lower()
        if guess in letters_left:
            character_index = letters_left.index(guess) #index method .index(value, start, end)
            score_board[character_index] = guess
            letters_left[character_index] = '$'
        else:
            wrong_guesses += 1

        print(' '.join(score_board))
        print('\n'.join(stages[0: wrong_guesses + 1]))

        if '__' not in score_board:
            print('You win! The word was:')
            print(' '.join(score_board))
            win = True
            break

    if not win:
        print('\n'.join(stages))
        print(f'You lose! The word was {word}')

def main():
    """
    Main function to control the flow of the game and handle replayability.
    """
    while True:
        word, hint = get_word_and_hint()
        hangman(word, hint)
        while True:
            play_again = input("Do you want to play again? (yes/no):").strip().lower()
            if play_again in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'.")

        if play_again == 'no':
            break
    print("Next time then. Thanks for playing!")

if __name__ == "__main__":
    main()