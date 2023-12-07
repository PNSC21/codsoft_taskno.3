import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import string

def generate_password():
    password_length = length_var.get()
    if not password_length or not password_length.isdigit() or int(password_length) <= 0:
        messagebox.showerror("Error", "Please enter a valid password length")
        return
    
    password_length = int(password_length)

    # Count for each selected category
    uppercase_count = ask_for_count("Uppercase Letters") if uppercase_var.get() else 0
    lowercase_count = ask_for_count("Lowercase Letters") if lowercase_var.get() else 0
    digit_count = ask_for_count("Digits") if digit_var.get() else 0
    symbol_count = ask_for_count("Symbols") if symbol_var.get() else 0

    # Total count for selected categories
    total_required = uppercase_count + lowercase_count + digit_count + symbol_count

    # Calculate remaining length
    remaining_length = password_length - total_required

    password = ''

    # If less than 4 categories are selected, distribute remaining characters to non-selected categories
    if not (uppercase_var.get() and lowercase_var.get() and digit_var.get() and symbol_var.get()):
        non_selected_count = remaining_length // (4 - sum([uppercase_var.get(), lowercase_var.get(), digit_var.get(), symbol_var.get()]))
        if not uppercase_var.get():
            uppercase_count += non_selected_count
        if not lowercase_var.get():
            lowercase_count += non_selected_count
        if not digit_var.get():
            digit_count += non_selected_count
        if not symbol_var.get():
            symbol_count += non_selected_count

    # Generate password based on the selected categories
    password += ''.join(random.choice(string.ascii_uppercase) for _ in range(uppercase_count))
    password += ''.join(random.choice(string.ascii_lowercase) for _ in range(lowercase_count))
    password += ''.join(random.choice(string.digits) for _ in range(digit_count))
    password += ''.join(random.choice(string.punctuation) for _ in range(symbol_count))

    # Shuffle the password characters
    password = ''.join(random.sample(password, len(password)))

    # Add remaining characters if generated password length is less than specified length
    if len(password) < password_length:
        remaining_characters = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_length - len(password)))
        password += remaining_characters

    password_label.config(text=f"Generated Password: {password}")

def ask_for_count(condition):
    count = simpledialog.askinteger("Password Generator", f"Enter the number of {condition}:",
                                    parent=root, minvalue=0)
    return count if count is not None else 0

def update_font_size(event):
    new_font_size = max(int(min(event.width, event.height) / 30), 12)
    style.configure('TLabel', font=('Arial', new_font_size), foreground='#ECF0F1', background='#34495E')
    style.configure('TButton', font=('Arial', new_font_size), background='#3498DB', foreground='#ECF0F1')
    style.configure('TCheckbutton', font=('Arial', new_font_size), background='#34495E', foreground='#ECF0F1')
    length_entry.configure(foreground='#34495E')

def update_main_window_geometry():
    root.update_idletasks()
    root.geometry("")

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x350")

style = ttk.Style()
style.configure('TFrame', background='#34495E')
style.configure('TLabel', font=('Arial', 10), foreground='#ECF0F1', background='#34495E')
style.configure('TButton', font=('Arial', 10), background='#3498DB', foreground='#ECF0F1')
style.configure('TCheckbutton', font=('Arial', 10), background='#34495E', foreground='#ECF0F1')

frame = ttk.Frame(root, padding=10, style='TFrame')
frame.pack(expand=True, fill='both')

instruction_label = ttk.Label(frame, text="Instructions:\n1. Enter the desired password length.\n2. Optionally, select the conditions for the password (Uppercase, Lowercase, Digits, Symbols).\n3. Click 'Generate Password'.", style='TLabel')
instruction_label.grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)

length_label = ttk.Label(frame, text="Password Length:", style='TLabel')
length_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

length_var = tk.StringVar()
length_entry = ttk.Entry(frame, textvariable=length_var, width=5, foreground='#34495E')
length_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

uppercase_var = tk.IntVar()
uppercase_check = ttk.Checkbutton(frame, text="Uppercase Letters", variable=uppercase_var, style='TCheckbutton')
uppercase_check.grid(row=2, column=0, columnspan=2, pady=5, sticky=tk.W)

lowercase_var = tk.IntVar()
lowercase_check = ttk.Checkbutton(frame, text="Lowercase Letters", variable=lowercase_var, style='TCheckbutton')
lowercase_check.grid(row=3, column=0, columnspan=2, pady=5, sticky=tk.W)

digit_var = tk.IntVar()
digit_check = ttk.Checkbutton(frame, text="Digits", variable=digit_var, style='TCheckbutton')
digit_check.grid(row=4, column=0, columnspan=2, pady=5, sticky=tk.W)

symbol_var = tk.IntVar()
symbol_check = ttk.Checkbutton(frame, text="Symbols", variable=symbol_var, style='TCheckbutton')
symbol_check.grid(row=5, column=0, columnspan=2, pady=5, sticky=tk.W)

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password, style='TButton')
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password, style='TButton')
generate_button.grid(row=6, column=0, columnspan=2, pady=10)
style.map('TButton', foreground=[('pressed', 'black'), ('active', 'black'), ('!disabled', 'black')])


password_label = ttk.Label(frame, text="Generated Password: ", style='TLabel')
password_label.grid(row=7, column=0, columnspan=2, pady=10)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.bind('<Configure>', update_font_size)

root.mainloop()
