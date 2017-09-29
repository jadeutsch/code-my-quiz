# opening message
name = raw_input(
    "Welcome to Hogwarts School of Witchcraft and Wizardry. What's your name? "
    )

# list of Harry Potter questions
quiz_questions = [
    "1. What is the name of the main character the books are named after? _1_ \n2. What is the name of the main dark wizard? _2_ \n3. What is the name of main character's male best friend? _3_ \n4. What is the name of the main character's female best friend? _4_",
    "1. What is the name of Harry's owl? _1_ \n2. What was the name of the Potions teacher that loved Harry's mother? _2_ \n3. What was the name of the Hogwarts headmaster that loved Harry like a grandson? _3_ \n4. What was the name of Harry's godfather? _4_",
    "1. What is the name of Voldemort's snake? _1_ \n2. What is the name of magical transportation where witches and wizards seem to appear and disappear? _2_ \n3. How many children do Harry and Ginny have? _3_ \n4.How many years later, from the Battle of Hogwarts, is the epilogue of Harry Potter and the Deathly Hallows set? _4_",
    "1. How long did the duel between Dumbledore and Grindelwald last? _1_ \n2. In the books, what does Ollivander make shoot out of Harry's wand before the First Task? _2_ \n3. What is the holiday James and Lily Potter were murdered on? _3_ \n4. What was the name off Severus Snape's mother?"
]

# list of Harry Potter answers
quiz_answers = [
    ["Harry Potter", "Voldemort", "Ron Weasley", "Hermione Granger"],
    ["Hedwig", "Severus Snape", "Albus Dumbledore", "Sirius Snape"],
    ["Nagini", "Apparition", "Three", "Nineteen"],
    ["Three hours", "Wine", "Halloween", "Eileen Prince"]
]


# function to return user's chosen level
def choose_level():
    return int(raw_input(
        "Choose your level of difficulty: \n1. Easy \n2. Medium \n3. Hard \n4. Insane \n"
        )
    )


# function to replace blanks in quiz
def replace_blanks(blank, answer, quiz):
    temp = "_" + str(blank + 1) + "_"
    next_quiz = quiz.replace(temp, key[blank])
    print next_quiz
    return next_quiz


def check_answer(blank, key, quiz, guesses):
    """
    Function takes user answer as input.
    Converts to uppercase to verify.
    Prints a statement based on user answer.
    Returns value.
    """
    answer = raw_input("\nWhat is your answer for _" + str(blank + 1) + "_? \n")
    answer = answer.upper()
    while answer in key[blank]:
        if answer == key[blank]:
            print "Correct! \n"
            return answer
        else:
            print "That's incorrect. You have " + str(guesses - 1) + " guesses left. \n"
            return False


# function to start quiz
def play_quiz(quiz, key):
    guesses = 5
    max_blank = 4
    blank = 0
    print quiz
    while guesses > 0 and blank < max_blank:
        flag = check_answer(blank, key, quiz, guesses)
        if flag:
            quiz = replace_blanks(blank, flag, quiz)
            blank = blank + 1
            if blank > 3:
                print "Congratulations! You've won! \n"
            else:
                guesses = guesses - 1
                if guesses < 1:
                    print "I'm sorry, but you lost. \n"


level = choose_level() - 1
quiz = quiz_questions[level]
key = quiz_answers[level]
play_quiz(quiz, key)
