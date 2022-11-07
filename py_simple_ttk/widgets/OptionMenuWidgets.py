#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from .Labeler import Labeler
from .LabeledMultiWidget import LabeledMultiWidgetMixin


class LabeledOptionMenu(Labeler, ttk.OptionMenu):
    """Labeled OptionMenu widget"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        options: list,
        default: int = 0,
        is_child: bool = False,
    ):
        self.var = tk.StringVar(value=options[default])
        self.is_child = is_child
        Labeler.__init__(self, parent, labeltext, header=not is_child)
        ttk.OptionMenu.__init__(self, self.frame, self.var, options[default], *options)
        ttk.OptionMenu.pack(self, fill="x", expand=False, side=tk.TOP)
        self.options, self.default = options, default

    def enable(self) -> None:
        """Enable OptionMenu. `Returns None`"""
        self["state"] = tk.NORMAL

    def disable(self) -> None:
        """Disable OptionMenu. `Returns None`"""
        self["state"] = tk.DISABLED

    def get(self) -> str:
        """Get OptionMenu value. `Returns a String`"""
        return self.var.get()

    def set(self, val) -> None:
        """Set OptionMenu value. `Returns None`"""
        self.var.set(val)

    def clear(self) -> None:
        """Sets OptionMenu to its default value. `Returns None`"""
        self.var.set(self.options[self.default])


class LabeledMultiOptionMenu(LabeledMultiWidgetMixin):
    """Labeled MultiWidget LabeledOptionMenu"""

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
            LabeledOptionMenu,
            parent,
            labeltext,
            config,
            is_child,
            labelside,
            **kw,
        )
