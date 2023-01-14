#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from .Labeler import Labeler
from .LabeledMultiWidget import LabeledMultiWidgetMixin
from .SuperWidget import SuperWidgetMixin
from .FrameWidgets import ColumnFrame


class ActiveRadiobutton(ttk.Radiobutton, SuperWidgetMixin):
    """ttk.Radiobutton with added features and the SuperWidgetMixin"""

    def __init__(
        self,
        parent: ttk.Frame,
        text: str,
        value: str,
        variable: tk.StringVar | tk.IntVar | tk.DoubleVar,
        widgetargs: dict = {},
        **kw,
    ):
        self.var, self.value = variable, value
        ttk.Radiobutton.__init__(
            self, parent, text=text, value=value, variable=variable, **kw
        )
        SuperWidgetMixin.__init__(self, **widgetargs)

    def get(self) -> bool:
        """`Returns a bool if the button is clicked`"""
        return self.state["selected"]

    def set(
        self,
        val: str | int | float,
    ) -> None:
        """Set value, input type varies base on tk variable type. `Returns None`"""
        self.configure(value=val)

    def enable(self) -> None:
        self.configure(state=tk.NORMAL)

    def disable(self) -> None:
        self.configure(state=tk.DISABLED)


class RadioTable(ttk.Frame):
    """A table of ttk.RadioButtons"""

    """Takes an itterable of options in the form `((text1, value1), (text2, value2), ...)`"""

    def __init__(
        self,
        parent: ttk.Frame,
        options: tuple,
        default: int = 0,
        variable_type: type = tk.StringVar,
        state: str = tk.NORMAL,
        columns: int = 1,
        pack_args: dict = {},
        **kw,
    ):
        self.options = options = list(options)
        self.values = [v for t, v in options]
        self.default = self.values[default] if any(self.values) else None
        self.var = tk.StringVar(value=self.default)
        ttk.Frame.__init__(self, parent, **kw)
        (args := {"fill": "x", "expand": False, "side": "top"}).update(pack_args)
        self.buttons = []
        if not columns == 1:
            self.frames = ColumnFrame(self, columns)
        for t, v in options:
            frame = self if columns == 1 else self.frames.yield_frame()
            self.buttons.append(
                b := ttk.Radiobutton(frame, text=t, value=v, variable=self.var)
            )
            b.pack(**args)
        self._state = state
        self._handle_state()

    def enable(self) -> None:
        """Disable Radiobutton. `Returns None`"""
        self._state = tk.NORMAL
        self._handle_state()

    def disable(self) -> None:
        """Enable Radiobutton. `Returns None`"""
        self._state = tk.DISABLED
        self._handle_state()

    def get(self) -> str:
        """Get Radiobutton value. `Returns a String`"""
        return self.var.get()

    def set(self, val: str) -> None:
        """Set Radiobutton value. `Returns None`"""
        self.var.set(val)
        print(val)
        index = self.values.index(val)
        print(self.buttons[index].state)
        self.buttons[index].state["selected"] = True

    def clear(self) -> None:
        """Sets Radiobutton to its default value. `Returns None`"""
        self.var.set(self.default)

    def _handle_state(self) -> None:
        """Propagates current state to children buttons. `Returns None`"""
        for b in self.buttons:
            b.configure(state=self._state)


class LabeledRadioTable(Labeler, RadioTable):
    """Labeled RadioTable widget"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        is_child: bool = False,
        labelside: str = tk.TOP,
        **kw,
    ):
        self.is_child = is_child
        Labeler.__init__(
            self, parent, labeltext, header=not is_child, labelside=labelside
        )
        RadioTable.__init__(self, self.frame, **kw)
        RadioTable.pack(self, fill=tk.BOTH, expand=True, side=tk.LEFT)


class LabeledMultiRadioTable(LabeledMultiWidgetMixin):
    """Labeled MultiWidget LabeledRadioTable"""

    __desc__ = """Used when you need multiple, vertically stacked LabeledRadioTables"""

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
            LabeledRadioTable,
            config,
            is_child,
            labelside,
            **kw,
        )


class SimpleRadioTable(RadioTable):
    """A simplified RadioTable where the text is used at the value."""

    __desc__ = """Uses a tk.StringVar variable type only. Takes a tuple in the form `(value1, value2, ...)`"""

    def __init__(self, parent: ttk.Frame, options: tuple, **kw):
        if kw.get("variable_type") and not kw.get("variable_type") is tk.StringVar:
            raise ValueError("SimpleRadioTable variable type must be tk.StringVar")
        RadioTable.__init__(self, parent, options=((o, o) for o in options), **kw)


class LabeledSimpleRadioTable(Labeler, SimpleRadioTable):
    """Labeled SimpleRadioTable widget"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        options: list,
        is_child: bool = False,
        labelside: str = tk.TOP,
        **kw,
    ):
        Labeler.__init__(
            self, parent, labeltext, header=not is_child, labelside=labelside
        )
        SimpleRadioTable.__init__(self, self.frame, options, **kw)
        SimpleRadioTable.pack(self, fill=tk.BOTH, expand=True, side=tk.LEFT)


class LabeledMultiSimpleRadioTable(LabeledMultiWidgetMixin):
    """Labeled MultiWidget LabeledSimpleRadioTable"""

    __desc__ = (
        """Used when you need multiple, vertically stacked LabeledSimpleRadioTables"""
    )

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
            LabeledSimpleRadioTable,
            config,
            is_child,
            labelside,
            **kw,
        )
