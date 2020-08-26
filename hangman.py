import random

def main():
    word = ['apple', 'pie', 'astronomy', 'duplex', 'scaffolding']
    word = random.choice(word)
    hidden_word = '_ ' * len(word)
    print(hidden_word)
    lives = 8
    used_chars = ''

    while lives > 0:
        print("Used chars: ", used_chars)
        guessed_letter = input("Enter letter: ")
        used_chars += guessed_letter + ' '

        new_hidden = ''
        loose_life = True
        for i, char in enumerate(word):
            if guessed_letter.lower() == char:
                new_hidden += char + ' '
                loose_life = False
            else:
                new_hidden += hidden_word[i*2] + " "

        hidden_word = new_hidden
        print(hidden_word)

        if loose_life:
            lives = lives - 1
            print("Oh no! You missed! Lifes left: ", lives)

        if '_' not in hidden_word:
            print("Win mofo! ")
            break

if __name__ == '__main__':
    main()
