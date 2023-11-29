import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Hello DIP01", font=('Arial', 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="1", height=4)
        self.button.place(x=1, y=50)

        self.button = tk.Button(self.root, text="2", height=4)
        self.button.place(x=20, y=50)

        self.button = tk.Button(self.root, text="3", height=4)
        self.button.place(x=40, y=50)

        self.button = tk.Button(self.root, text="4", height=4)
        self.button.place(x=60, y=50)

        self.button = tk.Button(self.root, text="5", height=4)
        self.button.place(x=80, y=50)

        self.button = tk.Button(self.root, text="6", height=4)
        self.button.place(x=100, y=50)

        self.button = tk.Button(self.root, text="7", height=4)
        self.button.place(x=120, y=50)

        self.button = tk.Button(self.root, text="8", height=4)
        self.button.place(x=140, y=50)

        self.button = tk.Button(self.root, text="9", height=4)
        self.button.place(x=160, y=50)

        self.root.mainloop()

MyCalculator()