import tkinter as tk
import random
import string
import uuid
from tkinter import messagebox

def buy_ticket(name_entry, age_entry, gender_var, start_entry, end_entry):
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    start_station = start_entry.get()
    end_station = end_entry.get()

    # Add your ticket purchase logic here
    # For now, let's just show the details and a random PNR number
    global pnr  # Declare pnr as global to store it for later use
    pnr = generate_pnr()

    # Display passenger details and PNR in a messagebox
    message = f"Name: {name}\nAge: {age}\nGender: {gender}\nStarting Station: {start_station}\nEnding Station: {end_station}\nPNR Number: {pnr}"
    messagebox.showinfo("Ticket Details", message)

def check_pnr_status(name, age, gender, start_station, end_station):
    # Add your PNR status check logic here
    # For now, let's just show a messagebox with the PNR status
    status = "Confirmed" if random.random() < 0.8 else "Waiting List"
    message = f"Name: {name}\nAge: {age}\nGender: {gender}\nStarting Station: {start_station}\nEnding Station: {end_station}\nPNR: {pnr}\nStatus: {status}"
    messagebox.showinfo("PNR Status", message)

def generate_pnr():
    # Generate a random PNR number using UUID
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def main():
    window = tk.Tk()
    window.title("Local Train Ticketing System")
    window.geometry("400x600")
    window.configure(bg="green")

    # Create a big text label
    big_text_label = tk.Label(window, text="Local Train Ticketing System", font=("Helvetica", 20), bg="green", fg="white")
    big_text_label.pack(pady=20)

    # Create entry widgets for name, age, and gender
    name_label = tk.Label(window, text="Name:", font=("Helvetica", 14), bg="green", fg="white")
    name_label.pack()
    name_entry = tk.Entry(window, font=("Helvetica", 14))
    name_entry.pack()

    age_label = tk.Label(window, text="Age:", font=("Helvetica", 14), bg="green", fg="white")
    age_label.pack()
    age_entry = tk.Entry(window, font=("Helvetica", 14))
    age_entry.pack()

    gender_label = tk.Label(window, text="Gender:", font=("Helvetica", 14), bg="green", fg="white")
    gender_label.pack()
    gender_var = tk.StringVar()
    gender_var.set("Male")  # Default value
    gender_choices = ["Male", "Female", "Other"]
    gender_dropdown = tk.OptionMenu(window, gender_var, *gender_choices)
    gender_dropdown.pack()

    # Create entry widgets for starting and ending station names
    start_label = tk.Label(window, text="Starting Station:", font=("Helvetica", 14), bg="green", fg="white")
    start_label.pack()
    start_entry = tk.Entry(window, font=("Helvetica", 14))
    start_entry.pack()

    end_label = tk.Label(window, text="Ending Station:", font=("Helvetica", 14), bg="green", fg="white")
    end_label.pack()
    end_entry = tk.Entry(window, font=("Helvetica", 14))
    end_entry.pack()

    # Create a button to buy a ticket
    buy_button = tk.Button(window, text="Buy Ticket", font=("Helvetica", 16), bg="white", fg="green", command=lambda: buy_ticket(name_entry, age_entry, gender_var, start_entry, end_entry))
    buy_button.pack(pady=10)

    # Create a separate entry widget for entering PNR number to check status
    pnr_label = tk.Label(window, text="Enter PNR:", font=("Helvetica", 14), bg="green", fg="white")
    pnr_label.pack()
    pnr_entry = tk.Entry(window, font=("Helvetica", 14))
    pnr_entry.pack()

    # Create a button to check PNR status
    check_status_button = tk.Button(window, text="Check PNR Status", font=("Helvetica", 16), bg="white", fg="green", command=lambda: check_pnr_status(name_entry.get(), age_entry.get(), gender_var.get(), start_entry.get(), end_entry.get()))
    check_status_button.pack(pady=10)

    # Run the GUI main loop
    window.mainloop()

if __name__ == "__main__":
    main()
