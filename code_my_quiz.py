name = raw_input("Hello, what's your name? ")
blanks = ["_1_", "_2_", "_3_", "_4_"]
#list of Harry Potter questions
easy_quiz = "1. What is the name of the main character the books are named for? _1_ \n2. What is the name of the dark wizard Harry fights? _2_ \n3. What is the name of Harry's male best friend? _3_ \n4. What is the name of Harry's female best friend? _4_"
medium_quiz = "1. What is the name of Harry's owl? _1_ \n2. What is the name of the Potions teacher that despises Harry? _2_ \n3. What was the name of the Hogwarts headmaster who loved Harry like a grandson? _3_ \n4. What is the name of Harry's godfather? _4_"
hard_quiz = "1. What is the name of Voldemort's snake? _1_ \n2. What is the name of magical transportation where witches and wizards seem to appear and disappear? _2_ \n3. How many children do Harry and Ginny have? _3_ \n4. How many years later, from the Battle of Hogwarts, is the epilogue in Harry Potter and the Deathly Hallows? _4_"
insane_quiz = "1. How long did the duel between Dumbledore and Grindelwald last? _1_ \n2. In the books, what does Ollivander make shoot out of Harry's wand before the First Task? _2_ \n3. What is the holiday James and Lily Potter were murdered on? _3_ \n4. What was the name of Severus Snape's mother? _4_"
#answers to questions
easy_answers = ["Harry Potter", "Voldemort", "Ron Weasley", "Hermione Granger"]
medium_answers = ["Hedwig", "Severus Snape", "Albus Dumbledore", "Sirius Snape"]
hard_answers = ["Nagini", "Apparition", "Three", "Nineteen"]
insane_answers = ["Three hours", "Wine", "Halloween", "Eileen Prince"]
#select type of Harry Potter questions
quiz_data = {
   'easy': {
        'quiz': easy_quiz,
        'answers': easy_answers,
        'message': "This will be easy."
    },
   'medium': {
          'quiz': medium_quiz,
          'answers': medium_answers,
          'message': "Just slightly harder than easy."
    },
   'hard': {
        'quiz': hard_quiz,
        'answers': hard_answers,
        'message': "This will be a challenge."
    },
   'insane': {
          'quiz': insane_quiz,
          'answers': insane_answers,
          'message': "You're insane."
    }
}
def choose_level():
    level = raw_input("Choose your level of difficulty: easy, medium, hard, or insane. ")
    while level not in ["easy","medium","hard","insane"]:
        level = raw_input("Please choose: easy, medium, hard, or insane. ")

    print quiz_data[level]['message']
    if level == "easy":
        return easy_quiz, easy_answers
    elif level == "medium":
        return medium_quiz, medium_answers
    elif level == "hard":
        return hard_quiz, hard_answers
    elif level == "insane":
        return insane_quiz, insane_answers

def check_answer(user_answer, quiz_list, quiz_index):
    if user_answer == quiz_list[quiz_index]:
        return "Correct!"
        return "Incorrect."
        pass

def you_lost():
    print "I'm sorry, but you lost."
    return

def you_win():
    print "Congratulations! You've won!"

def play_quiz():
    quiz,quiz_list = choose_level()
    print quiz
    quiz_index = 0
    guesses = 5
    while quiz_index < len(blanks):
        user_answer = raw_input("What's your answer to question " + blanks[quiz_index] + "?: ")
        if check_answer(user_answer, quiz_list, quiz_index) == "correct_answer":
            print "\nThat's correct! Good job!\n"
            quiz = quiz.replace(blanks[quiz_index], user_answer.upper())
            quiz_index += 1
            guesses = 5
            print quiz
            if quiz_index == len(blanks):
              return you_win()
        else:
            guesses -= 1
            if guesses == 0:
              return you_lost()
            print "That's incorrect. You have " + str (guesses) + " guesses left."

play_quiz()
