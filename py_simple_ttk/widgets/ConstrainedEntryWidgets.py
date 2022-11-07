import tkinter as tk
from tkinter import ttk
import string
from typing import Callable
from .Labeler import Labeler
from .WidgetsCore import SuperWidgetMixin
from .MultiWidget import MultiWidgetMixin

from .LabeledMultiWidget import LabeledMultiWidgetMixin

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


class ConstrainedEntry(ttk.Frame, SuperWidgetMixin):
    """Constrained Entry with SuperWidget mixin"""

    __desc__ = "An Entry widget that allows certain constraints to be placed on the input with a given check_function that returns true if the input is allowed for each keystroke / input."

    def __init__(
        self,
        parent: ttk.Frame,
        check_function: Callable,
        return_type: type = str,
        command: Callable = None,
        on_keystroke: bool = False,
        bind_enter: bool = True,
        bind_escape_clear: bool = True,
        default: str = "",
        widgetargs={},
        **kw,
    ):
        ttk.Frame.__init__(self, parent)
        SuperWidgetMixin.__init__(self, **widgetargs)
        self.var = tk.StringVar()
        self.var.trace("w", self._validate)
        self._command = command
        self.default = default
        if self.default:
            self.set(default)
        self.entry = ttk.Entry(self, textvariable=self.var, **kw)
        self.entry.pack(fill="x", expand=True)
        self.check_function, self.return_type = check_function, return_type
        self.last = ""
        if on_keystroke:
            self.entry.bind("<KeyRelease>", self._on_execute_command)
        if bind_enter:
            self.entry.bind("<Return>", self._on_execute_command)
        if bind_escape_clear:
            self.entry.bind("<Escape>", self.clear())

    def _on_execute_command(self, event=None) -> None:
        """Calls the provided "command" function with the contents of the Entry. `Returns None`"""
        if self._command:
            self._command(self.get())

    def _validate(self, *args, **kw) -> bool:
        """Applies the check function"""
        val = self.var.get()
        if self.check_function(val):
            self.last = val
        else:
            self.var.set(self.last)

    def get(self) -> object:
        """Get Entry value, return type varies based on Entry constraint."""
        return self.return_type(self.var.get())

    def set(self, val) -> None:
        """Set Entry value. `Returns None`"""
        try:
            self.var.set(str(val))
        except:
            raise ValueError("Invaild type supplied.")

    def clear(self) -> None:
        """Set Entry value to default, empty unless default set. `Returns None`"""
        self.var.set(self.default)

    def enable(self) -> None:
        """Enable Entry. `Returns None`"""
        self.entry["state"] = tk.NORMAL

    def disable(self) -> None:
        """Disable Entry. `Returns None`"""
        self.entry["state"] = tk.DISABLED


# fmt: off
class LabeledConstrainedEntry(Labeler, ConstrainedEntry):
    """Labeled Constrained Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        *args,
        is_child: bool = False,
        **kw,
    ):
        Labeler.__init__(self, parent, labeltext, header=not is_child)
        ConstrainedEntry.__init__(self, self.frame, *args, **kw)
        ConstrainedEntry.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        self.is_child = is_child
class LabeledMultiConstrainedEntry(LabeledMultiWidgetMixin):
    """Labeled Multi Constrained Entry"""
    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside: str = tk.TOP,
        **kw,
    ):
        LabeledMultiWidgetMixin.__init__(self,LabeledConstrainedEntry,parent,labeltext,config,is_child,labelside,**kw,)


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
            self, parent, labeltext, check_entry_int, **kwargs
        )
class LabeledMultiIntEntry(LabeledMultiWidgetMixin):
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
            self, LabeledIntEntry, parent, labeltext, config, is_child, labelside, **kw
        )


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
            self, parent, labeltext, check_entry_float, **kwargs
        )
class LabeledMultiFloatEntry(LabeledMultiWidgetMixin):
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
            self, LabeledFloatEntry, parent, labeltext, config, is_child, labelside, **kw
        )


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
            self, parent, labeltext, check_entry_ascii_lowercase, **kwargs
        )
class LabeledMultiLowercaseEntry(LabeledMultiWidgetMixin):
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
            self, LabeledLowercaseEntry, parent, labeltext, config, is_child, labelside, **kw
        )


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
            self, parent, labeltext, check_entry_ascii_uppercase, **kwargs
        )
class LabeledMultiUppercaseEntry(LabeledMultiWidgetMixin):
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
            self, LabeledUppercaseEntry, parent, labeltext, config, is_child, labelside, **kw
        )


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
            self, parent, labeltext, check_entry_ascii_letters, **kwargs
        )
class LabeledMultiLettersEntry(LabeledMultiWidgetMixin):
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
            self, LabeledLettersEntry, parent, labeltext, config, is_child, labelside, **kw
        )


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
            self, parent, labeltext, check_entry_ascii_digits, **kwargs
        )
class LabeledMultiDigitsEntry(LabeledMultiWidgetMixin):
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
            self, LabeledDigitsEntry, parent, labeltext, config, is_child, labelside, **kw
        )


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
            self, parent, labeltext, check_entry_ascii_uppercase_digits, **kwargs
        )
class LabeledMultiUppercaseDigitsEntry(LabeledMultiWidgetMixin):
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
            self, LabeledUppercaseDigitsEntry, parent, labeltext, config, is_child, labelside, **kw
        )


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
            self, parent, labeltext, check_entry_ascii_lowercase_digits, **kwargs
        )
class LabeledMultiLowercaseDigitsEntry(LabeledMultiWidgetMixin):
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
            self, LabeledLowercaseDigitsEntry, parent, labeltext, config, is_child, labelside, **kw
        )


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
            self, parent, labeltext, check_entry_ascii_letters_digits, **kwargs
        )
class LabeledMultiLettersDigitsEntry(LabeledMultiWidgetMixin):
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
            self, LabeledLettersDigitsEntry, parent, labeltext, config, is_child, labelside, **kw
        )


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
            self, parent, labeltext, check_entry_ascii_hexdigits, **kwargs
        )
class LabeledMultiHexdigitsEntry(LabeledMultiWidgetMixin):
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
            self, LabeledHexdigitsEntry, parent, labeltext, config, is_child, labelside, **kw
        )


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
            self, parent, labeltext, check_entry_ascii_octdigits, **kwargs
        )
class LabeledMultiOctdigitsEntry(LabeledMultiWidgetMixin):
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
            self, LabeledOctdigitsEntry, parent, labeltext, config, is_child, labelside, **kw
        )


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
            self, parent, labeltext, check_entry_ascii_printable, **kwargs
        )
class LabeledMultiPrintableEntry(LabeledMultiWidgetMixin):
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
            self, LabeledPrintableEntry, parent, labeltext, config, is_child, labelside, **kw
        )


# # # # # 3 # 519
