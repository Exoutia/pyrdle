from random import choice
import pathlib
from string import ascii_letters

def get_random_word(word_list: list, num: int = 5):
    """Get a random five leter word (default 5 you can change it using num key)


    Args:
        word_list (list): this is the list from where the word will be chosen
        num (int, optional): the size of word want to get. Defaults to 5.

    Returns:
        str: this is the word which will be chosen

    ## Example
    >>> get_random_word(['snake', 'worm', 'it-is'])
    'SNAKE'
    """

    words = [
    word.upper()
    for word in word_list
    if len(word) == num and all(letter in ascii_letters for letter in word)
    ]

    return choice(words) #nosec

def show_guess(guess_word: str, correct_word: str):
    """Show the user's guess on the terminal and classify all the letters
    ## Example:
    >>> show_guess("CRANE", "SNAKE")
    Correct letters: A, E
    Misplaced letters: N
    Wrong letters: C, R

    Args:
        guess_word (str): the word user has guessed
        correct_word (str): the correct word
    """

    correct_letters = {
        letter for letter, correct in zip(guess_word, correct_word) if letter == correct
    }
    misplaced_letters = set(guess_word) & set(correct_word) - correct_letters
    wrong_letters = set(guess_word) - set(correct_word)

    print(f'Correct letters: {", ".join(sorted(correct_letters))}')
    print(f'Misplaced letters: {", ".join(sorted(misplaced_letters))}')
    print(f'Wrong letters: {", ".join(sorted(wrong_letters))}')


def game_over(word):
    print(f'The word was {word}')

def main():
    # pre-process
    words_path = pathlib.Path(__file__).parent/'wordList.txt'
    word_list = words_path.read_text(encoding='utf-8').split('\n')
    word = get_random_word(word_list)

    # Process (main loop)
    for guess_num in range(1, 7):
        guess = input(f'\nGuess {guess_num}: ').upper()

        show_guess(guess, word)
        if guess == word:
            print("This is the correct word bro.")
            break

    # Post-process
    else:
        game_over(word)

if __name__ == "__main__":
    main()

