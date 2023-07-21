import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # Update every 1 second

# Create the main window
window = tk.Tk()
window.title("Digital Clock")

label=tk.Label(window, text="🧭🧭CLOCK🧭🧭" ,font=("verdana", 30))
label.pack(padx=100, pady=50)

# Create a label to display the clock
clock_label = tk.Label(window, font=("garamond", 80), bg="olive", fg="black")
clock_label.pack(padx=150, pady=150)

# Start the clock
update_clock()

# Run the main event loop
window.mainloop()
