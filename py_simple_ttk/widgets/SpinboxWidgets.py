import tkinter as tk
from tkinter import ttk

from .Labeler import Labeler
from .SuperWidget import SuperWidgetMixin
from .LabeledMultiWidget import LabeledMultiWidgetMixin

from typing import Callable


class ActiveSpinbox(ttk.Spinbox, SuperWidgetMixin):
    """Spinbox with added features"""

    def __init__(
        self,
        parent: ttk.Frame,
        command: Callable = None,
        default: int = 0,
        on_keystroke: bool = False,
        bind_enter: bool = True,
        bind_escape_clear: bool = True,
        bind_mouse_wheel: bool = True,
        custom_values: bool = True,
        widgetargs: dict = {},
        **kw,
    ):
        self.var = tk.IntVar()
        self.default = default
        # self.from_ = kw.get("from_")
        # self.to = kw.get("to")
        ttk.Spinbox.__init__(self, parent, textvariable=self.var, **kw)
        ttk.Spinbox.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        SuperWidgetMixin.__init__(self, **widgetargs)
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
        self.set(default)

    def disable(self) -> None:
        """Disable Spinbox. `Returns None`"""
        self["state"] = tk.DISABLED

    def enable(self) -> None:
        """Enable Spinbox. `Returns None`"""
        self["state"] = self._state

    def get(self) -> int:
        """Get Spinbox value. `Returns an Int`"""
        return self.var.get()

    def set(self, val: int) -> None:
        """Set Spinbox value. `Returns None`"""
        self.var.set(max(min(val, self.cget("to")), self.cget("from")))

    def clear(self) -> None:
        """Sets Spinbox to its default value. `Returns None`"""
        self.var.set(self.default)

    def _on_execute_command(self, event=None) -> None:
        """Calls the provided "command" function with the contents of the Entry. `Returns None`"""
        if self._command:
            self._command(self.get())


class LabeledSpinbox(Labeler, ActiveSpinbox):
    """Labeled Spinbox with the SuperWidget mixin"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        labelside: str = tk.LEFT,
        is_child: bool = False,
        **kw,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        self.is_child = is_child
        ActiveSpinbox.__init__(self, self.frame, **kw)
        ActiveSpinbox.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)


class LabeledMultiSpinbox(LabeledMultiWidgetMixin):
    """Labeled MultiWidget Spinbox."""

    __desc__ = """Used when you need multiple, vertically stacked Labeled Spinboxes"""

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
            LabeledSpinbox,
            config,
            is_child,
            labelside,
            **kw,
        )
