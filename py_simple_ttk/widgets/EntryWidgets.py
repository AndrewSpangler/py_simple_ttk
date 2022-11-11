#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import (
    askopenfilename,
    askopenfilenames,
    asksaveasfilename,
    askdirectory,
)
from typing import Callable
from .Labeler import Labeler

# from .MultiWidget import MultiWidgetMixin
from .LabeledMultiWidget import LabeledMultiWidgetMixin
from .Scroller import Scroller, _create_container
from .SuperWidget import SuperWidgetMixin
from .WidgetsCore import focus_next, get_asset
from .ToolTip import ToolTip
import sys

class ActiveEntry(ttk.Entry, SuperWidgetMixin):
    """Active ttk.Entry with added features and the SuperWidgetMixin"""

    def __init__(
            self,
            parent: ttk.Frame,
            command: Callable = None,
            default: str = "",
            on_keystroke: bool = False,
            bind_enter: bool = True,
            bind_escape_clear: bool = True,
            widgetargs: dict={},
            **kw
        ):
        self.var = tk.StringVar(value=default)
        ttk.Entry.__init__(self, parent, textvariable=self.var, **kw)
        SuperWidgetMixin.__init__(self, **widgetargs)
        self._command, self.default = command, default
        if on_keystroke:
            self.bind("<KeyRelease>", self._on_execute_command)
        if bind_enter:
            self.bind("<Return>", self._on_execute_command)
        if bind_escape_clear:
            self.bind("<Escape>", self.clear)

    def enable(self) -> None:
        """Enable Entry. `Returns None`"""
        self["state"] = tk.NORMAL

    def disable(self) -> None:
        """Disable Entry. `Returns None`"""
        self["state"] = tk.DISABLED

    def get(self) -> str:
        """Get Entry value. `Returns a String`"""
        return self.var.get()

    def set(self, val) -> None:
        """Set Entry value. `Returns None`"""
        try:
            self.var.set(str(val))
        except:
            raise ValueError("Invaild type supplied.")

    def clear(self) -> None:
        """Set Entry value to default, empty unless default set. `Returns None`"""
        self.var.set(self.default)

    def _on_execute_command(self, event=None) -> None:
        """Calls the provided "command" function with the contents of the Entry. `Returns None`"""
        if self._command:
            self._command(self.get())

class ScrolledEntry(Scroller, ActiveEntry):
    """Scrolled ttk.Entry with SuperWidgetMixin"""

    __desc__ = """This class is here for completeness but most of the time you will \
want to use the ScrolledText widget. Used when you need a scrollable text entry box."""

    @_create_container
    def __init__(self, parent: ttk.Frame, widgetargs: dict = {}, **kw):
        ActiveEntry.__init__(
            self,
            parent,
            **kw,
        )
        Scroller.__init__(self, parent)
        
class LabeledEntry(Labeler, ActiveEntry):
    """Labeled ActiveEntry"""

    __desc__ = """ActiveEntry with Label"""

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
        ActiveEntry.__init__(self, self.frame, **kw)
        ActiveEntry.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        
class LabeledMultiEntry(LabeledMultiWidgetMixin):
    """Labeled MultiWidget LabeledEntry"""

    __desc__ = """Used when you need multiple, vertically stacked Labeled Entries"""

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
            LabeledEntry,
            parent,
            labeltext,
            config,
            is_child,
            labelside,
            **kw,
        )


class LabeledButtonEntry(LabeledEntry):
    """LabeledEntry with a ttk.Button on the right"""

    def __init__(self, *args, button_text="", **kwargs):
        LabeledEntry.__init__(self, *args, **kwargs)
        self.button = ttk.Button(
            self, command=self._on_execute_command, text=button_text
        )
        self.button.pack(expand=False, side=tk.RIGHT)


class LabeledMultiButtonEntry(LabeledMultiWidgetMixin):
    """Labeled MultiWidget Labeled ButtonEntry"""

    __desc__ = """Used when you need multiple, vertically stacked Labeled Entries"""

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
            LabeledButtonEntry,
            parent,
            labeltext,
            config,
            is_child,
            labelside,
            **kw,
        )


class LabeledPathEntry(LabeledEntry):
    """LabeledEntry with a ttk.Button bound to a file- or folder-picker for easy \
    system path selection. Defaults to tk.filedialog.askopenfilename if no \
    tk.filedialog specified."""

    _valid_dialogs = [
        askopenfilename,
        asksaveasfilename,
        askdirectory,
    ]

    def __init__(
        self,
        *args,
        button_text: str = "...",
        dialog=None,
        dialog_args: dict = {},
        **kwargs,
    ):
        LabeledEntry.__init__(self, *args, **kwargs)
        dialog = dialog or tk.filedialog.askopenfilename
        if not dialog in self._valid_dialogs:
            raise ValueError(f"Invalid dialog type supplied")

        def press(*args, **kwargs):
            self.set(dialog(master=self.winfo_toplevel(), **dialog_args))

        self.button = ttk.Button(self, command=press, text=button_text)
        self.button.pack(expand=False, side=tk.RIGHT)


