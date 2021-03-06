from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Quiz:
    def __init__(self):

        # Formatting variables...
        font_color = "black"

        # quiz GUI
        self.quiz_frame = Frame()
        self.quiz_frame.grid(padx=10)

        self.starting_question = IntVar()
        self.starting_question.set(0)

        self.low_amount = IntVar()
        self.low_amount.set(0)

        self.high_amount = IntVar()
        self.high_amount.set(0)

        self.heading_frame = Frame(self.quiz_frame)
        self.heading_frame.grid(row=0)

        # Quiz (row 0)
        self.Quiz_label = Label(self.heading_frame, text="Math Quiz",
                                font="arial 20 bold", fg=font_color,
                                bg="#0197f6")
        self.Quiz_label.grid(row=0)

        # Initial Instructions (row 1)
        self.math_quiz_game_instructions = Label(self.heading_frame, font="Arial 10 italic",
                                                 text="Please select the amount of questions you are wanting, "
                                                      "e.g. 10, 15 or 20, select your low and higher number "
                                                      "and select Addition to play a Addition quiz, "
                                                      "Subtraction for a subtraction quiz "
                                                      "and Multiplication for a multiplication quiz. "
                                                      "If you need help on how to play the quiz "
                                                      "please press help / rules. ",
                                                 justify=CENTER,
                                                 wrap=250, padx=15, pady=15)
        self.math_quiz_game_instructions.grid(row=1)

        # Quiz (row 1)
        self.choice_frame = Frame(self.quiz_frame, width=200)
        self.choice_frame.grid(row=1)

        # label for error feedback
        self.amount_error_label = Label(self.choice_frame, font="arial 10 bold",
                                        text="", fg="red")
        self.amount_error_label.grid(row=0)

        # Number of questions label and entry
        self.cho_num_label = Label(self.choice_frame, text="Number of Questions",
                                   font="arial 12 bold",
                                   fg=font_color)
        self.cho_num_label.grid(row=1)

        self.cho_num_entry = Entry(self.choice_frame,
                                   font="arial 15 bold", width=10)
        self.cho_num_entry.grid(row=1, column=1)

        # Low number label and entry
        self.low_num_label = Label(self.choice_frame, text="Low number amount",
                                   font="arial 12 bold",
                                   fg=font_color)
        self.low_num_label.grid(row=2)

        self.low_num_entry = Entry(self.choice_frame,
                                   font="arial 15 bold", width=10)
        self.low_num_entry.grid(row=2, column=1)

        # High number label and entry
        self.high_num_label = Label(self.choice_frame, text="High number amount",
                                    font="arial 12 bold",
                                    fg=font_color)
        self.high_num_label.grid(row=3)

        self.high_num_entry = Entry(self.choice_frame,
                                    font="arial 15 bold", width=10)
        self.high_num_entry.grid(row=3, column=1)

        # Frame for entry button (row 4)
        self.enter_frame = Frame(self.quiz_frame)
        self.enter_frame.grid(row=4)

        self.question_amount_btn = Button(self.enter_frame, text="Enter",
                                          font="arial 14 bold", command=self.check_question)
        self.question_amount_btn.grid(row=0, pady=10, padx=10)

        # Frame for Multiplication, subtraction and addition button (row 5)
        self.cho_btn__frame = Frame(self.quiz_frame)
        self.cho_btn__frame.grid(row=5)

        # Addition button
        self.addition_btn = Button(self.cho_btn__frame, text="Addition", font="arial 17 bold", fg=font_color,
                                   bg="yellow", command=lambda: self.to_game(1))
        self.addition_btn.grid(row=1, column=0, pady=10)

        # Subtraction button
        self.subtraction_btn = Button(self.cho_btn__frame,
                                      text="Subtraction", font="arial 17 bold", fg=font_color,
                                      bg="orange", command=lambda: self.to_game(2))
        self.subtraction_btn.grid(row=1, column=1, pady=10)

        # Multiplication button
        self.multiplication_btn = Button(self.cho_btn__frame,
                                         text="Multiplication", font="arial 17 bold", fg=font_color,
                                         bg="red", command=lambda: self.to_game(3))
        self.multiplication_btn.grid(row=1, column=2, pady=10)

        # Frame for help button (row 6)
        self.help_frame = Frame(self.quiz_frame)
        self.help_frame.grid(row=6)

        self.addition_btn.config(state=DISABLED)
        self.subtraction_btn.config(state=DISABLED)
        self.multiplication_btn.config(state=DISABLED)

        # Help Button
        self.help_button = Button(self.help_frame,
                                  text="Help / Rules", font="arial 14 bold", fg="black",
                                  bg="#0197f6", command=self.help)
        self.help_button.grid(row=0, pady=10)

        # function to take me to help class
    def help(self):
        get_help = Help(self)
        get_help.help_text.configure()

        # function to get question amount, low amount and high amount
        # and have error feedback for any errors that occur
    def check_question(self):
        starting_question = self.cho_num_entry.get()
        low_amount = self.low_num_entry.get()
        high_amount = self.high_num_entry.get()

        # Set error background colour (and assume that there are no
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        # change background to white
        self.cho_num_entry.config(bg="white")
        self.amount_error_label.config(text="")
        self.low_num_entry.config(bg="white")
        self.low_num_entry.config(text="")
        self.high_num_entry.config(bg="white")
        self.high_num_entry.config(text="")

        # disables addition, subtraction and musltiplication button so that
        # the user doesn't enter the game without low and high number and number of questions
        self.addition_btn.config(state=DISABLED)
        self.subtraction_btn.config(state=DISABLED)
        self.multiplication_btn.config(state=DISABLED)

        try:
            starting_question = int(starting_question)

            # checks if number of questions is either below 5 or above 30
            if starting_question < 5:
                has_error = "yes"
                error_feedback = "Sorry, you need more than 5 questions"
                self.cho_num_entry.config(bg=error_back)
            elif starting_question > 30:
                has_error = "yes"
                error_feedback = "sorry you need less than 30 questions"
                self.cho_num_entry.config(bg=error_back)

        except ValueError:
            has_error = "yes"
            error_feedback = "Please enter a question amount between 5 and 30 (no text / decimals)"
            self.cho_num_entry.config(bg=error_back)

        try:
            low_amount = int(low_amount)

            # checks if low amount is below -100 or above 1000
            if low_amount < -100:
                has_error = "yes"
                error_feedback = "the low number is higher than -100"
                self.low_num_entry.config(bg=error_back)
            elif low_amount > 1000:
                has_error = "yes"
                error_feedback = "the low number is higher than 1,000"
                self.low_num_entry.config(bg=error_back)

        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes with whole numbers"
            self.low_num_entry.config(bg=error_back)

        if has_error == "yes":
            self.amount_error_label.config(text=error_feedback)

        try:
            high_amount = int(high_amount)

            # checks if high amount is lower than low amount or if high amount is above 10000
            if high_amount <= low_amount:
                has_error = "yes"
                error_feedback = "the high number needs to be higher than the low number"
                self.high_num_entry.config(bg=error_back)
            elif high_amount >= 10000:
                has_error = "yes"
                error_feedback = "the high number needs to be lower than 10,000"
                self.high_num_entry.config(bg=error_back)

        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes with whole numbers"
            self.high_num_entry.config(bg=error_back)

        if has_error == "yes":
            self.amount_error_label.config(text=error_feedback)

        else:
            self.starting_question.set(starting_question)
            self.low_amount.set(low_amount)
            self.high_amount.set(high_amount)
            self.addition_btn.config(state=NORMAL)
            self.subtraction_btn.config(state=NORMAL)
            self.multiplication_btn.config(state=NORMAL)
            self.cho_num_entry.config(state=DISABLED)
            self.low_num_entry.config(state=DISABLED)
            self.high_num_entry.config(state=DISABLED)

        # function to take me to the game
    def to_game(self, op):
        starting_question = self.cho_num_entry.get()
        low_amount = self.low_num_entry.get()
        high_amount = self.high_num_entry.get()

        Game(self, op, starting_question, low_amount, high_amount)


