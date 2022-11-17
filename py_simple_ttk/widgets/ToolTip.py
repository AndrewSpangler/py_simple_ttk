# Based on https://github.com/roseman/idle/blob/master/ToolTip.py
# Modified to for use with ttk theming
import tkinter as tk
from tkinter import ttk
from .TextWidgets import ScrolledText


class ToolTipBase:
    def __init__(self, parent: object, align: str = tk.LEFT):
        self.parent, self.align = parent, align
        self.x = self.y = 0
        self.parent.bind("<Enter>", self._enter)
        self.parent.bind("<Leave>", self._leave)
        self.parent.bind("<ButtonPress>", self._leave)
        self._id, self._tipwindow = None, None

    def _enter(self, event=None) -> None:
        self._schedule()

    def _leave(self, event=None) -> None:
        self._unschedule()
        self._hidetip()

    def _schedule(self) -> None:
        self._unschedule()
        self._id = self.parent.after(10, self._showtip)

    def _unschedule(self):
        _id = self._id
        self._id = None
        if _id:
            self.parent.after_cancel(_id)

    def _showtip(self) -> None:
        if self._tipwindow:
            return
        self._tipwindow = tk.Toplevel(self.parent)
        self._tipwindow.wm_overrideredirect(1)
        self._showcontents()
        self._tipwindow.update_idletasks()

        x = self.parent.winfo_rootx()
        y = self.parent.winfo_rooty() + self.parent.winfo_height() + 1

        if self.align == tk.LEFT:
            pass
        elif self.align == tk.RIGHT:
            x += self.parent.winfo_width() - self._tipwindow.winfo_width()
        else:
            raise ValueError(f"Unsupported ToolTip alignment {self.align}")
        self._tipwindow.wm_geometry("+%d+%d" % (x, y))

    def _showcontents(self, text: str = "") -> None:
        ttk.Label(self._tipwindow, text=text, borderwidth=2, relief=tk.SOLID).pack()

    def _hidetip(self) -> None:
        tw = self._tipwindow
        self._tipwindow = None
        if tw:
            tw.destroy()


class ToolTip(ToolTipBase):
    """Easy ToolTip"""

    __desc__ = """Easily show theme-friendly tooltip. Currently only left and right align are supported."""

    def __init__(self, parent: object, text: str, align: str = tk.LEFT):
        ToolTipBase.__init__(self, parent, align)
        self.text = text

    def _showcontents(self) -> None:
        ToolTipBase._showcontents(self, self.text)
