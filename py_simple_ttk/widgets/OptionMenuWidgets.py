#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from .Labeler import Labeler
from .LabeledMultiWidget import LabeledMultiWidgetMixin
from .SuperWidget import SuperWidgetMixin
from typing import Callable


class ActiveOptionMenu(ttk.OptionMenu, SuperWidgetMixin):
    """ttk.OptionMenu with added features and SuperWidgetMixin"""

    def __init__(
        self,
        parent: ttk.Frame,
        options: list,
        default: int = 0,
        on_keystroke: bool = False,
        bind_enter: bool = True,
        bind_escape_clear: bool = True,
        command: Callable = None,
        widgetargs: dict = {},
    ):
        self.var = tk.StringVar(value=options[default])
        ttk.OptionMenu.__init__(self, parent, self.var, options[default], *options)
        SuperWidgetMixin.__init__(self, **widgetargs)
        self.options, self.default, self._command = options, default, command
        self.var.trace("w", self._on_execute_command)
        if on_keystroke:
            self.bind("<KeyRelease>", self._on_execute_command)
        if bind_enter:
            self.bind("<Return>", self._on_execute_command)
        if bind_escape_clear:
            self.bind("<Escape>", self.clear)

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

    def _on_execute_command(self, *args, **kw) -> None:
        """Handles execution of provided command"""
        if self._command:
            self._command(self.get())


class LabeledOptionMenu(Labeler, ActiveOptionMenu):
    """Labeled ActiveOptionMenu"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        *args,
        is_child: bool = False,
        **kw,
    ):
        self.is_child = is_child
        Labeler.__init__(self, parent, labeltext, header=not is_child)
        ActiveOptionMenu.__init__(self, self.frame, *args, **kw)
        ActiveOptionMenu.pack(self, fill="x", expand=False, side=tk.TOP)


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
            parent,
            labeltext,
            LabeledOptionMenu,
            config,
            is_child,
            labelside,
            **kw,
        )
