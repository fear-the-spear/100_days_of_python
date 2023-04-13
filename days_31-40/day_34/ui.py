from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.scoreboard = Label(text="Score: 0", bg=THEME_COLOR)
        self.scoreboard.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="This is a test.",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280,
            anchor="center"
        )
        self.canvas.grid(
            column=0,
            row=1,
            columnspan=2,
            pady=50
        )

        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(
            image=true_img,
            highlightthickness=0,
            border=0,
            command=self.true_pressed
        )
        self.true_btn.grid(column=0, row=2)
        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(
            image=false_img,
            highlightthickness=0,
            border=0,
            command=self.false_pressed
        )
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.scoreboard.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            print(is_right)
        else:
            self.canvas.config(bg="red")
            print(is_right)
        self.window.after(1000, self.get_next_question)
