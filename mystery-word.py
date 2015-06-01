import random
import os


def find_word(path):
    level = input("Which level of judgement would you like to be subjected?\
     1/2/3: ")
    with open('/usr/share/dict/words') as words:
        word_list = words.read().split()
        word_choice = random.choice(word_list).lower()
        while True:
            if level == '1':
                if 4 <= len(word_choice) <= 6:
                    return word_choice
                else:
                    word_choice = random.choice(word_list).lower()
            elif level == '2':
                if 4 <= len(word_choice) <= 10:
                    return word_choice
                else:
                    word_choice = random.choice(word_list).lower()
            elif level == '3':
                if len(word_choice) > 10:
                    return word_choice
                else:
                    word_choice = random.choice(word_list).lower()
            else:
                print("You have 3 choices don't screw this up again!")
                return find_word(path)


print("Welcome to judgement town!")
random_word = find_word('/usr/share/dict/words')
print("Your salvation is {} letters long:".format(len(random_word)))
str_update = '_' * len(random_word)
list_update = list(str_update)
o_string = []
wrong_set = set({})
count = 8

while True:
    guess = (input("What letter do you guess? ")).lower()
    while len(guess) > 1 or not guess.isalpha():
        if not guess.isalpha():
            print("Do you speak english?")
        else:
            print('Did I ask you for more than one letter? Did I?')
        guess = (input("What LETTER do you guess? ")).lower()
    if guess in o_string or guess in wrong_set:
        count += 1
        print("Bro, you already gave me that guess...")
    for e, i in enumerate(random_word):
        if guess == i:
            list_update[e] = guess
            o_string.append(guess)
    if guess not in random_word:
        wrong_set.add(guess)
    n_string = ''.join(list_update)
    print(n_string)
    if n_string == str_update:
        count -= 1
        print('\nSuck what?\n')
    else:
        str_update = n_string
    if count > 0:
        print("Number of guess left: {}".format(count))
    else:
        print("""You have been hanged...
        \nP.S. No one will mourn you
        \nP.S.S. Your word was: {}""".format(random_word))
        break
    if n_string == random_word:
        print('You have earned your freedom!')
        break
    print("Here is a list of your failures: {}".format(' '.join(list(wrong_set))))

while True:
    masochist = input('Do you want to play again? y/n: ')
    if masochist == 'y':
        os.system('python3 mystery-word.py')
    else:
        break
