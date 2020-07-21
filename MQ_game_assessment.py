from functools import partial   # to prevent unwanted windows
from tkinter import *

import random


class Start:
    def __init__(self, partner):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(width=300, padx=10, pady=10)
        self.start_frame.grid()

        # Heading (label, row 0)
        self.math_text = Label(self.start_frame, text="Math's Quiz",
                               justify=CENTER, bg="#0197f6",
                               font="Arial 20 bold", wrap=225, pady=10, padx=10)
        self.math_text.grid(row=0, pady=10)

        # Initial Instructions (row 1)
        self.math_quiz_instructions = Label(self.start_frame, font="Arial 10 italic",
                                            text="Welcome to the Math's Quiz "
                                                 "Where you will test you knowledge "
                                                 "on general math's questions",
                                            wrap=275, justify=CENTER, padx=10, pady=10)
        self.math_quiz_instructions.grid(row=1)

        self.math_quiz_instructions_2 = Label(self.start_frame,
                                              text="press 'Start Quiz' to begin",
                                              font="arial 17 bold")
        self.math_quiz_instructions_2.grid(row=2, pady=10)

        # button to take you to the GUI to select difficulty
        '''
        self.start_quiz_button = Button(self.start_frame, font="arial 19 bold",
                                        text="Start Quiz",
                                        command=lambda: self.to_game,
                                        bg="#0197f6")
                                        '''
        self.start_quiz_button = Button(self.start_frame, font="arial 19 bold",
                                        text="Start Quiz",
                                        command=self.to_game,
                                        bg="#0197f6")
        self.start_quiz_button.grid(row=3)

    def to_game(self):
        Game(self)


