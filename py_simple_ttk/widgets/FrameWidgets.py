import tkinter as tk
from tkinter import ttk


class ColumnFrame(ttk.Frame):
    """A frame with a given number of children column frames"""

    def __init__(self, parent: ttk.Frame, columns: int = 1, pack_args: dict = {}, **kw):
        ttk.Frame.__init__(self, parent, **kw)
        (args := {"side": "left", "fill": "both", "expand": True}).update(pack_args)
        self.columns, self.frames, self.index = columns, [], 0
        for i in range(columns):
            self.frames.append(f := ttk.Frame(self))
            f.pack(**args)

    def yield_frame(self):
        """Cyclically returns frames"""
        self.index += 1
        return self.frames[(self.index - 1) % len(self.frames)]
