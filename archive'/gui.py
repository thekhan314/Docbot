import tkinter as tk
from threading import Thread
import time
import random
class ScriptApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Script App")

        # Entry widgets for user input
        self.base_time_entry = tk.Entry(self.master)
        self.base_time_entry.grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.master, text="Base Time:").grid(row=0, column=1, padx=10, pady=10)

        self.random_interval_entry = tk.Entry(self.master)
        self.random_interval_entry.grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.master, text="Random Interval:").grid(row=1, column=1, padx=10, pady=10)

        # Text boxes for script output
        self.text_box1 = tk.Text(self.master, height=10, width=40)
        self.text_box1.grid(row=2, column=0, padx=10, pady=10)


        # Buttons for script control
        self.start_button = tk.Button(self.master, text="Start Script", command=self.start_script)
        self.start_button.grid(row=3, column=0, pady=10)

        self.stop_button = tk.Button(self.master, text="Stop Script", command=self.stop_script)
        self.stop_button.grid(row=3, column=1, pady=10)

        # Variables to store user input
        self.base_time = tk.IntVar()
        self.random_interval = tk.IntVar()

        # Variables to track script state
        self.is_running = False
        self.script_thread = None

    def start_script(self):
        if not self.is_running:
            # Get user input values
            self.base_time.set(int(self.base_time_entry.get()))
            self.random_interval.set(int(self.random_interval_entry.get()))

            # Start script in a new thread
            self.is_running = True
            self.script_thread = Thread(target=self.run_script)
            self.script_thread.start()

    def run_script(self):
        while self.is_running:
            # Simulate a script adding text
            text1 = f"Script Output 1: {time.ctime()}\n"
            text2 = f"Script Output 2: {time.ctime()}\n"

            self.text_box1.insert(tk.END, text1)
            self.text_box2.insert(tk.END, text2)

            # Sleep for a base time + random interval
            sleep_time = self.base_time.get() + random.randint(0, self.random_interval.get())
            time.sleep(sleep_time)

    def stop_script(self):
        if self.is_running:
            self.is_running = False
            self.script_thread.join()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScriptApp(root)
    root.mainloop()
