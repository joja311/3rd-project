import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        # Initialize the QuizGame class
        self.root = root
        self.root.title("Quiz Game")

        # Set up the question label
        self.question_label = tk.Label(root, text="Question goes here", font=("Helvetica", 16))
        self.question_label.pack(pady=10)

        # Set up the variable for radio buttons
        self.var = tk.StringVar()
        self.var.set(None)

        # Set up the radio buttons for answer options
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(root, text=f"Option {i+1}", variable=self.var, value=str(i+1))
            radio_button.pack(pady=5)
            self.radio_buttons.append(radio_button)

        # Set up the submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        # Set up labels for score and timer
        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(root, text="Time left: ", font=("Helvetica", 14))
        self.timer_label.pack(pady=10)

        # Initialize variables for game state
        self.current_question = 0
        self.score = 0
        self.time_left = 60

        # Define quiz questions
        self.questions = [
            {"question": "What is the capital of France?", "correct_answer": "1", "options": ["Paris", "Berlin", "Madrid", "Rome"], "points": 1},
            # Add more questions...
        ]

        # Load the first question
        self.load_question()

    def load_question(self):
        # Load the next question if available, else end the quiz
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            for i in range(4):
                self.radio_buttons[i].config(text=question_data["options"][i])

            self.var.set(None)
            self.start_timer()
        else:
            # End of the quiz
            self.question_label.config(text="Quiz completed!")
            for button in self.radio_buttons:
                button.config(state=tk.DISABLED)
            self.submit_button.config(state=tk.DISABLED)
            self.score_label.config(text=f"Final Score: {self.score}")
            self.timer_label.config(text="Time left: 0")

    def start_timer(self):
        # Start the timer for each question
        self.time_left = 15
        self.update_timer()

    def update_timer(self):
        # Update the timer label and check if time is up
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            # Time's up, move to the next question
            messagebox.showinfo("Time's up!", "You ran out of time! Moving to the next question.")
            self.current_question += 1
            self.load_question()

    def check_answer(self):
        # Check the selected answer, update score, and move to the next question
        selected_option = self.var.get()
        if selected_option == self.questions[self.current_question]["correct_answer"]:
            self.score += self.questions[self.current_question]["points"]

        self.current_question += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.load_question()


root = tk.Tk()
root.geometry("400x400")

quiz_game = QuizGame(root)

root.mainloop()
