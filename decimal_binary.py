
import tkinter as tk
from tkinter import messagebox

# Function to handle conversions based on the selected mode
def convert():
    try:
        input_value = input_entry.get().strip()
        if mode.get() == "Decimal to Binary":
            decimal_value = int(input_value)
            result.set(f"Binary: {bin(decimal_value)[2:]}")
        elif mode.get() == "Binary to Decimal":
            if not all(ch in '01' for ch in input_value):
                raise ValueError
            decimal_value = int(input_value, 2)
            result.set(f"Decimal: {decimal_value}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid value based on the selected mode.")

# Function to clear the input and result fields
def clear():
    input_entry.delete(0, tk.END)
    result.set("")

# Initialize main window
root = tk.Tk()
root.title("Decimal ↔ Binary Converter")
root.geometry("400x250")
root.resizable(0,0)

# Conversion mode options
mode = tk.StringVar(value="Decimal to Binary")

tk.Label(root, text="Decimal ↔ Binary Converter", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

# Radio buttons for selecting the conversion mode
tk.Radiobutton(root, text="Decimal to Binary", variable=mode, value="Decimal to Binary").grid(row=1, column=0, sticky="w", padx=20)
tk.Radiobutton(root, text="Binary to Decimal", variable=mode, value="Binary to Decimal").grid(row=1, column=1, sticky="w", padx=20)

# Input field
tk.Label(root, text="Enter Value:").grid(row=2, column=0, pady=10, sticky="e")
input_entry = tk.Entry(root, width=30)
input_entry.grid(row=2, column=1, pady=10, padx=10)

# Convert button
tk.Button(root, text="Convert", command=convert, width=10).grid(row=3, column=0, pady=10)

# Clear button
tk.Button(root, text="Clear", command=clear, width=10).grid(row=3, column=1, pady=10)

# Result display
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12, "italic")).grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()