#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from .Labeler import Labeler
from .MultiWidget import MultiWidgetMixin
from .SuperWidget import SuperWidgetMixin
from typing import Callable


class ActiveScale(ttk.Scale, SuperWidgetMixin):
    """ttk.Scale with added features and the SuperWidget mixin"""

    def __init__(
        self,
        parent: ttk.Frame,
        command: Callable = None,
        default: float = 0,
        widgetargs: dict = {},
        **kw,
    ):
        self.default, self._command = float(default), command
        self.var = tk.DoubleVar(value=self.default)
        ttk.Scale.__init__(
            self, parent, variable=self.var, command=self._on_execute_command, **kw
        )
        SuperWidgetMixin.__init__(self, **widgetargs)

    def enable(self) -> None:
        """Disable Scale. `Returns None`"""
        self["state"] = tk.NORMAL

    def disable(self) -> None:
        """Enable Scale. `Returns None`"""
        self["state"] = tk.DISABLED

    def get(self) -> float:
        """Get Scale value. `Returns a Float`"""
        return self.var.get()

    def set(self, val: float) -> None:
        """Set Scale value. `Returns None`"""
        self.var.set(val)

    def clear(self) -> None:
        """Sets Scale to its default value. `Returns None`"""
        self.var.set(self.default)

    def _on_execute_command(self, val: float) -> None:
        if self._command:
            self._command(val)


class LabeledScale(Labeler, ActiveScale):
    """Labeled ActiveScale"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        command: Callable = None,
        orient: bool = tk.HORIZONTAL,
        is_child: bool = False,
        labelside: str = tk.LEFT,
        **kw,
    ):
        if not orient in (tk.HORIZONTAL, tk.VERTICAL):
            raise ValueError(f"Unknown orientation - {orient}")
        pack_args = {"fill": "x", "expand": True, "side": tk.TOP}
        if orient == tk.VERTICAL:
            labelside = tk.TOP
            pack_args.update({"fill": "y"})
        kw["orient"] = orient
        self.is_child = is_child
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ActiveScale.__init__(self, self.frame, **kw)
        ActiveScale.pack(self, **pack_args)


class LabeledMultiScale(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Scale"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
        orient=tk.HORIZONTAL,
        command=None,
    ):
        self.orient = orient
        self.is_child = is_child
        self._command = command
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledScale, config)

    def _on_command(self, key) -> Callable:
        def do_command(val):
            if self._command:
                return self._command({key: val})

        return do_command

    def add(
        self,
        parent: ttk.Frame,
        key: str,
        args: list,
        kwargs: dict,
        widget_type: type = None,
    ) -> object:

        """Override MultiWidgetMixin for vertical orientation"""
        widget_type = widget_type or self.widget_type
        kwargs["orient"] = self.orient
        w = widget_type(parent, key, *args, command=self._on_command(key), **kwargs)
        if self.orient == tk.HORIZONTAL:
            w.pack(fill="x", expand=False, side=tk.TOP, padx=(20, 0))
        elif self.orient == tk.VERTICAL:
            w.pack(fill="y", expand=True, side=tk.LEFT)
        else:
            raise ValueError(f"Bad orientation - {self.orient}")
        self.widgets[key] = w
        return w
