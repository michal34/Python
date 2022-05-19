keyword = input('podaj swoje slowo: ')

print('_ '*len(keyword))

again = []
guessed = []
letters = []
letters[:0]= keyword

for i in letters:
    guessed.append('_ ')

print('masz 10 zgadnięć!')
guesses = 10

while guesses != 0:
    guess = input('podaj litere: ')
    if guess in again:
        print('juz podales ta literke')
    else:
        again.append(guess)
        if guess in letters:
            for i in range(len(letters)):
                if letters[i] == guess:
                    guessed[i] = guess
                    print('brawo zgadles literke')
        else:
            guesses = guesses - 1
            if guesses == 0:
                print('ups umarles')
            else:
                print(f'ups, zla odpowiedz, zostaly ci {guesses} zycia')
        print(''.join(guessed))
        if letters == guessed:
            print('brawo wygrales')
            break