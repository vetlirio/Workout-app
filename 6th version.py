import tkinter as tk
import os

# Global flag for edit mode
edit_mode_enabled = False
exercises = ["Incline Dumbbell Press", "Squat", "Deadlift", "Overhead Press"]

def toggle_edit_mode():
    global edit_mode_enabled
    edit_mode_enabled = not edit_mode_enabled
    if edit_mode_enabled:
        edit_button.config(text="Editing ✏️", fg="green")
        log_listbox.config(selectmode=tk.SINGLE)  # Enable selection in edit mode
    else:
        edit_button.config(text="Edit ✏️", fg="black")
        log_listbox.config(selectmode=tk.NONE)  # Disable selection when not in edit mode
        log_listbox.selection_clear(0, tk.END)
        entry_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Workout Tracker")
root.geometry("500x600")

# ======= MAIN CONTAINERS =======
main_menu_frame = tk.Frame(root)
log_frame = tk.Frame(root)

main_menu_frame.pack(fill="both", expand=True)

# ======= MAIN MENU (Exercise Buttons) =======
tk.Label(main_menu_frame, text="Select an Exercise", font=("Arial", 16)).pack(pady=10)

# Add dynamic buttons for exercises
def update_exercise_buttons():
    for widget in main_menu_frame.winfo_children():
        if isinstance(widget, tk.Button):
            widget.destroy()  # Remove previous buttons

    for ex in exercises:
        btn = tk.Button(main_menu_frame, text=ex, width=40, height=2, command=lambda e=ex: open_log_sheet(e))
        btn.pack(pady=4)

# Add new exercise function
def add_exercise():
    new_exercise = exercise_entry.get()
    if new_exercise and new_exercise not in exercises:
        exercises.append(new_exercise)
        exercise_entry.delete(0, tk.END)
        update_exercise_buttons()

# Entry field to add new exercise
exercise_entry = tk.Entry(main_menu_frame, width=40)
exercise_entry.pack(pady=5)

# Add exercise button
add_button = tk.Button(main_menu_frame, text="Add Exercise", command=add_exercise)
add_button.pack(pady=5)

# Remove exercise function
def remove_exercise():
    exercise_to_remove = exercise_entry.get()
    if exercise_to_remove in exercises:
        exercises.remove(exercise_to_remove)
        exercise_entry.delete(0, tk.END)
        update_exercise_buttons()

# Remove exercise button
remove_button = tk.Button(main_menu_frame, text="Remove Exercise", command=remove_exercise)
remove_button.pack(pady=5)

update_exercise_buttons()  # Update exercise buttons initially

# ======= LOG SHEET VIEW =======
selected_exercise_label = tk.Label(log_frame, text="", font=("Arial", 10), anchor="w")
selected_exercise_label.pack(pady=5, anchor="w", padx=20)

log_listbox = tk.Listbox(
    log_frame, 
    width=50, 
    height=10, 
    font=("Courier", 10), 
    bd=0,  # Remove border
    bg=root.cget('background'),  # Use the root window background
    selectmode=tk.SINGLE,  # Enable selection in edit mode
    activestyle="none"  # No highlight when clicked
)
log_listbox.pack(pady=10)

edit_button = tk.Button(log_frame, text="Edit ✏️", command=toggle_edit_mode)
edit_button.pack(anchor="se", padx=10, pady=10)

entry_label = tk.Label(log_frame, text="Today's Set:")
entry_label.pack()
entry_entry = tk.Entry(log_frame, width=40)
entry_entry.pack()

# Save the log
def save_log(exercise):
    today = "09/04"  # You can update this with real auto-dates
    entry = entry_entry.get()
    line = f"{today}: {entry}"
    filename = f"{exercise}.txt"
    with open(filename, "a") as file:
        file.write(line + "\n")
    entry_entry.delete(0, tk.END)
    load_log(exercise)

# Load log from file
def load_log(exercise):
    filename = f"{exercise}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            log_listbox.delete(0, tk.END)  # Clear previous logs
            for line in lines:
                log_listbox.insert(tk.END, line.strip())  # Add logs to the list
    else:
        log_listbox.insert(tk.END, "(no logs yet)")

# Open the log sheet for selected exercise
def open_log_sheet(exercise):
    main_menu_frame.pack_forget()
    log_frame.pack(fill="both", expand=True)
    selected_exercise_label.config(text=exercise)  # Set the exercise name here
    save_button.config(command=lambda: save_log(exercise))
    load_log(exercise)

# Go back to the exercise selection screen
def go_back():
    log_frame.pack_forget()
    main_menu_frame.pack(fill="both", expand=True)

# Save and back buttons
save_button = tk.Button(log_frame, text="Save", width=20)
save_button.pack(pady=10)

back_button = tk.Button(log_frame, text="← Back", command=go_back)
back_button.pack(pady=10)

# Allow editing when in edit mode
def edit_selected_log(exercise):
    if not edit_mode_enabled:
        return  # Do nothing if edit mode is off

    selection = log_listbox.curselection()
