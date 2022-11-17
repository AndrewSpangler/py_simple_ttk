import tkinter as tk
from tkinter import ttk
from collections.abc import Iterable
from .WidgetsCore import get_asset


class ColumnFrame(ttk.Frame):
    """A frame with a given number of children column ttk.Frames"""

    __desc__ = """Takes a number of columns or a list of names when the `labeled` keyword is set to True"""

    def __init__(
        self,
        parent: ttk.Frame,
        columns: int | list = 1,
        labeled=False,
        pack_args: dict = {},
        **kw,
    ):
        ttk.Frame.__init__(self, parent, **kw)
        (args := {"side": "left", "fill": "both", "expand": True}).update(pack_args)
        self.columns, self.frames, self.index = columns, [], 0
        if labeled:
            for n in columns:
                self.frames.append(
                    f := ttk.LabelFrame(self, text=n, style="LargeBold.TLabelframe")
                )
                f.pack(**args)
        else:
            for i in range(columns):
                self.frames.append(f := ttk.Frame(self))
                f.pack(**args)

    def yield_frame(self):
        """Cyclically returns frames"""
        self.index += 1
        yield self.frames[(self.index - 1) % len(self.frames)]


class HamburgerFrame(ttk.Frame):
    """A ttk.Frame with a Hamburger Menu and supporting widgets"""

    __desc__ = """Options is an iterable in the form ((label, callback), (label2, callback2), ...). See examples/hamburger_demo.py for usage."""

    def __init__(
        self,
        parent: ttk.Frame,
        options: Iterable,
        menu_width: int = 300,
        column_style="Hamburger.TFrame",
        **kw,
    ):
        ttk.Frame.__init__(self, parent, **kw)
        self._parent = parent
        self._state, self._menu = False, None
        self.options = list(options)
        self.width, self._style = (menu_width, column_style)
        self.icon = tk.PhotoImage(file=get_asset("lines_16_gray.png"), format="PNG")
        self.header = ttk.Frame(self)
        self.header.pack(fill="x", side="top", anchor="w")
        self.button = ttk.Button(
            self.header, image=self.icon, command=self._toggle, width=0
        )
        self.button.pack(side="top", anchor="w", padx=5, pady=(5, 0))
        self.body = ttk.Frame(self)
        self.body.pack(fill="both", expand=True, side="top")

    def open(self, event=None) -> None:
        """Opens the menu. `Returns None`"""
        if self._menu:
            self._menu.destroy()
        self._menu = ttk.Frame(self._parent, style=self._style)
        self._menu.place(x=0, y=0, width=self.width, relheight=1)
        close_button = ttk.Button(
            self._menu,
            image=self.icon,
            command=lambda: self._toggle(state=False),
            width=3,
        )
        close_button.pack(side="top", anchor="w", padx=5, pady=(5, 0))
        close_button.focus_set()
        for opt, callback in self.options:
            ttk.Button(self._menu, text=opt, command=callback).pack(
                side="top", fill="x", padx=5
            )
        self._menu.bind("<Leave>", self.close)

    def close(self, event=None) -> None:
        """Closes the menu. `Returns None`"""
        if self._menu:
            self._menu.destroy()
        self.button.focus_set()
        self._state = False

    def _toggle(self, event=None, state=None) -> None:
        self._state = not self._state if state is None else state
        [self.close, self.open][self._state]()
