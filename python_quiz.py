# list containing the quiz of different difficulties
quiz = [
    "What is the name of the main character the books are named for? __1__. \nWhat is the name of the main dark wizard? __2__ \nWhat is the name of the main character's male best friend? __3__ \nWhat is the name of the main character's female best friend? __4__",
    "What is the name of Harry's owl? __1__ \nWhat was the name of the Potions teacher that despises Harry? __2__ \nWhat was the name of the Hogwarts headmaster who loved Harry like a grandson? __3__ \nWhat was the name of Harry's godfather? __4__",
    "What was the name of Voldemort's snake? __1__ \nWhat is the name of magical transportation where witches and wizards seem to appear and disappear? __2__ \nHow many children do Harry and Ginny have? __3__ \nHow many years later, from the Battle of Hogwarts, is the epilogue in Harry Potter and the Deathly Hallows? __4__",
    "How long did the duel between Dumbledore and Grindelwald last? __1__ \nIn the books, what does Ollivander make shoot out of Harry's wand before the First Task? __2__ \nWhat is the holiday James and Lily Potter were murdered on? __3__ \nWhat was the name of Severus Snape's mother? __4__"
]


# list containing the answers to the blanks
key = [
    ["Harry Potter", "Voldemort", "Ron Weasley", "Hermione Granger"],
    ["Hedwig", "Severus Snape", "Albus Dumbledore", "Sirius Black"],
    ["Nagini", "Apparition", "Three", "Nineteen"],
    ["Three hours", "Wine", "Halloween", "Eileen Prince"]
]


# function returning the chosen difficulty
def choose_level():
    return int(raw_input(
        "Now choose your level:\n1. Easy\n2. Medium\n3. Hard\n4. Insane\n")
    )


# function replacing the blanks in the quiz
def replace_blanks(blank, answer, current_quiz):
    temp = "__" + str(blank + 1) + "__"
    new_quiz = current_quiz.replace(temp, current_key[blank])
    print new_quiz
    return new_quiz


def answer_check(blank, current_key, current_quiz, guesses):
    """
    Function takes user input.
    Converts to string.
    Prints statement.
    Returns value.
    """
    answer = raw_input("What do you think will come in place of __" + str(blank + 1) + "__\n")
    if answer == current_key[blank]:
        print "Correct!\n"
        return answer
    else:
        print "Incorrect. You have " + str(guesses - 1) + " guesses left.\n"
        return False


# function starting the quiz. Calling the answer_check function and the main logic behind the quiz
def play_quiz(current_quiz, current_key):
    guesses = 5
    max_blank = 4
    blank = 0
    print current_quiz
    while guesses > 0 and blank < max_blank:
        flag = answer_check(blank, current_key, current_quiz, guesses)
        if flag:
            current_quiz = replace_blanks(blank, flag, current_quiz)
            blank = blank + 1
            if blank > 3:
                print "Congratulations! You won.\n"
        else:
            guesses = guesses - 1
            if guesses < 1:
                print "Sorry! You lost.\n"


print "Welcome to Hogwarts School of Witchcraft and Wizardry."
print "You'll be given 5 guesses to complete your exam."
print "Lose them and you lose the game. Get all correct to win.\n"

difficulty = choose_level() - 1
current_quiz = quiz[difficulty]
current_key = key[difficulty]
play_quiz(current_quiz, current_key)
