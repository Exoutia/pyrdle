from random import choice
import pathlib
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme
console = Console(width=40, theme=Theme({'warning': 'red on yellow'}))

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


def styled_show_guess(guesses, word):
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = 'bold white on green'
            elif letter in word:
                style = 'bold white on yellow'
            elif letter in ascii_letters:
                style = 'white on #666666'
            else:
                style = 'dim'
            styled_guess.append(f'[{style}]{letter}[/]')
        console.print(''.join(styled_guess), justify='center')

def game_over(word):
    print(f'The word was {word}')


def refresh_page(headline):
    console.clear()
    console.rule(f'[bold blue]:leafy_green: {headline} :leafy_green:[/]')


def main():
    # pre-process
    words_path = pathlib.Path(__file__).parent/'wordList.txt'
    word_list = words_path.read_text(encoding='utf-8').split('\n')
    word = get_random_word(word_list)
    guesses = ["_"*5]*6

    # Process (main loop)
    for idx in range(6):
        refresh_page(f"Guess {idx + 1}")
        styled_show_guess(guesses, word)

        guesses[idx] = input('\nGuess word: ').upper()
        if guesses[idx] == word:
            print("This is the correct word bro.")
            refresh_page(f"Guess {idx + 1}")
            styled_show_guess(guesses, word)
            break

    # Post-process
    game_over(guesses, word)

if __name__ == "__main__":
    main()

