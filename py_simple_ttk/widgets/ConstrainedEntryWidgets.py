import tkinter as tk
from tkinter import ttk
import string
from typing import Callable
from .Labeler import Labeler
from .WidgetsCore import SuperWidgetMixin
from .MultiWidget import MultiWidgetMixin

# Type-constrained
def check_entry_type(val: str, typ: type) -> bool:
    """Core type checker function. Limits entry to chars that construct a given type"""
    if not len(val):
        return True
    try:
        typ(val)
        return True
    except:
        return False


# Contents-constrained
def check_entry_contents(val: str, limiter: list) -> bool:
    """Core content checker function. Limits entry to a list of chars ['a', 'b', 'c', ...] or \
    the chars contained in a simple string 'abc...'"""
    for char in val:
        if not char in limiter:
            return False
    return True


class ConstrainedEntry(ttk.Frame):
    """An Entry widget that allows certain constraints to be placed on the input with a given check_function that returns true if the input is allowed for each keystroke / input."""

    def __init__(
        self,
        parent,
        check_function,
        return_type: type = str,
        default: str = "",
        widgetargs={},
        **kwargs,
    ):
        ttk.Frame.__init__(self, parent)
        self.var = tk.StringVar()
        self.var.trace("w", self._validate)
        self.default = default
        if self.default:
            self.set(default)
        self.entry = ttk.Entry(self, textvariable=self.var, **kwargs)
        self.entry.pack(fill="x", expand=True)
        self.check_function, self.return_type = check_function, return_type
        self.last = ""

    def _validate(self, *args, **kwargs) -> bool:
        val = self.var.get()
        if self.check_function(val):
            self.last = val
        else:
            self.var.set(self.last)

    def get(self) -> object:
        return self.return_type(self.var.get())

    def set(self, val) -> None:
        try:
            self.var.set(str(val))
        except:
            raise ValueError("Invaild type supplied.")

    def clear(self):
        """Set Entry value to default, empty unless default set. `Returns None`"""
        self.var.set(self.default)


class LabeledConstrainedEntry(Labeler, ConstrainedEntry, SuperWidgetMixin):
    """Labeled Constrained Entry with SuperWidgetMixin"""

    def __init__(
        self,
        parent: ttk.Frame,
        check_function: Callable,
        labeltext: str,
        command: Callable = None,
        default: str = "",
        on_keystroke: bool = False,
        bind_enter: bool = True,
        bind_escape_clear: bool = True,
        is_child: bool = False,
        min_width: int = 0,
        widgetargs={},
        **kw,
    ):
        Labeler.__init__(self, parent, labeltext, header=not is_child)
        ConstrainedEntry.__init__(
            self,
            self.frame,
            check_function,
            width=min_width,
            **kw,
        )
        ConstrainedEntry.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        SuperWidgetMixin.__init__(self, **widgetargs)
        self.default = default
        self.is_child = is_child
        self._command = command
        if on_keystroke:
            self.bind("<KeyRelease>", self._on_execute_command)
        if bind_enter:
            self.bind("<Return>", self._on_execute_command)
        if bind_escape_clear:
            self.bind("<Escape>", self.clear())

    def enable(self):
        """Enable Entry. `Returns None`"""
        self["state"] = tk.NORMAL

    def disable(self):
        """Disable Entry. `Returns None`"""
        self["state"] = tk.DISABLED

    def _on_execute_command(self, event=None):
        """Calls the provided "command" function with the contents of the Entry. `Returns None`"""
        if self._command:
            self._command(self.get())


# fmt: off
def check_entry_int(val: str) -> bool:
    """Check if an entry input is a valid integer"""
    return check_entry_type(val, int)
class IntEntry(ConstrainedEntry):
    """Int Entry Widget"""
    def __init__(self, parent, *args, **kwargs):
        ConstrainedEntry.__init__(self, parent, check_entry_int, int, *args, **kwargs)
class LabeledIntEntry(LabeledConstrainedEntry):
    """Labeled Int Entry Widget"""
    def __init__(self, parent, labeltext, *args, **kwargs):
        kwargs.update({"return_type": int})
        LabeledConstrainedEntry.__init__(
            self, parent, check_entry_int, labeltext, **kwargs
        )
class LabeledMultiIntEntry(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Int Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledIntEntry, config)
        self.is_child = is_child


