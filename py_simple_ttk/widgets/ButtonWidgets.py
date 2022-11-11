import tkinter as tk
from tkinter import ttk
from .Labeler import Labeler
from typing import Callable
from .SuperWidget import SuperWidgetMixin
from .LabeledMultiWidget import LabeledMultiWidgetMixin


class ActiveButton(ttk.Button, SuperWidgetMixin):
    """ttk.Button with added features"""

    def __init__(
        self,
        parent,
        default: str = "",
        command: Callable = None,
        widgetargs: dict = {},
        **kw,
    ):
        self.var = tk.StringVar(value=kw.pop("text") if kw.get("text") else default)
        self.default, self._command = default, command
        ttk.Button.__init__(
            self, parent, textvariable=self.var, command=self._on_press, **kw
        )
        SuperWidgetMixin.__init__(self, **widgetargs)

    def _on_press(self) -> None:
        """Handle button press"""
        if self._command:
            self._command()

    def set(self, val: str) -> None:
        """Set button text"""
        self.var.set(val)

    def get(self) -> str:
        """Get button text"""
        return self.var.get()

    def _on_press(self) -> None:
        """Handle button press"""
        if self._command:
            self._command()

    def clear(self) -> None:
        """Set button text to default"""
        self.set(self.default)


class LabeledButton(Labeler, ActiveButton):
    """Labeled ActiveButton widget"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        command: str = "",
        is_child: bool = False,
        labelside: str = tk.LEFT,
        **kw,
    ):
        self.is_child = is_child
        Labeler.__init__(
            self, parent, labeltext, header=not is_child, labelside=labelside
        )
        ActiveButton.__init__(self, self.frame, default=default, command=command, **kw)
        ActiveButton.pack(self, fill="x", expand=True, side="left")


class LabeledMultiButton(LabeledMultiWidgetMixin):
    """Labeled MultiWidget LabeledButton."""

    __desc__ = (
        """Used when you need multiple, vertically stacked Labeled ActiveButtons"""
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
            LabeledButton,
            parent,
            labeltext,
            config,
            is_child,
            labelside,
            **kw,
        )


class CycleButton(ActiveButton):
    """ActiveButton that cycles through options on each click"""

    def __init__(
        self,
        parent: ttk.Frame,
        options: list,
        default: int = 0,
        command: Callable = None,
        **kw,
    ):
        ActiveButton.__init__(self, parent, command=self._on_cycle, **kw)
        self.options = options
        self.index = default
        self.set(self.options[default])
        self.bind("<KeyRelease>", self._on_cycle)
        self._cycle_command = command

    def _on_cycle(self, event=None):
        self.index += 1
        self.set(self.options[self.index % len(self.options)])
        if self._cycle_command:
            self._cycle_command(self.get())


class LabeledCycleButton(Labeler, CycleButton):
    """Labeled CycleButton widget"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        options: list,
        is_child: bool = False,
        labelside: str = tk.LEFT,
        **kw,
    ):
        self.is_child = is_child
        Labeler.__init__(
            self, parent, labeltext, header=not is_child, labelside=labelside
        )
        CycleButton.__init__(self, self.frame, options, **kw)
        CycleButton.pack(self, fill="x", expand=True, side="left")


class LabeledMultiCycleButton(LabeledMultiWidgetMixin):
    """Labeled MultiWidget LabeledCycleButton"""

    __desc__ = (
        """Used when you need multiple, vertically stacked Labeled CycleButtons"""
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
            LabeledCycleButton,
            parent,
            labeltext,
            config,
            is_child,
            labelside,
            **kw,
        )
