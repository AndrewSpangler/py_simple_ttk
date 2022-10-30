import tkinter as tk
from tkinter import ttk
from .Labeler import Labeler


class LabeledButton(Labeler, ttk.Button):
    """Labeled Button widget"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        is_child: bool = False,
        command=None,
        **kw,
    ):
        self.is_child = is_child
        self.var = tk.StringVar()
        self.default = None
        if kw.get("text"):
            self.var.set((text := kw.pop("text")))
            if not kw.get("default"):
                self.default = text
        if kw.get("default"):
            self.default = kw.pop("default")
        if self.default is None:
            self.default = ""
        self._command = command
        Labeler.__init__(self, parent, labeltext, header=not is_child, labelside="top")
        ttk.Button.__init__(
            self, self.frame, textvariable=self.var, command=self._on_press, **kw
        )
        ttk.Button.pack(self, fill="both", expand=True, side="left")

    def _on_press(self) -> None:
        """Handle button press"""
        if self._command:
            self._command()

    def set(self, val: str) -> None:
        """Set button text"""
        self.var.set(val)

    def get(self) -> str:
        """Get button text"""
        return self.var.get()

    def clear(self) -> None:
        """Set button text to default"""
        self.set(self.default)