def check_entry_float(val: str) -> bool:
    """Check if an entry input is a valid float"""
    if val == ".":
        return True
    return check_entry_type(val, float)
class FloatEntry(ConstrainedEntry):
    def __init__(self, parent, *args, **kwargs):
        ConstrainedEntry.__init__(
            self, parent, check_entry_float, float, *args, **kwargs
        )
class LabeledFloatEntry(LabeledConstrainedEntry):
    def __init__(self, parent, labeltext, *args, **kwargs):
        kwargs.update({"return_type": float})
        LabeledConstrainedEntry.__init__(
            self, parent, check_entry_float, labeltext, **kwargs
        )
class LabeledMultiFloatEntry(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Float Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledFloatEntry, config)
        self.is_child = is_child


def check_entry_ascii_lowercase(val: str) -> bool:
    """Check if entry input is made only of lowercase ascii"""
    return check_entry_contents(val, string.ascii_lowercase)
class LowercaseEntry(ConstrainedEntry):
    def __init__(self, parent, *args, **kwargs):
        ConstrainedEntry.__init__(
            self, parent, check_entry_ascii_lowercase, *args, **kwargs
        )
class LabeledLowercaseEntry(LabeledConstrainedEntry):
    def __init__(self, parent, labeltext, *args, **kwargs):
        LabeledConstrainedEntry.__init__(
            self, parent, check_entry_ascii_lowercase, labeltext, **kwargs
        )
class LabeledMultiLowercaseEntry(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Lowercase Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledLowercaseEntry, config)
        self.is_child = is_child


def check_entry_ascii_uppercase(val: str) -> bool:
    """Check if entry input is made only of uppercase ascii"""
    return check_entry_contents(val, string.ascii_uppercase)
class UppercaseEntry(ConstrainedEntry):
    def __init__(self, parent, *args, **kwargs):
        ConstrainedEntry.__init__(
            self, parent, check_entry_ascii_uppercase, *args, **kwargs
        )
class LabeledUppercaseEntry(LabeledConstrainedEntry):
    def __init__(self, parent, labeltext, *args, **kwargs):
        LabeledConstrainedEntry.__init__(
            self, parent, check_entry_ascii_uppercase, labeltext, **kwargs
        )
class LabeledMultiUppercaseEntry(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Uppercase Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledUppercaseEntry, config)
        self.is_child = is_child


def check_entry_ascii_letters(val: str) -> bool:
    """Check if entry input is made only of uppercase and lowercase ascii"""
    return check_entry_contents(val, string.ascii_letters)
class LettersEntry(ConstrainedEntry):
    def __init__(self, parent, *args, **kwargs):
        ConstrainedEntry.__init__(
            self, parent, check_entry_ascii_letters, *args, **kwargs
        )
class LabeledLettersEntry(LabeledConstrainedEntry):
    def __init__(self, parent, labeltext, *args, **kwargs):
        LabeledConstrainedEntry.__init__(
            self, parent, check_entry_ascii_letters, labeltext, **kwargs
        )
class LabeledMultiLettersEntry(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Letters Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledLettersEntry, config)
        self.is_child = is_child


def check_entry_ascii_digits(val: str) -> bool:
    """Check if entry input is made only of digits"""
    return check_entry_contents(val, string.digits)
class DigitsEntry(ConstrainedEntry):
    def __init__(self, parent, *args, **kwargs):
        ConstrainedEntry.__init__(
            self, parent, check_entry_ascii_digits, *args, **kwargs
        )
class LabeledDigitsEntry(LabeledConstrainedEntry):
    def __init__(self, parent, labeltext, *args, **kwargs):
        LabeledConstrainedEntry.__init__(
            self, parent, check_entry_ascii_digits, labeltext, **kwargs
        )
class LabeledMultiDigitsEntry(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Digits Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledDigitsEntry, config)
        self.is_child = is_child


def check_entry_ascii_uppercase_digits(val: str) -> bool:
    """Check if entry input is made only of uppercase ascii and digits"""
    return check_entry_contents(val, string.ascii_uppercase + string.digits)
class UppercaseDigitsEntry(ConstrainedEntry):
    def __init__(self, parent, *args, **kwargs):
        ConstrainedEntry.__init__(
            self, parent, check_entry_ascii_uppercase_digits, *args, **kwargs
        )
class LabeledUppercaseDigitsEntry(LabeledConstrainedEntry):
    def __init__(self, parent, labeltext, *args, **kwargs):
        LabeledConstrainedEntry.__init__(
            self, parent, check_entry_ascii_uppercase_digits, labeltext, **kwargs
        )
