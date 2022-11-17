import tkinter as tk
from tkinter import ttk
from py_simple_ttk import App, Tab, HamburgerFrame


class HamburgerDemo(App):
    def __init__(self):
        App.__init__(self, "hamburger_demo.json")
        self.notebook.pack_forget()
        label_var = tk.StringVar(value="Select A Food")
        conf = ("Pizza", "Hot Dog", "Fries", "Chicken Nuggets", "Spaghetti")
        conf = ((t, lambda t=t: label_var.set(t)) for t in conf)
        (frame := HamburgerFrame(self.window, conf)).pack(fill="both", expand=True)
        ttk.Label(frame.body, textvariable=label_var, style="LargeBold.TLabel").pack(
            expand=True, anchor="center"
        )


if __name__ == "__main__":
    HamburgerDemo().mainloop()
