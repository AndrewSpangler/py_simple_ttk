import tkinter as tk
from tkinter import ttk

from .Labeler import Labeler
from .WidgetsCore import SuperWidgetMixin
from .MultiWidgets import MultiWidgetMixin

from typing import Callable


class LabeledSpinbox(Labeler, ttk.Spinbox, SuperWidgetMixin):
    """Labeled Spinbox with the SuperWidget mixin"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        command: Callable = None,
        default: int = 0,
        on_keystroke: bool = False,
        bind_enter: bool = True,
        bind_escape_clear: bool = True,
        bind_mouse_wheel: bool = True,
        custom_values: bool = True,
        labelside: str = tk.LEFT,
        is_child: bool = False,
        widgetargs={},
        **kw
    ):
        self.var = tk.IntVar(value=default)
        self.default = default
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Spinbox.__init__(self, self.frame, textvariable=self.var, **kw)
        ttk.Spinbox.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        SuperWidgetMixin.__init__(self, **widgetargs)

        self.is_child = is_child
        self._command = command
        self._state = "normal" if custom_values else "readonly"

        if on_keystroke:
            self.bind("<KeyRelease>", self._on_execute_command)
        if bind_enter:
            self.bind("<Return>", self._on_execute_command)
        if bind_escape_clear:
            self.bind("<Escape>", self.clear)
        if bind_mouse_wheel:
            self.bind("<MouseWheel>", self._on_execute_command)

    def disable(self) -> None:
        """Disable Spinbox. `Returns None`"""
        self["state"] = tk.DISABLED

    def enable(self) -> None:
        """Enable Spinbox. `Returns None`"""
        self["state"] = self._state

    def get(self) -> int:
        """Get Spinbox value. `Returns an Int`"""
        return self.var.get()

    def set(self, val: str) -> None:
        """Set Spinbox value. `Returns None`"""
        self.var.set(val)

    def clear(self) -> None:
        """Sets Spinbox to its default value. `Returns None`"""
        self.var.set(self.default)

    def _on_execute_command(self, event=None) -> None:
        """Calls the provided "command" function with the contents of the Entry. `Returns None`"""
        if self._command:
            self._command(self.get())
