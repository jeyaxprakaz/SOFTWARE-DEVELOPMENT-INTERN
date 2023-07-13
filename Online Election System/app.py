import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askinteger


def vote():
    selected_candidate = candidate_list.get(tk.ACTIVE)
    candidate_votes.setdefault(selected_candidate, 0)
    candidate_votes[selected_candidate] += 1
    result_text.delete(1.0, tk.END)
    for candidate in candidate_votes:
        result_text.insert(tk.END, f"{candidate}: {candidate_votes[candidate]} votes\n")

    winner = calculate_winner()
    result_text.insert(tk.END, f"\nWinner: {winner}")


def calculate_winner():
    max_votes = max(candidate_votes.values())
    winners = [candidate for candidate, votes in candidate_votes.items() if votes == max_votes]
    if len(winners) == 1:
        return winners[0]
    else:
        return "Tie"


root = tk.Tk()
root.title("Online Election Management System")
root.geometry("600x400")

voting_frame = tk.Frame(root)
voting_frame.pack(pady=10)

num_candidates = askinteger("Number of Candidates", "Enter the number of candidates:")
candidate_list = tk.Listbox(voting_frame, height=10, width=20)
candidate_list.pack(side="left", padx=10)

for i in range(num_candidates):
    candidate_name = f"Candidate {i + 1}"
    candidate_list.insert(tk.END, candidate_name)

vote_button = tk.Button(voting_frame, text="Vote", command=vote)
vote_button.pack(side="right", padx=10)

result_frame = tk.Frame(root)
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="Result")
result_label.pack()

result_text = tk.Text(result_frame, height=10, width=20)
result_text.pack()

candidate_votes = {}  # Initialize the candidate_votes dictionary

root.mainloop()
