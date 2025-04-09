import tkinter as tk

root = tk.Tk()
root.title("Workout Tracker")
root.geometry("400x400")

# Workout name
tk.Label(root, text="Workout Name:").pack()
workout_entry = tk.Entry(root)
workout_entry.pack()

# Exercise
tk.Label(root, text="Exercise:").pack()
exercise_entry = tk.Entry(root)
exercise_entry.pack()

# List to show logged workouts
log_listbox = tk.Listbox(root, width=50)
log_listbox.pack(pady=10)

# Log function with file saving
def log_workout():
    workout = workout_entry.get()
    exercise = exercise_entry.get()
    entry = f"{workout}: {exercise}"
    log_listbox.insert(tk.END, entry)

    # Save to file
    with open("workout_log.txt", "a") as file:
        file.write(entry + "\n")

    workout_entry.delete(0, tk.END)
    exercise_entry.delete(0, tk.END)

# Button to log workout
tk.Button(root, text="Log Workout", command=log_workout).pack(pady=5)

root.mainloop()

