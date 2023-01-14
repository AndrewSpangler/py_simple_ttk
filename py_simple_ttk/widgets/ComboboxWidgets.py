import tkinter as tk
from tkinter import ttk
from .Labeler import Labeler
from .LabeledMultiWidget import LabeledMultiWidgetMixin
from .SuperWidget import SuperWidgetMixin
from typing import Callable


class ActiveCombobox(ttk.Combobox, SuperWidgetMixin):
    """ttk.Combobox with added features and the SuperWidgetMixin"""

    def __init__(
        self,
        parent: ttk.Frame,
        command: Callable = None,
        default: int = 0,
        on_keystroke: bool = False,
        bind_enter: bool = True,
        bind_escape_clear: bool = True,
        values: list = (),
        custom_values: bool = True,
        widgetargs: dict = {},
        **kw,
    ):
        self._state = "normal" if custom_values else "readonly"
        self.default = values[default] if any(values) else ""
        self.var = tk.StringVar(value=self.default)
        ttk.Combobox.__init__(self, parent, textvariable=self.var, **kw)
        SuperWidgetMixin.__init__(self, **widgetargs)
        self._command, self["values"] = command, values
        if on_keystroke:
            self.bind("<KeyRelease>", self._on_execute_command)
        if bind_enter:
            self.bind("<Return>", self._on_execute_command)
        if bind_escape_clear:
            self.bind("<Escape>", self.clear())

    def disable(self) -> None:
        """Disable Combobox. `Returns None`"""
        self["state"] = tk.DISABLED

    def enable(self) -> None:
        """Enable Combobox. `Returns None`"""
        self["state"] = self._state

    def get(self) -> str:
        """Get Combobox value. `Returns a String`"""
        return self.var.get()

    def set(self, val: str) -> None:
        """Set Combobox value. `Returns None`"""
        self.var.set(val)

    def clear(self) -> None:
        """Sets Combobox to its default value. `Returns None`"""
        self.var.set(self.default)

    def _on_execute_command(self, event=None) -> None:
        """Calls the provided "command" function with the contents of the Entry. `Returns None`"""
        if self._command:
            self._command(self.get())


class LabeledCombobox(Labeler, ActiveCombobox):
    """Labeled Combobox with the Super Widget mixin"""

    __desc__ = """Set custom_values keyword to "False" to disable custom user-entered values. Set the "default" keyword to the index of the value to display by default from the "values" keyword."""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        labelside: str = tk.LEFT,
        is_child: bool = False,
        widgetargs={},
        **kw,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ActiveCombobox.__init__(self, self.frame, **kw)
        ActiveCombobox.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        self.is_child = is_child


class LabeledMultiCombobox(LabeledMultiWidgetMixin):
    """Labeled MultiWidget LabeledCombobox."""

    __desc__ = """Used when you need mutiple, vertically stacked Labeled Comboboxes"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside: str = tk.TOP,
        **kw,
    ):
        LabeledMultiWidgetMixin.__init__(
            self,
            parent,
            labeltext,
            LabeledCombobox,
            config,
            is_child,
            labelside,
            **kw,
        )
