import tkinter as tk
from tkinter import messagebox
import random

def check_winner():
    """Check if a player has won the game."""
    global x_score, o_score

    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            winner = buttons[combo[0]]["text"]
            buttons[combo[0]].config(bg="lightgreen")
            buttons[combo[1]].config(bg="lightgreen")
            buttons[combo[2]].config(bg="lightgreen")

            messagebox.showinfo("Game Over", f"Player {winner} wins!")

            if winner == "X":
                x_score += 1
            else:
                o_score += 1

            update_scoreboard()
            reset_board()
            return

    # Check for draw
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_board()

def click(i):
    """Handle button click for human player."""
    global player
    if buttons[i]["text"] == "":
        buttons[i].config(text=player)
        check_winner()
        player = "O" if player == "X" else "X"
        label.config(text=f"Player {player}'s turn")

        if single_player and player == "O":
            root.after(500, ai_move)  # AI moves after 500ms

def ai_move():
    """Simple AI opponent that picks a random empty cell."""
    empty_cells = [i for i in range(9) if buttons[i]["text"] == ""]
    if empty_cells:
        ai_choice = random.choice(empty_cells)
        buttons[ai_choice].config(text="O")
        check_winner()
        global player
        player = "X"
        label.config(text="Player X's turn")

def reset_board():
    """Clears the board for a new game."""
    global player
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    player = "X"
    label.config(text="Player X's turn")

def update_scoreboard():
    """Updates the scoreboard label."""
    score_label.config(text=f"Score - X: {x_score} | O: {o_score}")

def set_mode(mode):
    """Set game mode to single-player or two-player."""
    global single_player
    single_player = (mode == "Single Player")
    mode_frame.pack_forget()  # Hide mode selection buttons
    game_frame.pack()  # Show the game board

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
player = "X"
x_score, o_score = 0, 0  # Score variables
single_player = False  # Default to two-player mode

# Mode selection frame
mode_frame = tk.Frame(root)
tk.Label(mode_frame, text="Choose Game Mode", font=("Arial", 20)).pack()
tk.Button(mode_frame, text="Single Player (vs AI)", font=("Arial", 16), command=lambda: set_mode("Single Player")).pack(pady=5)
tk.Button(mode_frame, text="Two Player", font=("Arial", 16), command=lambda: set_mode("Two Player")).pack(pady=5)
mode_frame.pack()

# Game frame (initially hidden)
game_frame = tk.Frame(root)

# Create Tic Tac Toe buttons
for i in range(9):
    btn = tk.Button(game_frame, text="", font=("Arial", 20), width=5, height=2, command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Label for turn display
label = tk.Label(game_frame, text="Player X's turn", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)

# Scoreboard label
score_label = tk.Label(game_frame, text="Score - X: 0 | O: 0", font=("Arial", 16))
score_label.grid(row=4, column=0, columnspan=3)

# Restart button
restart_btn = tk.Button(game_frame, text="Restart Game", font=("Arial", 16), command=reset_board)
restart_btn.grid(row=5, column=0, columnspan=3)

root.mainloop()
