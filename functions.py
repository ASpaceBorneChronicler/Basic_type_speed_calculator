import time
from tkinter import messagebox
import tkinter as tk
import random
from list import sentences

message = random.choice(sentences)

class Timer:
    def __init__(self, window, text_box, label):
        """
        Initializes the Timer class.

        Args:
            window: The main Tkinter window.
            text_box: The Tkinter Text widget for user input.
            label: The Tkinter Label widget to display the sentence.
        """
        self.start_time = None
        self.window = window
        self.sentence = label
        self.text_box = text_box
        self.message = message
        # Bind the stop method to the KeyRelease event
        self.text_box.bind("<KeyRelease>", self.stop)
        # Bind the calculate_wpm method to the Return key
        self.window.bind("<Return>", self.calculate_wpm)

    def start(self):
        """Starts the timer by recording the current time."""
        self.start_time = time.time()

    def stop(self, event=None):
        """
        Stops the timer and calculates WPM if the input matches the sentence.

        Args:
            event: The Tkinter event (default is None).
        """
        if self.text_box.get("1.0", tk.END).strip() == self.message:
            self.calculate_wpm()

    def calculate_wpm(self, event=None):
        """
        Calculates and displays the words per minute (WPM).

        Args:
            event: The Tkinter event (default is None).
        """
        elapsed_time = time.time() - self.start_time
        wpm = round((len(self.text_box.get("1.0", tk.END).strip()) / 5) / (elapsed_time / 60), 2)
        messagebox.showinfo("Speed Typing Test", f"Your typing speed is {wpm} words per minute", 
                            parent=self.window)

    def reset(self, event=None):
        """
        Resets the text box and selects a new random sentence.

        Args:
            event: The Tkinter event (default is None).
        """
        self.message = random.choice(sentences)
        self.sentence.config(text=self.message)
        self.text_box.delete("1.0", tk.END)
        # Bind the start method to the first key press
        self.text_box.bind("<Key>", lambda event: (self.start(), self.text_box.unbind("<Key>")))
        
