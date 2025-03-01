import tkinter as tk
from tkinter import messagebox

def register():
    name = name_entry.get()
    department = department_entry.get()
    year = year_entry.get()
    section = section_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not all([name, department, year, section, password, confirm_password]):
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    # Store user data in a file (database simulation)
    with open("users.txt", "a") as file:
        file.write(f"{name},{department},{year},{section},{password}\n")

    messagebox.showinfo("Success", "✅ Successfully Registered!")
    root.destroy()  # Close the window after registration

# Create GUI window
root = tk.Tk()
root.title("User Registration")
root.geometry("350x400")

# Labels and Entry Fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Department").pack()
department_entry = tk.Entry(root)
department_entry.pack()

tk.Label(root, text="Year").pack()
year_entry = tk.Entry(root)
year_entry.pack()

tk.Label(root, text="Section").pack()
section_entry = tk.Entry(root)
section_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Label(root, text="Confirm Password").pack()
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.pack()

# Register Button
tk.Button(root, text="Register", command=register).pack(pady=10)

# Run the GUI
root.mainloop()