class LabeledMultiUppercaseDigitsEntry(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Uppercase Digits Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledUppercaseDigitsEntry, config)
        self.is_child = is_child


def check_entry_ascii_lowercase_digits(val: str) -> bool:
    """Check if entry input is made only of lowercase ascii and digits"""
    return check_entry_contents(val, string.ascii_lowercase + string.digits)
class LowercaseDigitsEntry(ConstrainedEntry):
    def __init__(self, parent, *args, **kwargs):
        ConstrainedEntry.__init__(
            self, parent, check_entry_ascii_lowercase_digits, *args, **kwargs
        )
class LabeledLowercaseDigitsEntry(LabeledConstrainedEntry):
    def __init__(self, parent, labeltext, *args, **kwargs):
        LabeledConstrainedEntry.__init__(
            self, parent, check_entry_ascii_lowercase_digits, labeltext, **kwargs
        )
class LabeledMultiLowercaseDigitsEntry(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Lowercase Digits Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledLowercaseDigitsEntry, config)
        self.is_child = is_child


def check_entry_ascii_letters_digits(val) -> bool:
    """Check if entry input is made only of ascii lowercase, ascii uppercase, and digits"""
    return check_entry_contents(val, string.ascii_letters + string.digits)
class LettersDigitsEntry(ConstrainedEntry):
    def __init__(self, parent, *args, **kwargs):
        ConstrainedEntry.__init__(
            self, parent, check_entry_ascii_letters_digits, *args, **kwargs
        )
class LabeledLettersDigitsEntry(LabeledConstrainedEntry):
    def __init__(self, parent, labeltext, *args, **kwargs):
        LabeledConstrainedEntry.__init__(
            self, parent, check_entry_ascii_letters_digits, labeltext, **kwargs
        )
class LabeledMultiLettersDigitsEntry(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Letters Digits Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledLettersDigitsEntry, config)
        self.is_child = is_child


def check_entry_ascii_hexdigits(val: str) -> bool:
    """Check if entry input is made only of hexigits"""
    return check_entry_contents(val, string.hexdigits)
class HexdigitsEntry(ConstrainedEntry):
    def __init__(self, parent, *args, **kwargs):
        ConstrainedEntry.__init__(
            self, parent, check_entry_ascii_hexdigits, *args, **kwargs
        )
class LabeledHexdigitsEntry(LabeledConstrainedEntry):
    def __init__(self, parent, labeltext, *args, **kwargs):
        LabeledConstrainedEntry.__init__(
            self, parent, check_entry_ascii_hexdigits, labeltext, **kwargs
        )
class LabeledMultiHexdigitsEntry(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Hexdigits Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledHexdigitsEntry, config)
        self.is_child = is_child


def check_entry_ascii_octdigits(val: str) -> bool:
    """Check if entry input is made only of octdigits"""
    return check_entry_contents(val, string.octdigits)
class OctdigitsEntry(ConstrainedEntry):
    def __init__(self, parent, *args, **kwargs):
        ConstrainedEntry.__init__(
            self, parent, check_entry_ascii_octdigits, *args, **kwargs
        )
class LabeledOctdigitsEntry(LabeledConstrainedEntry):
    def __init__(self, parent, labeltext, *args, **kwargs):
        LabeledConstrainedEntry.__init__(
            self, parent, check_entry_ascii_octdigits, labeltext, **kwargs
        )
class LabeledMultiOctdigitsEntry(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Octdigits Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledOctdigitsEntry, config)
        self.is_child = is_child


def check_entry_ascii_printable(val: str) -> bool:
    """Check if entry input is made only of printable characters"""
    return check_entry_contents(val, string.check_ascii_printable)
class PrintableEntry(ConstrainedEntry):
    def __init__(self, parent, *args, **kwargs):
        ConstrainedEntry.__init__(
            self, parent, check_entry_ascii_printable, *args, **kwargs
        )
class LabeledPrintableEntry(LabeledConstrainedEntry):
    def __init__(self, parent, labeltext, *args, **kwargs):
        LabeledConstrainedEntry.__init__(
            self, parent, check_entry_ascii_printable, labeltext, **kwargs
        )
class LabeledMultiPrintableEntry(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget Labeled Printable Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledPrintableEntry, config)
        self.is_child = is_child
