import tkinter as tk
from functions import Timer, message


window = tk.Tk()
window.title("Speed Typing Test")
window.config(padx=10, pady=10)

# Header
instruction = tk.Label(window, text="Start Typing", font=("Helvetica", 20))
label = tk.Label(window, 
                 text=  message, 
                 font=("Helvetica", 15))

instruction.pack()
label.pack()

# Text Box
text_box = tk.Text(window, 
                   font=("Helvetica", 15), 
                   padx=10, 
                   pady=10, 
                   wrap="word", 
                   relief="flat", 
                   highlightthickness=1,  
                   bd=0)
text_box.focus_set()
text_box.pack()

# Initialize timer
timer = Timer(window, text_box, label)

start_button = tk.Button(window, 
                         text="Start Again", 
                         width=20, 
                         command=timer.reset, 
                         font=("Helvetica", 10), 
                         relief="flat",
                         )
start_button.pack(pady=20)

# Starts timer when a key is pressed
text_box.bind("<Key>", lambda event: (timer.start(), text_box.unbind("<Key>")))

window.mainloop()
