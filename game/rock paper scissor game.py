import tkinter as tk
from tkinter import messagebox
import random


# Main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("550x600")
window.resizable(False, False)


# Score
user_score = 0
computer_score = 0


# Heading
heading = tk.Label(
    window,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 24, "bold")
)
heading.pack(pady=25)


# Instructions
instruction = tk.Label(
    window,
    text="Choose your move:",
    font=("Arial", 17)
)
instruction.pack(pady=10)


# Result labels
user_choice_label = tk.Label(
    window,
    text="Your Choice: -",
    font=("Arial", 16)
)
user_choice_label.pack(pady=8)


computer_choice_label = tk.Label(
    window,
    text="Computer Choice: -",
    font=("Arial", 16)
)
computer_choice_label.pack(pady=8)


result_label = tk.Label(
    window,
    text="Let's Play!",
    font=("Arial", 20, "bold")
)
result_label.pack(pady=20)


# Score label
score_label = tk.Label(
    window,
    text="You: 0    Computer: 0",
    font=("Arial", 16, "bold")
)
score_label.pack(pady=10)


# Game function
def play_game(user_choice):

    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]

    computer_choice = random.choice(choices)

    # Show choices
    user_choice_label.config(
        text="Your Choice: " + user_choice
    )

    computer_choice_label.config(
        text="Computer Choice: " + computer_choice
    )

    # Decide winner
    if user_choice == computer_choice:
        result = "It's a Draw!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win! 🎉"
        user_score += 1

    else:
        result = "Computer Wins!"

        computer_score += 1

    # Show result
    result_label.config(text=result)

    # Update score
    score_label.config(
        text=f"You: {user_score}    Computer: {computer_score}"
    )


# Buttons frame
button_frame = tk.Frame(window)
button_frame.pack(pady=20)


# Rock button
tk.Button(
    button_frame,
    text="🪨 ROCK",
    font=("Arial", 15),
    width=12,
    height=2,
    command=lambda: play_game("Rock")
).grid(row=0, column=0, padx=8)


# Paper button
tk.Button(
    button_frame,
    text="📄 PAPER",
    font=("Arial", 15),
    width=12,
    height=2,
    command=lambda: play_game("Paper")
).grid(row=0, column=1, padx=8)


# Scissors button
tk.Button(
    button_frame,
    text="✂️ SCISSORS",
    font=("Arial", 15),
    width=12,
    height=2,
    command=lambda: play_game("Scissors")
).grid(row=0, column=2, padx=8)


# Reset game
def reset_game():

    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_choice_label.config(
        text="Your Choice: -"
    )

    computer_choice_label.config(
        text="Computer Choice: -"
    )

    result_label.config(
        text="Let's Play!"
    )

    score_label.config(
        text="You: 0    Computer: 0"
    )


# Reset button
tk.Button(
    window,
    text="RESET GAME",
    font=("Arial", 14),
    width=20,
    height=2,
    command=reset_game
).pack(pady=20)


# Start game
window.mainloop()