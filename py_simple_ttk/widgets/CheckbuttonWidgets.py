#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from .Labeler import Labeler
from .LabeledMultiWidget import LabeledMultiWidgetMixin


class ActiveCheckbutton(ttk.Checkbutton):
    """ttk.Checkbutton with added features"""

    __desc__ = """The "replace_output" keyword argument allows the user to \
provide a tuple of length 2 to replace the default True/False return values."""

    def __init__(
        self,
        parent: ttk.Frame,
        replace_output: list = None,
        default: bool = False,
        **kw,
    ):
        self.var = tk.IntVar(value=default)
        self.default, self.replace_output = default, replace_output
        ttk.Checkbutton.__init__(self, parent, variable=self.var)

    def enable(self) -> None:
        """Enable Checkbutton. `Returns None`"""
        self["state"] = tk.NORMAL

    def disable(self) -> None:
        """Disable Checkbutton. `Returns None`"""
        self["state"] = tk.DISABLED

    def get(self) -> bool:
        """Get Checkbutton value. `Returns a Boolean unless replace_output is set`"""
        return (
            self.replace_output[self.var.get()]
            if not self.replace_output is None
            else self.var.get()
        )

    def set(self, val: bool) -> None:
        """Set Checkbutton value. `Returns None`"""
        self.var.set(val)

    def clear(self) -> None:
        """Sets the Checkbutton to its default value, usually *False* `Returns None`"""
        self.var.set(self.default)


class LabeledCheckbutton(Labeler, ActiveCheckbutton):
    """Labeled Checkbutton"""

    __desc__ = """ActiveCheckbutton with a Label"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str = "",
        is_child: bool = False,
        **kw,
    ):
        self.is_child = is_child
        Labeler.__init__(self, parent, labeltext, header=not is_child)
        ActiveCheckbutton.__init__(self, self.frame, **kw)
        ActiveCheckbutton.pack(self, fill="x", expand=False, side=tk.RIGHT, anchor="w")


class LabeledMultiCheckbutton(LabeledMultiWidgetMixin):
    """Labeled MultiWidget LabeledCheckbutton."""

    __desc__ = (
        """Used when you need multiple, vertically stacked Labeled Checkbuttons"""
    )

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        labelside: str = tk.TOP,
        **kw,
    ):
        LabeledMultiWidgetMixin.__init__(
            self,
            parent,
            labeltext,
            LabeledCheckbutton,
            config,
            labelside=labelside,
            **kw,
        )
