import json
from tkinter import *

# Load Quiz Questions
questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Paris", "Rome", "Madrid"], "answer": "Paris"},
    {"question": "What is 5 + 3?", "options": ["5", "8", "10", "15"], "answer": "8"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Homer", "Tolstoy", "Dickens"], "answer": "Shakespeare"}
]

current_question = 0
score = 0

# Function to check answer
def check_answer(selected_option):
    global current_question, score
    if selected_option == questions[current_question]["answer"]:
        score += 1
    current_question += 1
    if current_question < len(questions):
        load_question()
    else:
        quiz_end()

# Function to load a question
def load_question():
    question_label.config(text=questions[current_question]["question"])
    for i in range(4):
        options[i].config(text=questions[current_question]["options"][i], command=lambda opt=questions[current_question]["options"][i]: check_answer(opt))

# Function to display the score
def quiz_end():
    question_label.config(text=f"Quiz Finished! Your Score: {score}/{len(questions)}")
    for button in options:
        button.pack_forget()

# GUI Setup
root = Tk()
root.title("Python Quiz")

question_label = Label(root, text="", font=("Arial", 14))
question_label.pack(pady=20)

options = [Button(root, text="", font=("Arial", 12), width=20) for _ in range(4)]
for btn in options:
    btn.pack(pady=5)

load_question()
root.mainloop()
