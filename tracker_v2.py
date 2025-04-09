import tkinter as tk

root = tk.Tk()
root.title("Workout Tracker")
root.geometry("500x500")

# List of exercises
exercises = ["Incline Dumbbell Press", "Squat", "Deadlift", "Overhead Press"]

# Label to show selected exercise
selected_exercise_label = tk.Label(root, text="Select an exercise", font=("Arial", 14))
selected_exercise_label.pack(pady=10)

# Frame to hold exercise buttons
exercise_frame = tk.Frame(root)
exercise_frame.pack()

# This label will show the full log
log_display = tk.Label(root, text="", justify="left", anchor="w", font=("Courier", 10))
log_display.pack(pady=10)

# Input for today's entry
entry_label = tk.Label(root, text="Today's Set:")
entry_label.pack()
entry_entry = tk.Entry(root, width=40)
entry_entry.pack()

# Save function
def save_log(exercise):
    today = "09/04"  # You can replace this with auto-date later
    entry = entry_entry.get()
    line = f"{today}: {entry}"

    filename = f"{exercise}.txt"
    with open(filename, "a") as file:
        file.write(line + "\n")

    entry_entry.delete(0, tk.END)
    load_log(exercise)

# Load function
def load_log(exercise):
    filename = f"{exercise}.txt"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            lines = lines[::-1]  # Reverse so latest is first
            log_display.config(text=f"{exercise}:\n" + "".join(lines))
    except FileNotFoundError:
        log_display.config(text=f"{exercise}:\n")

# Updated select_exercise
def select_exercise(name):
    selected_exercise_label.config(text=f"Exercise: {name}")
    # Change save button to work with this exercise
    save_button.config(command=lambda: save_log(name))
    load_log(name)

# Save button (placed at the bottom of your code)
save_button = tk.Button(root, text="Save", width=20)
save_button.pack(pady=10)


# Create a button for each exercise
for exercise in exercises:
    btn = tk.Button(exercise_frame, text=exercise, width=30, command=lambda e=exercise: select_exercise(e))
    btn.pack(pady=2)

root.mainloop()
