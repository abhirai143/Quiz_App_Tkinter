THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface():

    def __init__(self, q_list: QuizBrain):
        self.quiz = q_list
        self.window = Tk()
        self.m = "true"
        self.f = "false"
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.ans_label = Label(text="", fg="white", bg=THEME_COLOR)
        self.ans_label.grid(column=0, row=0)

        self.score_label = Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 125, text="", width=280,font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.right_img = PhotoImage(file="images/true.png")
        self.right = Button(self.window, image=self.right_img, text="true", highlightthickness=0, command=lambda m="true": self.on_click_r(self.m))
        self.right.grid(column=0, row=2)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.wrong_img, highlightthickness=0, command=lambda m="false": self.on_click_w(self.f))
        self.wrong.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.ans_label.config(text="")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)

    def on_click_r(self,button_press):
        user_answer = button_press
        score = self.quiz.check_answer(user_answer)
        self.score_label.config(text=f"Score: {score}")
        self.ans_label.config(text="True 🥳")
        self.get_next_question()



    def on_click_w(self,button_press):
        user_answer = button_press
        score = self.quiz.check_answer(user_answer)
        self.score_label.config(text=f"Score: {score}")
        self.ans_label.config(text="False 😟")
        self.get_next_question()


