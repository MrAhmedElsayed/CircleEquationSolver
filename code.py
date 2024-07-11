import tkinter as tk
from tkinter import ttk

def generate_circle_equation():
    h = float(entry_h.get())
    k = float(entry_k.get())
    r = float(entry_r.get())
    
    standard_form, general_form = circle_equation(h, k, r)
    
    result_text.set(f"Standard form: {standard_form}\nGeneral form: {general_form}")

# Function to generate circle equation
def circle_equation(h, k, r):
    # Standard form of the circle equation
    standard_form = f"(x - {h})^2 + (y - {k})^2 = {r**2}"
    
    # Convert to general form
    D = -2 * h
    E = -2 * k
    F = h**2 + k**2 - r**2
    
    general_form = f"x^2 + y^2 + ({D})x + ({E})y + ({F}) = 0"
    
    return standard_form, general_form

# Create GUI window
root = tk.Tk()
root.title("Circle Equation Generator")

# Create input fields
label_h = ttk.Label(root, text="Enter center x-coordinate (h):")
label_h.grid(row=0, column=0, padx=5, pady=5)
entry_h = ttk.Entry(root)
entry_h.grid(row=0, column=1, padx=5, pady=5)

label_k = ttk.Label(root, text="Enter center y-coordinate (k):")
label_k.grid(row=1, column=0, padx=5, pady=5)
entry_k = ttk.Entry(root)
entry_k.grid(row=1, column=1, padx=5, pady=5)

label_r = ttk.Label(root, text="Enter radius (r):")
label_r.grid(row=2, column=0, padx=5, pady=5)
entry_r = ttk.Entry(root)
entry_r.grid(row=2, column=1, padx=5, pady=5)

# Create button to generate equation
generate_button = ttk.Button(root, text="Generate Equation", command=generate_circle_equation)
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create label to display result
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, wraplength=300)
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start GUI event loop
root.mainloop()
