import tkinter as tk
from tkinter import messagebox
import datetime


class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def mark_attendance(self, student_id):
        now = datetime.datetime.now()
        date = now.date()
        time = now.strftime("%H:%M:%S")

        if student_id in self.students:
            self.students[student_id].append((date, time))
        else:
            self.students[student_id] = [(date, time)]

    def get_attendance(self, student_id):
        if student_id in self.students:
            return self.students[student_id]
        else:
            return []


def mark_attendance():
    student_id = entry.get()
    if student_id:
        attendance_system.mark_attendance(student_id)
        messagebox.showinfo("Attendance Marked", f"Attendance marked for student {student_id}")
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a student ID")


def get_attendance():
    student_id = entry.get()
    if student_id:
        attendance = attendance_system.get_attendance(student_id)
        messagebox.showinfo("Attendance Records", f"Attendance records for student {student_id}:\n\n{attendance}")
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a student ID")


# Create the main window
root = tk.Tk()
root.title("Attendance Monitoring System")

# Set the font size
font = ("Arial", 14)

# Create an instance of the AttendanceSystem class
attendance_system = AttendanceSystem()

# Create and grid the label and entry widgets
label = tk.Label(root, text="Student ID:", font=font)
label.grid(row=0, column=0, pady=10)

entry = tk.Entry(root, width=30, font=font)
entry.grid(row=0, column=1, pady=5)

# Create and grid the mark attendance and get attendance buttons
mark_button = tk.Button(root, text="Mark Attendance", command=mark_attendance, font=font)
mark_button.grid(row=1, column=0, columnspan=2, pady=5)

get_button = tk.Button(root, text="Get Attendance", command=get_attendance, font=font)
get_button.grid(row=2, column=0, columnspan=2, pady=5)

# Center the main content
root.update_idletasks()  # Update the window's geometry information
width = root.winfo_width()
height = root.winfo_height()
x_offset = (root.winfo_screenwidth() - width) // 2
y_offset = (root.winfo_screenheight() - height) // 2
root.geometry(f"+{x_offset}+{y_offset}")

# Call the mainloop function
root.mainloop()