class LabeledMultiPathEntry(LabeledMultiWidgetMixin):
    """Labeled MultiWidget LabeledPathEntry"""

    __desc__ = """Used when you need multiple, vertically stacked LabeledPathEntries"""

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
            LabeledPathEntry,
            parent,
            labeltext,
            config,
            is_child,
            labelside,
            **kw,
        )


class PasswordEntry(ttk.Frame):
    """Username / Password Entry"""

    __desc__ = "A username/password entry widget with optional password peeking. Set password_char \
to `''` to show password by default. The provided command will always be called with the \
tuple `(username_entry.get(), password_entry.get())` as the only argument even if one of the \
entries is disabled."

    def __init__(
        self,
        *args,
        instruction_text: str = "",
        username_text: str = "Username: ",
        username_enabled: bool = True,
        password_text: str = "Password: ",
        password_enabled: bool = True,
        button_text: str = "Submit",
        command=print,
        password_char: str = "*",
        peek_enabled: bool = True,
        invert_peek_colors: bool = False,
        **kwargs,
    ):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.command = command
        if instruction_text:
            t = ttk.Label(self, text=instruction_text).pack(side=tk.TOP)
        self.username_entry = LabeledEntry(self, labeltext=username_text)
        self.username_entry.bind("<Return>", focus_next)
        if username_enabled:
            self.username_entry.pack(side=tk.TOP, anchor="n", fill="x", expand=True)
        f = ttk.Frame(self)
        f.pack(fill="x", expand=True)
        self.password_entry = LabeledEntry(f, labeltext=password_text)
        self.password_entry.configure(show=password_char)
        self.password_entry.bind("<Return>", self._on_submit)
        if password_enabled:
            self.password_entry.pack(side=tk.LEFT, anchor="n", fill="x", expand=True)
            if peek_enabled:
                self.peek = [
                    tk.PhotoImage(file=get_asset("eye_16_black.png")),
                    tk.PhotoImage(file=get_asset("eye_16_white.png")),
                ]
                if invert_peek_colors:
                    self.peek = list(reversed(self.peek))
                self.peek_button = ttk.Button(
                    f,
                    width=0,
                    image=self.peek[0],
                    style="NoPad.TButton",
                )
                self.peek_button.pack(
                    side=tk.RIGHT, expand=False, ipadx=0, ipady=0, padx=0, pady=0
                )
                self.peek_button.bind("<Button-1>", self._on_peek_press)
                self.peek_button.bind("<ButtonRelease-1>", self._on_peek_release)
                ToolTip(self.peek_button, "Peek at password", align=tk.RIGHT)

        ttk.Button(self, text=button_text, command=self._on_submit).pack(
            side=tk.TOP, fill="x", expand=False
        )

    def _on_peek_press(self, event=None) -> None:
        """Show the contents of the password entry while it is being pressed"""
        self.password_entry.configure(show="")
        self.peek_button.configure(image=self.peek[1])

    def _on_peek_release(self, event=None) -> None:
        """Rehide the contents of the password entry"""
        self.password_entry.configure(show="*")
        self.peek_button.configure(image=self.peek[0])

    def _on_submit(self, event=None) -> None:
        """Calls the provided "command" function with the contents of the entry box. `Returns None`"""
        if self.command:
            self.command(self.get())

    def get(self) -> tuple:
        return (self.username_entry.get(), self.password_entry.get())

    def set(self, values: tuple) -> None:
        username, password = values
        self.username_entry.set(username)
        self.password_entry.set(password)


class LabeledPasswordEntry(Labeler, PasswordEntry):
    """Labeled Username/Password entry"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        *args,
        is_child: bool = False,
        **kw,
    ):
        Labeler.__init__(self, parent, labeltext, header=not is_child)
        PasswordEntry.__init__(self, self.frame, *args, **kw)
        PasswordEntry.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        self.is_child = is_child


class LabeledMultiPasswordEntry(LabeledMultiWidgetMixin):
    """Labeled MultiWidget Labeled PasswordEntry"""

    __desc__ = """Used when you need multiple, vertically stacked Labeled Username/Password Entries"""

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
            LabeledPasswordEntry,
            parent,
            labeltext,
            config,
            is_child,
            labelside,
            **kw,
        )
