import tkinter as tk

# Function to perform addition
def add():
    try:
        result.set(float(num1.get()) + float(num2.get()))
    except ValueError:
        result.set("Error")

# Function to perform subtraction
def subtract():
    try:
        result.set(float(num1.get()) - float(num2.get()))
    except ValueError:
        result.set("Error")

# Function to perform multiplication
def multiply():
    try:
        result.set(float(num1.get()) * float(num2.get()))
    except ValueError:
        result.set("Error")

# Function to perform division
def divide():
    try:
        if float(num2.get()) == 0:
            result.set("Error! Cannot divide by zero.")
        else:
            result.set(float(num1.get()) / float(num2.get()))
    except ValueError:
        result.set("Error")

# Function to append digit to the entry field
def append_digit(digit):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + digit)

# Function to clear entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")  # Set window size

# Set colors
bg_color = "#FFFFFF"  # White
button_bg_color = "#E0E0E0"  # Light Gray
button_active_bg_color = "#BDBDBD"  # Slightly Darker Gray
button_fg_color = "#000000"  # Black
label_fg_color = "#000000"  # Black

# Set fonts
large_font = ("Helvetica", 12)
small_font = ("Helvetica", 10)

# Configure window background color
window.configure(bg=bg_color)

# Create input field
entry = tk.Entry(window, font=large_font, justify="right", bg=button_bg_color, fg=button_fg_color)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Create buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(window, text=text, font=large_font, bg=button_bg_color, fg=button_fg_color,
                       activebackground=button_active_bg_color, width=5, height=2,
                       command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Function to handle button clicks
def on_button_click(text):
    if text == '=':
        try:
            result.set(eval(entry.get()))
        except Exception as e:
            result.set("Error")
    elif text == 'C':
        clear_entry()
    else:
        append_digit(text)

# Create a label to display the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, bg=bg_color, fg=label_fg_color, font=large_font)
result_label.grid(row=5, columnspan=4, padx=10, pady=10, sticky="ew")

# Run the GUI
window.mainloop()
