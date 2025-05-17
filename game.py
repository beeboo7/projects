import random

# title of the game
title = 'Wordz'

word_bank = []

letters_guessed_wrong = []
letters_in_wrong_place = []
max_turns = 5
turns_taken = 0

def read_file():
    with open('words.txt') as f:
        for line in f:
            # read each line from the file and add to word bank
            word_bank.append(line.strip().lower())

def generate_word():
    word_to_guess = random.choice(word_bank)
    return word_to_guess

def main():
    read_file()
    print(f'Welcome to {title}!')
    print('1. Play')
    print('2. Instructions')
    print('3. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        play()
    elif choice == '2':
        instructions()
    elif choice == '3':
        exit_game()
    else:
        print('Invalid choice. Please try again.')
        main()

def instructions():
    print('Instructions:')
    print('1. You have 5 turns to guess the 5 letter word.')
    print('2. After each guess, you will receive feedback on your guess.')
    print('3. A letter in the correct position will be marked with a *')
    print('4. A letter in the wrong position will be marked with a -')
    print('5. A letter not in the word will be marked with a X')
    print('Good luck!')
    main()

def exit_game():
    print('Thanks for playing!')
    return
    

def play():
    global turns_taken, letters_guessed_wrong, letters_in_wrong_place

    turns_taken = 0
    letters_guessed_wrong = []
    letters_in_wrong_place = []

    word_to_guess = generate_word()
    while turns_taken < max_turns:
        print(f'You have {max_turns - turns_taken} turns left to guess the word.')
        guess = input('Guess a 5 letter word: ').lower()

        if len(guess) != len(word_to_guess) or not guess.isalpha():
            print("Please enter a 5-letter word.")
            continue
        
        if guess == word_to_guess:
            print(f'Congratulations! You guessed the word: {word_to_guess}')
            return

        index = 0
        for i in guess:
            if i == word_to_guess[index]:
                print(f'{i} * ', end='')
            elif i in word_to_guess:
                print(f'{i} - ', end='')
                if i not in letters_in_wrong_place:
                    letters_in_wrong_place.append(i)
            else:
                print(f'{i} X ', end='')
                if i not in letters_guessed_wrong:
                    letters_guessed_wrong.append(i)
            index += 1
        print()  # Move to next line after feedback
        turns_taken += 1

    print('No more turns left!')
    print(f'The word was: {word_to_guess}')

if __name__ == '__main__':
    main()