import tkinter as tk
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    history.append((user_choice, computer_choice, result))

def clear_history():
    history.clear()
    history_label.config(text="")

def view_history():
    history_text = "\n".join(f"User: {user_choice}, Computer: {computer_choice}, Result: {result}" for user_choice, computer_choice, result in history)
    history_label.config(text=history_text)

def create_game_window():
    global history
    history = []

    game_window = tk.Toplevel(root)
    game_window.title("Rock Paper Scissors Game")
    game_window.geometry("400x250")  # Set dimensions of the game window (width x height)

    rock_button = tk.Button(game_window, text="Rock", command=lambda: play_game('rock'))
    rock_button.pack()

    paper_button = tk.Button(game_window, text="Paper", command=lambda: play_game('paper'))
    paper_button.pack()

    scissors_button = tk.Button(game_window, text="Scissors", command=lambda: play_game('scissors'))
    scissors_button.pack()

    global result_label
    result_label = tk.Label(game_window, text="", font=("Arial", 12))
    result_label.pack()

    global history_label
    history_label = tk.Label(game_window, text="", font=("Arial", 12))
    history_label.pack()

    clear_button = tk.Button(game_window, text="Clear History", command=clear_history)
    clear_button.pack()

    view_button = tk.Button(game_window, text="View History", command=view_history)
    view_button.pack()

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("300x100")  # Set dimensions of the main window (width x height)

# Create the play button
play_button = tk.Button(root, text="Play Game", command=create_game_window)
play_button.pack()

# Start the GUI event loop
root.mainloop()
