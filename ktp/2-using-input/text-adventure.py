from text_actions import animated_text, animated_text_with_input, leave
import random


def thinking():
    animated_text("...", 0.3)
    print()


def new_line():
    print()
# start of text adventure


players_name = animated_text_with_input("what is your name? ")

animated_text("Hi, {0}".format(players_name))

new_line()

thinking()

activity = animated_text_with_input("What do you like to do for fun? ")

animated_text(
    "Wow, {0} that's really interesting... *actually yawning".format(activity))

new_line()

want_to_play_game = animated_text_with_input("Do you want to play a game? ")

if (want_to_play_game == 'yes'):
    animated_text('Great!')
else:
    animated_text('Fine!')
    leave()

new_line()

correct_guess = False
random_number = random.randint(1, 10)

print(random_number)


def test_guess(guesses: int):
    new_line()
    if (guesses == 0):
        players_guess = animated_text_with_input(
            "{0}, I'm thinking of a number between 1 and 10... guess what it is? ".format(players_name))
    elif (guesses > 3):
        players_guess = animated_text_with_input(
            "{0}, c'mon what it is? ".format(players_name))
    else:
        players_guess = animated_text_with_input(
            "what it is? ")

    if (int(players_guess) == random_number):
        animated_text("Great job!")
        return True
    else:
        animated_text("Wrong, try again...")
        return False


guesses = 0

while not correct_guess:
    correct_guess = test_guess(guesses)
    guesses += 1

new_line()

animated_text("Now for the next game...")
