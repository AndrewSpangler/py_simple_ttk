import tkinter as tk
from tkinter import ttk
import string
from typing import Callable
from .Labeler import Labeler
from .SuperWidget import SuperWidgetMixin
from .LabeledMultiWidget import LabeledMultiWidgetMixin
from .EntryWidgets import ActiveEntry

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
def check_entry_contents(val: str, limiter: list | str) -> bool:
    """Core content checker function. Limits entry to a list of chars ['a', 'b', 'c', ...] or \
    the chars contained in a simple string 'abc...'"""
    for char in val:
        if not char in limiter:
            return False
    return True


# This class is used as a base for every class below
class ConstrainedEntry(ActiveEntry):
    """Constrained ActiveEntry"""

    __desc__ = "An Entry widget that allows certain constraints to be placed on the input with a given check_function that returns true if the input is allowed for each keystroke / input."

    def __init__(
        self,
        parent: ttk.Frame,
        check_function: Callable,
        return_type: type = str,
        **kw,
    ):
        ActiveEntry.__init__(self, parent, **kw)
        self.check_function, self.return_type = check_function, return_type
        self.var.trace("w", self._validate)
        self.last = ""

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
        LabeledMultiWidgetMixin.__init__(self, parent, labeltext, LabeledConstrainedEntry, config, is_child, labelside, **kw)


def check_entry_int(val: str) -> bool:
    """Check if an entry input is a valid integer"""
    return check_entry_type(val, int)
class IntEntry(ConstrainedEntry):
    """Int Entry Widget"""
    def __init__(self, parent, *args, **kwargs):
        # Ignore the fact that int is passed as get method is overridden
        ConstrainedEntry.__init__(self, parent, check_entry_int, int, *args, **kwargs)
    def get(self) -> int:
        """Get IntEntry value, `Returns an Int`"""
        return None if not (val := self.var.get()) else int(val)
class LabeledIntEntry(LabeledConstrainedEntry):
    """Labeled Int Entry Widget"""
    def __init__(self, parent, labeltext, *args, **kwargs):
        kwargs.update({"return_type": int})
        LabeledConstrainedEntry.__init__(
            self, parent, labeltext, check_entry_int, **kwargs
        )
    def get(self) -> int:
        """Get IntEntry value, `Returns an Int`"""
        return None if not (val := self.var.get()) else int(val)
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
            self, parent, labeltext, LabeledIntEntry, config, is_child, labelside, **kw
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
            self, parent, labeltext, LabeledFloatEntry, config, is_child, labelside, **kw
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
            self, parent, labeltext, LabeledLowercaseEntry, config, is_child, labelside, **kw
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
            self, parent, labeltext, LabeledUppercaseEntry, config, is_child, labelside, **kw
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
            self, parent, labeltext, LabeledLettersEntry, config, is_child, labelside, **kw
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
            self, parent, labeltext, LabeledDigitsEntry, config, is_child, labelside, **kw
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
            self, parent, labeltext, LabeledUppercaseDigitsEntry, config, is_child, labelside, **kw
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
            self, parent, labeltext, LabeledLowercaseDigitsEntry, config, is_child, labelside, **kw
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
            self, parent, labeltext, LabeledLettersDigitsEntry, config, is_child, labelside, **kw
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
            self, parent, labeltext, LabeledHexdigitsEntry, config, is_child, labelside, **kw
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
            self, parent, labeltext, LabeledOctdigitsEntry, config, is_child, labelside, **kw
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
            self, parent, LabeledPrintableEntry, labeltext, config, is_child, labelside, **kw
        )