class Game:
    def __init__(self, partner):

        partner.start_quiz_button.config(state=DISABLED)

        # GUI setup
        self.game_box = Toplevel()

        self.game_box.protocol('WM_DELETE_WINDOW', partial(self.close_game, partner))

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid(padx=10)

        self.questions_funds = IntVar()
        self.questions_funds.set(0)

        # Heading (label, row 0)
        self.game_text = Label(self.game_frame, text="Math's Quiz",
                               justify=CENTER, bg="#0197f6",
                               font="Arial 20 bold")
        self.game_text.grid(row=0)

        # Initial Instructions (row 1)
        self.math_quiz_game_instructions = Label(self.game_frame, font="Arial 10 italic",
                                                 text="Please select how many questions you are wanting "
                                                      "e.g. 10, 15 or 20 etc "
                                                      "and the difficulty of the Math's Quiz "
                                                      "press either 'easy', 'medium' or 'hard'. "
                                                      "To learn how to play the Math's Quiz, "
                                                      "press 'how to play' to read the instructions ",
                                                 justify=CENTER,
                                                 wrap=250, padx=15, pady=15)
        self.math_quiz_game_instructions.grid(row=1)

        self.entry_error_frame = Frame(self.game_frame, width=200)
        self.entry_error_frame.grid(row=2)

        self.questions_amount_entry = Entry(self.entry_error_frame,
                                            font="Arial 19 bold", width=10)
        self.questions_amount_entry.grid(row=0, column=0)

        self.add_questions_button = Button(self.entry_error_frame,
                                           font="Arial 14 bold",
                                           text="Number of questions ",
                                           command=self.check_questions)
        self.add_questions_button.grid(row=0, column=1)

        self.amount_error_label = Label(self.entry_error_frame)

        self.difficulty_frame = Frame(self.game_frame)
        self.difficulty_frame.grid(row=3)

        # difficulty buttons goes here...
        # Yellow for easy difficulty...
        self.easy_difficulty_button = Button(self.difficulty_frame, text="Easy ",
                                             command=self.to_question,
                                             font="Arial 15 bold", bg="yellow")
        self.easy_difficulty_button.grid(row=0, column=0, pady=10)

        # orange for medium difficulty
        self.medium_difficulty_button = Button(self.difficulty_frame, text="Medium ",
                                               command=self.to_question,
                                               font="Arial 15 bold", bg="orange")
        self.medium_difficulty_button.grid(row=0, column=1, pady=10)

        # red for hard difficulty
        self.hard_difficulty_button = Button(self.difficulty_frame, text="Hard ",
                                             command=self.to_question,
                                             font="Arial 15 bold", bg="red")
        self.hard_difficulty_button.grid(row=0, column=2, pady=10)

        self.help_button = Button(self.game_frame,
                                  text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#0197f6", fg="black",
                                  command=self.to_help)
        self.help_button.grid(row=4, pady=10)

        self.easy_difficulty_button.config(state=DISABLED)
        self.medium_difficulty_button.config(state=DISABLED)
        self.hard_difficulty_button.config(state=DISABLED)

    def close_game(self, partner):
        partner.start_quiz_button.config(state=NORMAL)
        self.game_box.destroy()

    def to_help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="To begin the quiz, choose how many questions "
                                          "you want in the quiz between 5 and 30, "
                                          "and then choose a difficulty "
                                          "ranging from 'Easy', 'Medium' or 'Hard'. "
                                          "This will determine how difficult "
                                          "the questions will be. "
                                          "e.g. 'Easy': Question 1: What is 4 x 5 or "
                                          "what is 17 + 21, "
                                          "'Medium': Question 1: What is 95 - 32 or "
                                          "what is 5 x 14, "
                                          "'Hard': Question 1: What is 532 - 267 or "
                                          "what is 450 / 90",
                                     justify=CENTER)

    def check_questions(self):
        starting_questions = self.questions_amount_entry.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        self.questions_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        self.easy_difficulty_button.config(state=DISABLED)
        self.medium_difficulty_button.config(state=DISABLED)
        self.hard_difficulty_button.config(state=DISABLED)

        try:
            starting_questions = int(starting_questions)

            if starting_questions < 5:
                has_errors = "yes"
                error_feedback = "please pick more questions " \
                                 "so that the quiz is not short and boring"
            elif starting_questions > 30:
                has_errors = "yes"
                error_feedback = "Please pick less questions " \
                                 "so that the quiz is not long and tiring"

            elif starting_questions >= 5:
                self.easy_difficulty_button.config(state=NORMAL)
                self.medium_difficulty_button.config(state=NORMAL)
                self.hard_difficulty_button.config(state=NORMAL)

            elif starting_questions <= 30:
                self.easy_difficulty_button.config(state=NORMAL)
                self.medium_difficulty_button.config(state=NORMAL)
                self.hard_difficulty_button.config(state=NORMAL)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a question amount between 5 and 30 (no text / decimals)"

        if has_errors == "yes":
            self.questions_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)
        else:
            # set starting questions to amount entered by user
            self.questions_funds.set(starting_questions)

    def to_question(self):

        # retrieve starting questions
        starting_questions = self.questions_funds.get()

        question(self, starting_questions)