class Game:
    def __init__(self, partner, op, starting_question, low_amount, high_amount):

        starting_question = int(starting_question)
        questions_played = int(1)
        how_many_right = int(0)

        self.correct = IntVar()
        self.correct.set(0)

        low_amount = int(low_amount)
        high_amount = int(high_amount)
        self.history_questions = []

        op = int(op)

            # if addition is chosen, then prints addition question
        if op == 1:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} + {}".format(hi_lo_num, hi_lo_num2)
            var_correct = hi_lo_num + hi_lo_num2
            self.correct.set(var_correct)
            op_text = "Addition"
            # if subtraction is chosen, then prints subtraction question
        elif op == 2:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} - {}".format(hi_lo_num, hi_lo_num2)
            var_correct = hi_lo_num - hi_lo_num2
            self.correct.set(var_correct)
            op_text = "Subtraction"
            # if multiplication is chosen, then prints multiplication question
        elif op == 3:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} x {}".format(hi_lo_num, hi_lo_num2)
            var_correct = hi_lo_num * hi_lo_num2
            self.correct.set(var_correct)
            op_text = "Multiplication"

        self.history_questions.append(questions)

        # disable buttons
        partner.cho_num_entry.config(state=DISABLED)
        partner.low_num_entry.config(state=DISABLED)
        partner.high_num_entry.config(state=DISABLED)
        partner.addition_btn.config(state=DISABLED)
        partner.subtraction_btn.config(state=DISABLED)
        partner.multiplication_btn.config(state=DISABLED)
        partner.question_amount_btn.config(state=DISABLED)
        partner.help_button.config(state=DISABLED)

        # Set up Geo game one
        self.addition_box = Toplevel()

        # If users press at top, closes help and 'releases' help button
        self.addition_box.protocol('WM_DELETE_WINDOW', partial(self.close_addition, partner))

        # Set up GUI Frame
        self.addition_frame = Frame(self.addition_box, width=300)
        self.addition_frame.grid()

        # Set up Geo Instruction heading (row 0)
        self.heading = Label(self.addition_frame, text=op_text,
                             font="arial 20 bold")
        self.heading.grid(row=0)

        # Geo text (label, row 1)
        self.game = Label(self.addition_frame,
                          text="Fill the boxes",
                          justify=LEFT, width=50, wrap=200)
        self.game.grid(row=1)

        # frame for next button, check answer button and statements printed based on
        # if the answer is wrong or not
        self.ask_questions_frame = Frame(self.addition_frame)
        self.ask_questions_frame.grid(row=1)

        self.get1_label = Label(self.ask_questions_frame,
                                text=questions,
                                font="arial 10 bold", fg="black")
        self.get1_label.grid(row=1)

        # entry to ask either addition, subtraction or multiplication questions
        self.checking_ans_btn = Entry(self.ask_questions_frame, font="arial 15 bold")
        self.checking_ans_btn.grid(row=2)

        # button to check if the answer is correct or incorrect
        self.check_ans_btn = Button(self.ask_questions_frame, text="Check Answer", font="arial 10 bold", fg="black",
                                    bg="#0197f6", pady=7,
                                    command=lambda: self.check_ans(low_amount, high_amount, op, starting_question,
                                                                   questions_played, how_many_right,
                                                                   self.history_questions))
        self.check_ans_btn.grid(row=2, column=1)

        # frame for dismiss button (row 3)
        self.dismiss_export_frame = Frame(self.addition_frame)
        self.dismiss_export_frame.grid(row=3)

        # Dismiss button
        self.dismiss_btn = Button(self.dismiss_export_frame, text="Dismiss", width=10, bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_addition, partner))
        self.dismiss_btn.grid(row=1, pady=10)

        # function to check if the answer is correct or incorrect
    def check_ans(self, low_amount, high_amount, op, starting_question, questions_played, how_many_right,
                  history_questions):
        answer = self.checking_ans_btn.get()
        self.checking_ans_btn.config(state=DISABLED)

        var_correct = self.correct.get()

        # change background to white (for testing purposes) ...
        self.check_ans_btn.config(bg="white")
        self.check_ans_btn.config(text="")

        try:
            answer = int(answer)
            correct = int(var_correct)
            self.history_questions.append(answer)

            # label for the question if the user gets the question wrong
            if answer != correct:
                self.feedback_label = Label(self.ask_questions_frame, text=" sorry, wrong answer ",
                                            font="arial 10 bold", fg="black", width=25)
                self.feedback_label.grid(row=3)
            elif answer == correct:

                # label for the question if the user gets the question right
                self.feedback_label = Label(self.ask_questions_frame, text=" That's the right answer",
                                            font="arial 10 bold", fg="black", width=25)
                self.feedback_label.grid(row=3)
                how_many_right += 1

            # label for the question if the user doesn't input a question
        except ValueError:
            self.feedback_label = Label(self.ask_questions_frame, text="Wrong answer: no answer given",
                                        font="arial 10 bold", fg="black", width=25)
            self.feedback_label.grid(row=3)

           # game over label
        if starting_question <= questions_played:
            self.game_over_label = Label(self.ask_questions_frame, text="Game Over", font="arial 10 bold", fg="black",
                                         bg="red", pady=10, padx=10)
            self.game_over_label.grid(row=2, column=1)

            # frame for export button
            self.export_frame = Frame(self.addition_frame)
            self.export_frame.grid(row=2)

            self.export_btn = Button(self.export_frame, text="Export", font="arial 10 bold", fg="black",
                                     bg="#0197f6", width=8,
                                     command=lambda: self.export(low_amount, high_amount, questions_played,
                                                                 how_many_right, history_questions))
            self.export_btn.grid(row=1, column=1)

            self.next_btn.config(state=DISABLED)
        else:
            self.check_ans_btn.config(text="")

            # next button to take the user to the next question
            self.next_btn = Button(self.ask_questions_frame, text="Next", font="arial 10 bold", fg="black",
                                   bg="#0197f6", pady=7,
                                   command=lambda: self.next(low_amount, high_amount, op, starting_question,
                                                                  questions_played, how_many_right, history_questions))
            self.next_btn.grid(row=2, column=1)

        # label to say how many questions the user played
        self.played_label = Label(self.ask_questions_frame, font="arial 10 bold",
                                  fg="black", pady=7,
                                  text="You have played {}/{}".format(questions_played, starting_question))
        self.played_label.grid(row=4)

        # function to print a new question
    def next(self, low_amount, high_amount, op, starting_question, questions_played, how_many_right, history_questions):
        starting_question = int(starting_question)
        self.checking_ans_btn.config(state=NORMAL)
        self.checking_ans_btn.delete(0, 'end')

        if op == 1:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} + {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            var_correct = hi_lo_num + hi_lo_num2
            self.correct.set(var_correct)
            questions_played += 1
        elif op == 2:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} - {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            var_correct = hi_lo_num - hi_lo_num2
            self.correct.set(var_correct)
            questions_played += 1
        elif op == 3:
            hi_lo_num = random.randrange(low_amount, high_amount)
            hi_lo_num2 = random.randrange(low_amount, high_amount)
            questions = "{} x {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            var_correct = hi_lo_num * hi_lo_num2
            self.correct.set(var_correct)
            questions_played += 1

        self.history_questions.append(questions)

        # button to check if the answer is correct or incorrect
        self.check_ans_btn = Button(self.ask_questions_frame, text="Check Answer", font="arial 10 bold", fg="black",
                                    bg="#0197f6", pady=7,
                                    command=lambda: self.check_ans(low_amount, high_amount, op,
                                                                   starting_question, questions_played, how_many_right,
                                                                   history_questions))
        self.check_ans_btn.grid(row=2, column=1)

    def close_addition(self, partner):
        # Put buttons back to normal
        partner.cho_num_entry.config(state=NORMAL)
        partner.low_num_entry.config(state=NORMAL)
        partner.high_num_entry.config(state=NORMAL)
        partner.help_button.config(state=NORMAL)
        partner.question_amount_btn.config(state=NORMAL)
        self.addition_box.destroy()

    def export(self, low_amount, high_amount, questions_played, how_many_right, history_questions):
        Export(self, low_amount, high_amount, questions_played, how_many_right, history_questions)


class Help:
    def __init__(self, partner):

        # disable all quiz class buttons
        partner.question_amount_btn.config(state=DISABLED)
        partner.cho_num_entry.config(state=DISABLED)
        partner.low_num_entry.config(state=DISABLED)
        partner.high_num_entry.config(state=DISABLED)
        partner.addition_btn.config(state=DISABLED)
        partner.subtraction_btn.config(state=DISABLED)
        partner.multiplication_btn.config(state=DISABLED)
        partner.help_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame,
                                 text="Help / Instruction",
                                 font="arial 20 bold",
                                 bg="#0196f7")
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               text="This is a math quiz / game"
                                    " It will help you practice Addition, subtraction and multiplication questions \n"
                               "\n"
                                    "To play the game please:\n"
                               "\n"
                                    "Enter how many questions you are wanting to play, \n"
                               "\n"
                                    "Enter the range of numbers you want your quiz to be \n"
                               "\n"
                                    "by choosing a low number and a high number e.g. 2, 7 or 10, 15\n ",
                               justify=LEFT, width=50, wrap=400, font="arial 15 ")
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="red",
                                  font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.question_amount_btn.config(state=NORMAL)
        partner.cho_num_entry.config(state=NORMAL)
        partner.low_num_entry.config(state=NORMAL)
        partner.high_num_entry.config(state=NORMAL)
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class Export:
    def __init__(self, partner, low_amount, high_amount, questions_played, how_many_right, history_questions):

        # disable export button
        partner.export_btn.config(state=DISABLED)

        # Set up child window (ie: export box)
        self.export_box = Toplevel()

        # If user press cross at top, closes export and
        # 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.how_heading = Label(self.export_frame,
                                 text="Export / Stats", fg="black",
                                 font="arial 20 bold")
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                                         "in the box below "
                                                         "button to save your "
                                                         "game history "
                                                         "to a text file.",
                                 font="arial 13 italic",
                                 justify=LEFT, width=50, wrap=200)
        self.export_text.grid(row=1)

        # Help text (label, row 1)
        self.history_label = Label(self.export_frame, text="your low number was: {}""\n"
                                                           "your high number was: {}""\n"
                                                           "you have played {} questions""\n"
                                                           "you got {} correct out of {}  ""\n"
                                   .format(low_amount, high_amount, questions_played, how_many_right, questions_played),
                                   font="arial 13 italic",
                                   justify=LEFT, width=50, wrap=200)
        self.history_label.grid(row=2)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                                         "you enter below "
                                                         "already exists, "
                                                         "its contents will "
                                                         "be replaced with "
                                                         "your game "
                                                         "history",
                                 justify=LEFT, fg="black",
                                 font="arial 10 italic", wrap=225, padx=10,
                                 pady=10)
        self.export_text.grid(row=3, pady=10)

        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=15,
                                    font="arial 14 bold")
        self.filename_entry.grid(row=4, pady=10)

        # Frame for invalid filename (row 5)
        self.save_error_label = Label(self.export_frame, text="", fg="black")
        self.save_error_label.grid(row=5)

        # Save / Cancel Frame (row 6)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=6, pady=10)

        # Save and Cancel buttons
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="arial 10 bold", fg="black",
                                  bg="#0197f6", padx=10, pady=10,
                                  command=partial(lambda: self.save_history(partner, low_amount, high_amount,
                                                                            questions_played, how_many_right,
                                                                            history_questions)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="arial 10 bold", fg="black",
                                    bg="red", padx=10, pady=10,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

        # function to save game history
    def save_history(self, partner, low_amount, high_amount, questions_played, how_many_right, history_questions):

        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            f.write("your low number was: {}""\n".format(low_amount))
            f.write("your high number was: {}""\n".format(high_amount))
            f.write("you have played {} questions""\n".format(questions_played))
            f.write("you got {} correct out of {}  ""\n".format(how_many_right, questions_played))
            f.write("{} ""\n".format(history_questions))

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_btn.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Quiz()
    root.mainloop()
