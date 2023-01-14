#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from typing import Callable
from .Labeler import Labeler
from .Scroller import Scroller, _create_container
from .WidgetsCore import default_pack
from .LabeledMultiWidget import LabeledMultiWidgetMixin
from .SuperWidget import SuperWidgetMixin


class ScrolledText(Scroller, tk.Text, SuperWidgetMixin):
    """Scrolled Text with SuperWidget mixin"""

    __desc__ = """Scrolled Text SuperWidget"""

    @_create_container
    def __init__(self, parent, widgetargs: dict = {}, **kw):
        tk.Text.__init__(
            self,
            parent,
            wrap=tk.WORD,
            **kw,
        )
        # Some systems don't bind this automatically
        self.bind("<Control-Key-a>", self.select_all, "+")
        Scroller.__init__(self, parent)
        SuperWidgetMixin.__init__(self, **widgetargs)
        # Create widget proxy
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._event_generate)

    def _event_generate(self, tk_call: str, *args) -> tk.Event:
        """Proxy method to generate an event when text contents change"""
        result = self.tk.call((self._orig, tk_call) + args)
        if tk_call in ("insert", "delete", "replace"):
            self.event_generate("<<Modified>>")
        return result

    def select_all(self, event=None) -> None:
        """Selects all text. `Returns None`"""
        self.tag_add(tk.SEL, "1.0", tk.END)
        self.mark_set(tk.INSERT, "1.0")
        self.see(tk.INSERT)

    def set(self, val: str) -> None:
        """Sets the text. `Returns a String`"""
        state = self["state"]
        self.configure(state=tk.NORMAL)
        self.clear()
        self.insert("1.0", val)
        self.configure(state=state)

    def get(self, start: str = "1.0", end: str = tk.END):
        """Returns the contents of the text box with optional start/end kwargs. `Returns a String`"""
        return tk.Text.get(self, start, end)

    def clear(self) -> None:
        """Empties the text box. `Returns None`"""
        self.delete("1.0", tk.END)

    def get_cursor(self):
        """Get the current location of the cursor. `Returns None`"""
        return tk.Text.index(self, tk.INSERT)

    def set_cursor(self, col: int, row: int) -> None:
        """Sets the cursor to a given col / row. `Returns None`"""
        text_widget_name.mark_set(tk.INSERT, "%d.%d" % (col, row))

    def enable(self) -> None:
        """Enable Text box"""
        self.config(state="normal")

    def disable(self) -> None:
        self.config(state="disable")


class CopyBox(ttk.Frame):
    """Scrolled Text with "Copy to Clipboard" Button"""

    __desc__ = "A widget with a scrolled textbox and button that copies the textbox contents to the user's clipboard. Useful for form output, etc."

    def __init__(self, parent: ttk.Frame, **kw):
        ttk.Frame.__init__(self, parent)
        self.button = ttk.Button(self, text="Copy to Clipboard", command=self._on_click)
        self.button.pack(side=tk.BOTTOM, fill="x", expand=False, pady=(0, 5))
        self.text = ScrolledText(self, **kw)
        self.text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def _on_click(self) -> None:
        self.button.configure(text="Copied!")
        self.clipboard_clear()
        self.clipboard_append(self.get())
        self.after(1000, lambda: self.button.configure(text="Copy To Clipboard"))

    def enable(self) -> None:
        """Enable CopyBox"""
        self.text.enable()

    def disable(self) -> None:
        """Disable CopyBox"""
        self.text.disable()

    def get(self) -> None:
        """Get CopyBox contents"""
        return self.text.get()

    def set(self, val: str) -> None:
        """Set CopyBox Contents"""
        self.text.set(val)

    def clear(self) -> None:
        """Clear CopyBox Contents"""
        self.text.clear()


class LabeledCopyBox(Labeler, CopyBox):
    """Labeled CopyBox widget"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        is_child: bool = False,
        labelside: str = tk.LEFT,
        **kw,
    ):
        self.is_child = is_child
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        CopyBox.__init__(self, self.frame, **kw)
        CopyBox.pack(self, fill="both", expand=True, side="left")


class LabeledMultiCopyBox(LabeledMultiWidgetMixin):
    """Labeled MultiWidget CopyBox."""

    __desc__ = """Used when you need multiple, vertically stacked Labeled CopyBoxes"""

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
            CopyBox,
            config,
            is_child,
            labelside,
            **kw,
        )
