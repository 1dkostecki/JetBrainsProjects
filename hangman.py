import random


attempts_remaining = 8
allowed_letters = 'abcdefghijklmnopqrstuvwxyz'
word_list = ['python', 'java', 'kotlin', 'javascript']
user_guesses = []
random_word = word_list[random.randint(0, 3)]
hyphenated_secret_word = len(random_word) * "-"
hyphenated_secret_word_list = list(hyphenated_secret_word)
print("H A N G M A N")
while True:
    user_choice = input('Type "play" to play the game, "exit" to quit: ')
    if user_choice == 'play':
        pass
    elif user_choice == 'exit':
        break
    else:
        continue
    while attempts_remaining > 0:
        print()
        hyphenated_secret_word = "".join(hyphenated_secret_word_list)
        print(str(hyphenated_secret_word))
        if hyphenated_secret_word == random_word:
            print(f"You guessed the word {random_word}!")
            print("You survived!")
            break
        user_letter = input("Input a letter: ")
        user_guesses.append(user_letter)
        if len(user_letter) > 1 or user_letter == ' ':
            print("You should input a single letter")
        elif user_letter not in allowed_letters:
            print("It is not an ASCII lowercase letter")
        elif user_guesses.count(user_letter) > 1:
            print("You already typed this letter")
        elif user_letter not in random_word:
            print("No such letter in the word")
            attempts_remaining += -1
        elif user_letter in random_word:
            for i in range(len(random_word)):
                if random_word[i] == user_letter:
                    hyphenated_secret_word_list[i] = user_letter
                    hyphenated_secret_word = "".join(hyphenated_secret_word_list)
    if hyphenated_secret_word != random_word:
        print("You are hanged!")
