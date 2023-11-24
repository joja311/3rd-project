import tkinter as tk
from tkinter import messagebox
import time

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.question_label = tk.Label(root, text="Question goes here", font=("Helvetica", 16))
        self.question_label.pack(pady=10)

        self.var = tk.StringVar()
        self.var.set(None)

        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(root, text=f"Option {i+1}", variable=self.var, value=str(i+1))
            radio_button.pack(pady=5)
            self.radio_buttons.append(radio_button)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(root, text="Time left: ", font=("Helvetica", 14))
        self.timer_label.pack(pady=10)

        self.current_question = 0
        self.score = 0
        self.time_left = 60

        self.questions = [
            {"question": "What is the capital of France?", "correct_answer": "1", "options": ["Paris", "Berlin", "Madrid", "Rome"], "points": 1},
            {"question": "Which planet is known as the Red Planet?", "correct_answer": "2", "options": ["Earth", "Mars", "Jupiter", "Venus"], "points": 2},
            {"question": "What is the largest mammal in the world?", "correct_answer": "3", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "points": 3},
            {"question": "Who wrote 'Romeo and Juliet'?", "correct_answer": "4", "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "points": 4},
            {"question": "What is the currency of Japan?", "correct_answer": "1", "options": ["Yen", "Euro", "Dollar", "Pound"], "points": 1},

            {"question": "What is the capital of Australia?", "correct_answer": "1", "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"], "points": 1},
            {"question": "In which year did World War II end?", "correct_answer": "3", "options": ["1942", "1945", "1950", "1939"], "points": 3},
            {"question": "Who painted the Mona Lisa?", "correct_answer": "2", "options": ["Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Claude Monet"], "points": 2},
            {"question": "Which ocean is the largest?", "correct_answer": "4", "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"], "points": 4},

        ]

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            for i in range(4):
                self.radio_buttons[i].config(text=question_data["options"][i])

            self.var.set(None)
            self.start_timer()
        else:
            self.question_label.config(text="Quiz completed!")
            for button in self.radio_buttons:
                button.config(state=tk.DISABLED)
            self.submit_button.config(state=tk.DISABLED)
            self.score_label.config(text=f"Final Score: {self.score}")
            self.timer_label.config(text="Time left: 0")

    def start_timer(self):
        self.time_left = 15 
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.time_left -= 0 #bug in time left it accelerates I set this to 0 instead of 1
            self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's up!", "You ran out of time! Moving to the next question.")
            self.current_question += 1
            self.load_question()

    def check_answer(self):
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