class question:
    def __init__(self, partner, starting_questions):

        partner.easy_difficulty_button.config(state=DISABLED)
        partner.medium_difficulty_button.config(state=DISABLED)
        partner.hard_difficulty_button.config(state=DISABLED)
        partner.add_questions_button.config(state=DISABLED)

        self.balance = IntVar()

        self.balance.set(starting_questions)

        self.questions_stats_list = [starting_questions, starting_questions]

        round_stats_list = []

        # GUI setup
        self.question_box = Toplevel()

        self.question_box.protocol('WM_DELETE_WINDOW', partial(self.close_questions, partner))

        # level = input(self.question_text).lower()

        operation_list = ["+", "*", "-"]
        operation = random.choice(operation_list)

        level = ["easy", "medium", "hard"]

        if level == "easy":
            if operation == "+" or operation == "-":
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)

            else:
                num1 = random.randint(1, 12)
                num2 = random.randint(1, 12)

        else:
            if operation == "+" or operation == "-":
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)

            else:
                factor = [10, 100, 1000]
                num1 = random.randint(1, 10) * random.choice(factor)
                num2 = random.randint(1, 10) * random.choice(factor)

        question = "{} {} {}".format(num2, operation, num1)

        if level == "medium":
            if operation == "+" or operation == "-":
                num1_1 = random.randint(25, 100)
                num2_1 = random.randint(25, 100)

            else:
                num1_1 = random.randint(1, 12)
                num2_1 = random.randint(1, 12)

        else:
            if operation == "+" or operation == "-":
                num1_1 = random.randint(25, 100)
                num2_1 = random.randint(25, 100)

            else:
                factor = [10, 100, 1000]
                num1_1 = random.randint(5, 12) * random.choice(factor)
                num2_1 = random.randint(5, 12) * random.choice(factor)

        question_1 = "{} {} {}".format(num2_1, operation, num1_1)

        if level == "hard":
            if operation == "+" or operation == "-":
                num1_2 = random.randint(100, 300)
                num2_2 = random.randint(100, 300)

            else:
                num1_2 = random.randint(1, 12)
                num2_2 = random.randint(1, 12)

        else:
            if operation == "+" or operation == "-":
                num1_2 = random.randint(100, 300)
                num2_2 = random.randint(100, 300)

            else:
                factor = [10, 100, 1000]
                num1_2 = random.randint(10, 20) * random.choice(factor)
                num2_2 = random.randint(10, 20) * random.choice(factor)

        question_2 = "{} {} {}".format(num2_2, operation, num1_2)

        self.question_frame = Frame(self.question_box)
        self.question_frame.grid()

        # Heading (label, row 0)
        self.question_text = Label(self.question_frame,
                                   justify=CENTER, bg="#0197f6",
                                   font="Arial 20 bold", text=question,
                                   wrap=225, padx=10)
        self.question_text.grid(row=0, pady=10)

        # Initial Instructions (row 1)
        self.mystery_instructions = Label(self.question_frame, font="Arial 10 italic",
                                          text="Please enter a answer to see if "
                                               "you are correct or incorrect",
                                          wrap=275, justify=CENTER, padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        self.answer_frame = Frame(self.question_frame)
        self.answer_frame.grid(row=2)

        self.questions_box_entry = Entry(self.answer_frame, font="Arial 15 bold",
                                         width=10)
        self.questions_box_entry.grid(row=0, pady=10)

        self.submit_question_button = Button(self.answer_frame, font="Arial 15 bold",
                                             text="Submit")
        self.submit_question_button.grid(row=0, column=1)

        self.next_question_button = Button(self.question_frame, font="Arial 15 bold",
                                           text="Next Question",
                                           width=15)
        self.next_question_button.grid(row=3, pady=10)

        self.stats_button = Button(self.question_frame, text="Game stats...",
                                   font="arial 15 bold",
                                   bg="#0197f6", fg="black",
                                   command=lambda: self.to_stats(round_stats_list, questions_stats_list))
        self.stats_button.grid(row=4)

        self.quit_questions_button = Button(self.question_frame, text="Quit", fg="black",
                                            bg="#0197f6", font="Arial 15 bold", width=20,
                                            command=partial(self.close_questions, partner))
        self.quit_questions_button.grid(row=5, pady=10)

    def close_questions(self, partner):
        partner.easy_difficulty_button.config(state=NORMAL)
        partner.medium_difficulty_button.config(state=NORMAL)
        partner.hard_difficulty_button.config(state=NORMAL)
        partner.add_questions_button.config(state=NORMAL)
        self.question_box.destroy()

    def to_stats(self, questions_history, questions_stats):
        Stats(self, questions_history, questions_stats)


class Stats:
    def __init__(self, partner, questions_history, questions_stats):

        partner.stats_button.config(state=DISABLED)

        self.all_stats_list = []

        heading = "Arial 12 bold"
        content = "Arial 12"

        self.stats_box = Toplevel()

        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        self.stats_heading_label = Label(self.stats_frame, text="Stats / Export",
                                         font="arial 19 bold", justify=CENTER,
                                         bg="#0197f6")
        self.stats_heading_label.grid(row=0)

        self.export_instructions = Label(self.stats_frame,
                                         text="Welcome to Stats / Export "
                                         "Please press the 'Export' button to "
                                         "gain access to your quiz results "
                                         "and to save those results.", wrap=250,
                                         font="arial 10 italic",
                                         justify=CENTER,)
        self.export_instructions.grid(row=1)

        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        self.start_questions_label = Label(self.details_frame,
                                           text="Number of questions:", font=heading,
                                           anchor="e")
        self.start_questions_label.grid(row=0, column=0, padx=0)

        self.start_questions_value_label = Label(self.details_frame, font=content,
                                                 text="{}".format(questions_stats[0]),
                                                 anchor="w")
        self.start_questions_value_label.grid(row=0, column=1, padx=0)

        self.chosen_difficulty_label = Label(self.details_frame,
                                             text="chosen difficulty:", font=heading,
                                             anchor="e")
        self.chosen_difficulty_label.grid(row=1, column=0, padx=0)

        self.chosen_difficulty_value_label = Label(self.details_frame, font=content,
                                                   text=len(questions_history),
                                                   anchor="w")
        self.chosen_difficulty_value_label.grid(row=1, column=1, padx=0)

        self.dismiss_button = Button(self.details_frame, text="Dismiss",
                                     width=10, bg="#660000",
                                     font="arial 15 bold",
                                     padx=10, pady=10,
                                     command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=3, pady=10)

        self.export_button = Button(self.details_frame, text="export",
                                    font="Arial 12 bold",
                                    bg="#0197f6",
                                    padx=40, pady=5,
                                    command=lambda: self.export(questions_history, partner))
        self.export_button.grid(row=2)

    def close_stats(self, partner):
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def export(self, questions_history, partner):
        Export(self, questions_history, partner)


class Export:
    def __init__(self, partner, questions_history, all_questions_stats):

        partner.export_button.config(state=DISABLED)

        self.export_box = Toplevel()

        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        self.question_text = Label(self.export_frame, text="Export",
                                   justify=CENTER, bg="#0197f6",
                                   font="Arial 20 bold", wrap=225, pady=10, padx=10)
        self.question_text.grid(row=0, pady=10)

        self.how_heading = Label(self.export_frame, text="Quiz Stats",
                                 font="arial 14 bold")
        self.how_heading.grid(row=1)

        self.export_text = Label(self.export_frame, text="Save your stats by entering "
                                                         "an acceptable filename "
                                                         "and press 'save' to save your stats",
                                 justify=CENTER, font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        self.save_error_label = Label(self.export_frame, text="", fg="red")
        self.save_error_label.grid(row=5)

        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="Arial 15 bold", bg="#0197f6",
                                  command=partial(lambda: self.save_history(partner, questions_history,
                                                                            all_questions_stats)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 15 bold", bg="#0197f6",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, questions_history, all_questions_stats):

        valid_char = "[A-Za-z0-9_]"
        has_errors = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no space allowed)"

            else:
                problem = ("(no {}'s allowed".format(letter))
            has_errors = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_errors = "yes"

        if has_errors == "yes":
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            self.filename_entry.config(bg="#0197f6")

        else:
            filename = filename + ".txt"

            f = open(filename, "w+")

            f.write("Game Statistics\n\n")

            for item in questions_history:
                f.write(item + "\n")

            f.write("Round Details\n\n")

            for item in questions_history:
                f.write(item + "\n")

            f.close()

            self.close_export(partner)

    def close_export(self, partner):
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


class Help:
    def __init__(self, partner):
        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_button = Button(self.help_frame, text="Dismiss",
                                     width=10, bg="#660000", fg="white",
                                     font="arial 15 bold",
                                     padx=10, pady=10,
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math's quiz")
    something = Start(root)
    root.mainloop()
