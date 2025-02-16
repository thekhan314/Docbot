import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow modules

def show_result(answer):
    result_window = tk.Toplevel()  # Use Toplevel for new windows
    result_window.title("Result")

    if answer == "yes":
        label = tk.Label(result_window, text="Hahaha, you are a fat monkey!")
        label.pack(padx=10, pady=10)

        # Load and display the image
        image_path = "/home/ukhan/Docbot/assets/fatmonkey.jpg"
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        img_label = tk.Label(result_window, image=img)
        img_label.image = img
        img_label.pack(padx=10, pady=10)

    else:
        label = tk.Label(result_window, text="Are you sure? You look like a fat monkey.")
        label.pack(padx=10, pady=10)

# ... (rest of the code remains the same)


def ask_question():
    question_window = tk.Tk()
    question_window.title("Monkey Question")

    label = tk.Label(question_window, text="Are you a fat monkey?")
    label.pack(padx=10, pady=10)

    yes_button = tk.Button(question_window, text="Yes", command=lambda: show_result("yes"))
    yes_button.pack(side="left", padx=5)

    no_button = tk.Button(question_window, text="No", command=lambda: show_result("no"))
    no_button.pack(side="right", padx=5)

    question_window.mainloop()

# Initial window
root = tk.Tk()
root.title("Monkey Quiz")

start_button = tk.Button(root, text="Start", command=ask_question)
start_button.pack(pady=20)

root.mainloop()

root = tk.Tk()
root.title("Monkey Quiz")

start_button = tk.Button(root, text="Start", command=ask_question)
start_button.pack(pady=20)

root.mainloop()

