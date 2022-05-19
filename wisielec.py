keyword = input('Podaj slowo: ')

print('_ '*len(keyword))

again = []
guessed = []
letters = []
letters[:0] = keyword

for i in letters:
    guessed.append('_ ')
    
print('Masz 10 prob')
guesses = 10

while guesses != 0:
    guess = input('Podaj literę: ')
    if guess in again:
        print('Już podales ta literke')
    else:
        again.append(guess)
        if guess in letters:
            for i in range(len(letters)):
                if letters[i] == guess:
                    guessed[i] = guess
                    print('Zgadłes literę')
        else:
            guesses -= 1
            if guesses == 0:
                print('Koniec gry jarek sie powiesił')
            else:
                print(f'Zła odpowiedź, zostały ci {guess} życia')
        print(''.join(guessed))
        if letters == guessed:
            print('Wygrałes')
            break