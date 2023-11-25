Quiz Game

Welcome to the Quiz Game! This is a simple quiz application built using Tkinter in Python.
Getting Started
Prerequisites

Make sure you have Python installed on your machine.
Installation

    Clone the repository:

git clone https://github.com/joja311/3rd-project.git

Navigate to the project directory:


cd 3rd-project

Install the required packages:
    pip install tk

Running the Quiz Game

Run the following command to start the quiz game:
python quiz_game.py

How to Play

    The quiz consists of multiple-choice questions with four options each.

    Select the correct option for each question.

    Click the "Submit" button to check your answer.

    The timer on the top-right corner indicates the time left for each question.

    If the timer runs out, the game will automatically move to the next question.

    After completing the quiz, the final score will be displayed.

Customizing Questions

You can customize the quiz questions by modifying the questions list in the QuizGame class in the quiz_game.py file.

python

self.questions = [
    {"question": "Your Question Here", "correct_answer": "1", "options": ["Option 1", "Option 2", "Option 3", "Option 4"], "points": 1},
    # Add more questions...
]

Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.
