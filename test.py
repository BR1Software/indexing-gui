import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("300x200")

def show_panel():
    if not hidden_frame.winfo_ismapped():
        hidden_frame.grid(row=1, column=0, pady=10)
    else:
        hidden_frame.grid_remove()

# Create a button to toggle the panel
toggle_button = tk.Button(root, text="Show/Hide Panel", command=show_panel)
toggle_button.grid(row=0, column=0, padx=10, pady=10)

# Create the hidden panel (Frame)
hidden_frame = tk.Frame(root, bg="lightblue", height=100)
hidden_label = tk.Label(hidden_frame, text="This is a hidden panel", bg="lightblue")
hidden_label.pack(pady=20)

label = tk.Label(root, text="This is the main window", bg="lightgreen")
label.grid(row=2, column=0, padx=10, pady=10)

# Initially hide the panel
hidden_frame.grid_remove()

root.mainloop()