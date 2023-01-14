import platform
import tkinter as tk
from tkinter import ttk
from typing import Callable
from .Labeler import Labeler
from .SuperWidget import SuperWidgetMixin
from .LabeledMultiWidget import LabeledMultiWidgetMixin


class Counter(ttk.Frame):
    """Up / down counter widgets"""

    def __init__(
        self,
        parent: ttk.Frame,
        default: int = 0,
        min_value: int = None,
        max_value: int = None,
        step: int = 1,
        state: str = "normal",
        command: Callable = None,
        depth: int = 1,
        **kwargs,
    ):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.min_value, self.max_value = min_value, max_value
        self.default, self.step = default, step
        self._state, self.command = state, command
        self.var = tk.IntVar()
        self.set(default, no_command=True)
        self.buttons = []
        if not depth or depth < 1:
            raise ValueError("Counter depth cannot be less than 1")
        for i in reversed(range(depth)):
            self.buttons.append(
                ttk.Button(
                    self,
                    text="<" * (i + 1),
                    command=lambda i=i: self._dec(10**i),
                    width=i + 1.1,
                )
            )
        self.buttons.append(l := ttk.Label(self, textvariable=self.var))
        for i in range(depth):
            self.buttons.append(
                ttk.Button(
                    self,
                    text=">" * (i + 1),
                    command=lambda i=i: self._inc(10**i),
                    width=i + 1.1,
                )
            )
        self.get = self.var.get
        self._handle_state()
        for b in self.buttons:
            b.pack(side="left", ipadx=0, padx=0)
            b.bind("<MouseWheel>", self._on_mousewheel)
        self.buttons.remove(l)

    def set(self, val: int, adjust: int = 0, no_command: bool = False) -> int:
        if not self._state == "normal":
            return
        val = int(val) + adjust
        if not self.max_value is None:
            val = min(val, self.max_value)
        if not self.min_value is None:
            val = max(val, self.min_value)
        self.var.set(val)
        if not no_command:
            if self.command:
                self.command(val)
        return val

    def _inc(self, amount: int = 1) -> int:
        # self.set(val := int(self.get()) + amount)
        return self.set(self.get(), amount)

    def _dec(self, amount: int = 1) -> int:
        return self.set(self.get(), -amount)

    def clear(self) -> int:
        return self.set(self.default)

    def enable(self) -> None:
        self._state = "normal"
        self._handle_state()

    def disable(self) -> None:
        self._state = "disable"
        self._handle_state()

    def _handle_state(self) -> None:
        for b in self.buttons:
            b.configure(state=self._state)

    def _on_mousewheel(self, event=None) -> None:
        if platform.system() in ["Windows", "Darwin"]:
            self._inc(self.step) if event.delta > 1 else self._dec(self.step)
        else:
            self._inc(self.step) if event.num == 4 else self._dec(self.step)


class LabeledCounter(Labeler, Counter, SuperWidgetMixin):
    """Labeled Counter Widget"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        command: Callable = None,
        labelside: str = tk.LEFT,
        is_child: bool = False,
        state: str = "normal",
        widgetargs: dict = {},
        **kw,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        Counter.__init__(self, self.frame, command=command, **kw)
        Counter.pack(self, side="right", expand=False)
        SuperWidgetMixin.__init__(self, **widgetargs)
        self.is_child = is_child


class LabeledMultiCounter(LabeledMultiWidgetMixin):
    """Labeled MultiWidget LabeledCounter."""

    __desc__ = """Used when you need multiple, vertically stacked Labeled Counters"""

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
            LabeledCounter,
            config,
            is_child,
            labelside,
            **kw,
        )


class FloatCounter(ttk.Frame):
    """Float Counter Widget"""

    def __init__(
        self,
        parent=ttk.Frame,
        default: float = 0.0,
        min_value: float = None,
        max_value: float = None,
        step: float = 1.0,
        state: str = "normal",
        command: Callable = None,
        decimal_level: int = 1,
        integer_level: int = 1,
        **kwargs,
    ):
        ttk.Frame.__init__(self, parent, **kwargs)
        self.var = tk.StringVar(value=default)
        self._val = default
        self.decimal_level = decimal_level
        buttons = []

        for i in reversed(range(integer_level)):
            buttons.append(
                ttk.Button(
                    self,
                    text="<" * (i + 1),
                    command=lambda i=i: self._dec(float(10**i)),
                    width=i + 2,
                )
            )

        for i in range(decimal_level):
            print(0.1 ** (i))
            buttons.append(
                ttk.Button(
                    self,
                    text="." * (i + 1),
                    command=lambda i=i: self._dec(0.1 ** (i + 1)),
                    width=i + 2,
                )
            )

        buttons.append(l := ttk.Label(self, textvariable=self.var))

        for i in reversed(range(decimal_level)):
            buttons.append(
                ttk.Button(
                    self,
                    text="." * (i + 1),
                    command=lambda i=i: self._inc(0.1 ** (i + 1)),
                    width=i + 2,
                )
            )

        for i in range(integer_level):
            buttons.append(
                ttk.Button(
                    self,
                    text=">" * (i + 1),
                    command=lambda i=i: self._inc(float(10**i)),
                    width=i + 2,
                )
            )

        self.state, self.command, self.buttons = state, command, buttons
        self.default, self.step = default, step
        self.min_value, self.max_value = min_value, max_value
        self._handle_state()
        for b in self.buttons:
            b.pack(side="left")
            b.bind("<MouseWheel>", self._on_mousewheel)
        self.buttons.remove(l)

    def get(self) -> float:
        return self._val

    def set(self, val: float, adjust: float = 0.0) -> float:
        if not self.state == "normal":
            return
        val = float(val) + adjust
        if not self.min_value is None:
            val = max(val, min_value)
        if not self.max_value is None:
            val = min(val, max_value)
        # Fix float bug
        fmt = "{:." + str(self.decimal_level) + "f}"
        self._val = float(fmt.format(val))
        self.var.set(str(self._val))
        if self.command:
            self.command(val)
        return val

    def _inc(self, amount: float = 1) -> float:
        return self.set(self._val, amount)

    def _dec(self, amount: float = 1) -> float:
        return self.set(self._val, -amount)

    def clear(self) -> float:
        return self.set(self.default)

    def enable(self) -> None:
        self.state = "normal"
        self._handle_state()

    def disable(self) -> None:
        self.state = "disable"
        self._handle_state()

    def _handle_state(self) -> None:
        for b in self.buttons:
            b.configure(state=self.state)

    def _on_mousewheel(self, event=None) -> None:
        if platform.system() in ["Windows", "Darwin"]:
            self._inc(self.step) if event.delta > 1 else self._dec(self.step)
        else:
            self._inc(self.step) if event.num == 4 else self._dec(self.step)


class LabeledFloatCounter(Labeler, FloatCounter, SuperWidgetMixin):
    """Labeled Float Counter Widget"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        command: Callable = None,
        labelside: str = tk.LEFT,
        is_child: bool = False,
        state: str = "normal",
        widgetargs: dict = {},
        **kw,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        FloatCounter.__init__(self, self.frame, command=command, **kw)
        FloatCounter.pack(self, side="right", expand=False)
        SuperWidgetMixin.__init__(self, **widgetargs)
        self.is_child = is_child


class LabeledMultiFloatCounter(LabeledMultiWidgetMixin):
    """Labeled MultiWidget Labeled FloatCounter."""

    __desc__ = (
        """Used when you need multiple, vertically stacked Labeled FloatCounters"""
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
            LabeledFloatCounter,
            config,
            is_child,
            labelside,
            **kw,
        )
