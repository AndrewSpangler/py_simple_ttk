import tkinter as tk
from tkinter import ttk
from typing import Callable
from .SuperWidget import SuperWidgetMixin


class ActiveLabel(ttk.Label, SuperWidgetMixin):
    """Active ttk.Entry with added features and the SuperWidgetMixin"""

    def __init__(
        self,
        parent: ttk.Frame,
        command: Callable = None,
        default: str = "",
        widgetargs: dict = {},
        **kw
    ):
        self.var = tk.StringVar(value=default)
        ttk.Label.__init__(self, parent, textvariable=self.var, **kw)
        SuperWidgetMixin.__init__(self, **widgetargs)
        self._command, self.default = command, default
        self._state = tk.NORMAL
        self.bind("<ButtonRelease-1>", self._on_execute_command)

    def enable(self) -> None:
        """Enable label updates. `Returns None`"""
        self._state = tk.NORMAL

    def disable(self) -> None:
        """Disable label updates. `Returns None`"""
        self._state = tk.DISABLED

    def get(self) -> str:
        """Get label value. `Returns a String`"""
        return self.var.get()

    def set(self, val) -> None:
        """Set label value. `Returns None`"""
        try:
            self.var.set(str(val))
        except:
            raise ValueError("Invaild type supplied.")

    def clear(self) -> None:
        """Set label value to default, empty unless default set. `Returns None`"""
        self.var.set(self.default)

    def _on_execute_command(self, event=None) -> None:
        """Calls the provided "command" function with the contents of the Entry. `Returns None`"""
        if self._command:
            self._command(self.get())


class LabeledValue(ttk.Frame):
    """A pair of ActiveLabels in a frame acting as a label and value pair with the label in bold"""

    def __init__(
        self,
        parent: ttk.Frame,
        label_text: str = None,
        value_text: str = None,
        label_config: dict = {},
        value_config: dict = {},
        *args,
        **kwargs
    ):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.label = ActiveLabel(
            self, default=label_text, style="Bold.TLabel", **label_config
        )
        self.label.pack(side="left")
        self.value = ActiveLabel(self, default=value_text, **value_config)
        self.value.pack(side="right")

    def get(self) -> str:
        """Returns the label's and value's texts separated by a space. `Returns a String`"""
        return self.label.get() + " " + self.value.get()

    def set(self, val: tuple):
        """Set the label and value from two text strings in a tuple like ("label:", "value"). `Returns None`"""
        label, value = val
        self.label.set(label)
        self.value.set(value)
