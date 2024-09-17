import random
import string
import util

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = util.load_words()

def is_valid_guess(secret_word, letter):
    word_map = {}
    for l in secret_word:
        word_map[l] = (word_map.get(l) or 0) + 1

    for l in secret_word:
        if (not bool(word_map.get(letter))):
            return False
    return True


def is_word_guessed(secret_word, letters_guessed):
    word_map = {}
    for l in letters_guessed:
        word_map[l] = (word_map.get(l) or 0) + 1
    # print(word_map)
    for l in secret_word:
        if (not bool(word_map.get(l))):
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    result = []
    word_map = {}
    for l in letters_guessed:
        word_map[l] = (word_map.get(l) or 0) + 1

    for l in secret_word:
        if (not bool(word_map.get(l))):
            result.append("_ ")
        else:
            result.append(l)

    return "".join(result)

def get_available_letters(letters_guessed):
    result = []
    word_map = {}
    
    for l in letters_guessed:
        word_map[l] = (word_map.get(l) or 0) + 1

    alphabet = list(string.ascii_lowercase)
    
    for char in alphabet:
        if (not word_map.get(char)):
            result.append(char)
    return "".join(result)

def hangman(secret_word):
    num_of_guesses = 6
    num_of_warnings = 3
    guess_list = []
    vowels = 'aeiou'
    letter_count = {}
    
    for l in secret_word:
        letter_count[l] = (letter_count.get(l) or 0) + 1

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long')
    print('You have', num_of_warnings, 'warnings left')
    print('------------')

    while (num_of_guesses > 0):
        print("You have", num_of_guesses, "guesses left.")
        print("Available letters:", get_available_letters(guess_list))
        guess = input("Please guess a letter: ").lower()

        if (not guess.isalpha()):
            num_of_warnings -= 1
            print('That is not a valid letter. You have',
                  num_of_warnings, 'warnings left:',
                  get_guessed_word(secret_word, guess_list))
            if (num_of_warnings == 0):
                print('You have exhausted all warnings so you lose a guess')
                num_of_guesses -= 1
            continue

        if (guess in guess_list):
            if (num_of_warnings == 0):
                print(
                    'Oops! You\'ve already guessed that letter. You have no',
                    'warnings left so you lose one guess:', 
                    get_guessed_word(secret_word, guess_list))

                num_of_guesses -= 1
            else:
                num_of_warnings -= 1
                print('Oops! You\'ve already guessed that letter. You have',
                      num_of_warnings, 'warnings left:')
                print(get_guessed_word(secret_word, guess_list))

            continue

        guess_list.append(guess)

        is_valid = is_valid_guess(secret_word, guess)

        if (is_word_guessed(secret_word, guess_list)):
            break
          
        if (is_valid):
            print("Good guess:", get_guessed_word(secret_word, guess_list))
        else:
            print("Opps! That letter is not in my word:",
                  get_guessed_word(secret_word, guess_list))
            num_of_guesses -= 1
            if (guess in vowels):
                #print('vowel - lose another guess')
                num_of_guesses -= 1

        print('------------')

    if (is_word_guessed(secret_word, guess_list)):
        print('Congratulations, you won!')
        print('Total score is', num_of_guesses * len(letter_count))
    else:
        print('Sorry, you ran out of guesses. The word was', secret_word)

def match_with_gaps(my_word, other_word):
    my_word = ''.join(my_word.split())
    
    if(len(my_word) != len(other_word)):
        return False
    i = 0

    res = True
    while (i < len(my_word)):
        if (my_word[i] == other_word[i]):
            pass
        elif (my_word[i] == '_' and other_word[i] not in my_word):
            pass
        else:
            res = False
            break
        i += 1
            
    return res
  
def show_possible_matches(my_word):
    matches = []
    for word in wordlist:
        if (match_with_gaps(my_word, word)):
            matches.append(word)
            
    return ', '.join(matches) if bool(len(matches)) else 'No matches found'
  
def hangman_with_hints(secret_word):
    num_of_guesses = 6
    num_of_warnings = 3
    guess_list = []
    vowels = 'aeiou'
    letter_count = {}
    
    for l in secret_word:
        letter_count[l] = (letter_count.get(l) or 0) + 1
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long')
    print('You have', num_of_warnings, 'warnings left')
    print('------------')
    
    while (num_of_guesses > 0):
        print("You have", num_of_guesses, "guesses left.")
        print("Available letters:", get_available_letters(guess_list))
        guess = input("Please guess a letter: ").lower()

        if (guess == '*'):
            word = get_guessed_word(secret_word, guess_list)
            matches = (show_possible_matches(word))
            print(matches)
            continue
            
        if (not guess.isalpha()):
            num_of_warnings -= 1
            print('That is not a valid letter. You have',
                  num_of_warnings, 'warnings left:',
                  get_guessed_word(secret_word, guess_list))
            if (num_of_warnings == 0):
                print('You have exhausted all warnings so you lose a guess')
                num_of_guesses -= 1
            continue
    
        if (guess in guess_list):
            if (num_of_warnings == 0):
                print(
                    'Oops! You\'ve already guessed that letter. You have no',
                    'warnings left so you lose one guess:', 
                    get_guessed_word(secret_word, guess_list))
    
                num_of_guesses -= 1
            else:
                num_of_warnings -= 1
                print('Oops! You\'ve already guessed that letter. You have',
                      num_of_warnings, 'warnings left:')
                print(get_guessed_word(secret_word, guess_list))
    
            continue
    
        guess_list.append(guess)
    
        is_valid = is_valid_guess(secret_word, guess)
    
        if (is_word_guessed(secret_word, guess_list)):
            break
    
        if (is_valid):
            print("Good guess:", get_guessed_word(secret_word, guess_list))
        else:
            print("Opps! That letter is not in my word:",
                  get_guessed_word(secret_word, guess_list))
            num_of_guesses -= 1
            if (guess in vowels):
                #print('vowel - lose another guess')
                num_of_guesses -= 1
    
        print('------------')
    
    if (is_word_guessed(secret_word, guess_list)):
        print('Congratulations, you won!')
        print('Total score is', num_of_guesses * len(letter_count))
    else:
        print('Sorry, you ran out of guesses. The word was', secret_word)
        
#secret_word = choose_word(wordlist)
#hangman(secret_word)
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
