#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from .Labeler import Labeler
from .LabeledMultiWidget import LabeledMultiWidgetMixin


class LabeledRadiobutton(Labeler, ttk.Frame):
    """Labeled Radiobutton widget"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        options: list = [],
        default: int = 0,
        is_child: bool = False,
        **kw,
    ):
        self.var = tk.StringVar()
        self.default = options[default]
        self.var.set(self.default)
        self.is_child = is_child
        Labeler.__init__(self, parent, labeltext, header=not is_child, labelside=tk.TOP)
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.LEFT)
        for o in options:
            b = ttk.Radiobutton(self, text=o, value=o, variable=self.var, **kw)
            b.pack(fill="x", expand=False, side=tk.TOP, padx=(20, 0))

    def enable(self) -> None:
        """Disable Radiobutton. `Returns None`"""
        self["state"] = tk.NORMAL

    def disable(self) -> None:
        """Enable Radiobutton. `Returns None`"""
        self["state"] = tk.DISABLED

    def get(self) -> str:
        """Get Radiobutton value. `Returns a String`"""
        return self.var.get()

    def set(self, val: bool) -> None:
        """Set Radiobutton value. `Returns None`"""
        self.var.set(val)

    def clear(self) -> None:
        """Sets Radiobutton to its default value. `Returns None`"""
        self.var.set(self.default)


class LabeledMultiRadiobutton(LabeledMultiWidgetMixin):
    """Labeled MultiWidget LabeledRadiobutton"""

    __desc__ = """Used when you need multiple, vertically stacked LabeledRadiobuttons"""

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
            LabeledRadiobutton,
            parent,
            labeltext,
            config,
            is_child,
            labelside,
            **kw,
        )
