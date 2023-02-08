from random import choice
import pathlib
from string import ascii_letters

def get_random_word(num: int = 5):
    WORDLIST = pathlib.Path('wordList.txt')

    words = [
    word.upper()
    for word in WORDLIST.read_text(encoding='utf-8').split('\n')
    if len(word) == num and all(letter in ascii_letters for letter in word)
    ]

    return choice(words) #nosec

def show_guess(guess_word: str, correct_word: str):
    correct_letters = {
        letter for letter, correct in zip(guess_word, correct_word) if letter == correct
    }
    misplaced_letters = set(guess_word) & set(correct_word) - correct_letters
    wrong_letters = set(guess_word) - set(correct_word)

    print(f'Correct letters: {", ".join(sorted(correct_letters))}')
    print(f'Misplaced Letters: {", ".join(sorted(misplaced_letters))}')
    print(f'Wrong Letters: {", ".join(sorted(wrong_letters))}\n')


def game_over(word):
    print(f'The word was {word}')

def main():
    # pre-process
    word = get_random_word()

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

