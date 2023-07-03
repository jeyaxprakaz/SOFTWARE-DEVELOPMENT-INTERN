import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.simpledialog as sd

class Bug:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.is_fixed = False

    def mark_as_fixed(self):
        self.is_fixed = True

    def __str__(self):
        return f"Bug: ID={self.id}, Description={self.description}, Fixed={self.is_fixed}"


class BugTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bug Tracker")
        self.bug_tracker = []

        style = ttk.Style()
        style.configure("Bug.TButton", foreground="red", font=("Arial", 12))

        self.bug_listbox = tk.Listbox(self, width=50, height=10, font=("Arial", 14))
        self.add_button = ttk.Button(self, text="Add Bug", command=self.add_bug, style="Bug.TButton")
        self.mark_fixed_button = ttk.Button(self, text="Mark as Fixed", command=self.mark_as_fixed, style="Bug.TButton")

        self.bug_listbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.add_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.mark_fixed_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def add_bug(self):
        description = sd.askstring("Add Bug", "Enter bug description:")
        if description:
            bug_id = len(self.bug_tracker) + 1
            bug = Bug(bug_id, description)
            self.bug_tracker.append(bug)
            self.bug_listbox.insert(tk.END, str(bug))

    def mark_as_fixed(self):
        selected_index = self.bug_listbox.curselection()
        if selected_index:
            bug = self.bug_tracker[selected_index[0]]
            bug.mark_as_fixed()
            self.bug_listbox.delete(selected_index)
            messagebox.showinfo("Bug Fixed", f"Bug with ID={bug.id} marked as fixed.")
        else:
            messagebox.showwarning("No Bug Selected", "Please select a bug from the list.")

if __name__ == "__main__":
    app = BugTrackerApp()
    app.mainloop()
