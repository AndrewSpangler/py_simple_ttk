import tkinter as tk
from tkinter import ttk
from .WidgetsCore import center_window, default_pack
from .EntryWidgets import PasswordEntry
from .ListBoxWidgets import Table
from .RadiobuttonWidgets import LabeledRadioTable
from .TextWidgets import ScrolledText
from typing import Callable


class FocusedToplevel(tk.Toplevel):
    """Base Focused Toplevel Class"""

    __desc__ = """Window that takes focus and center's itself on the current window. Used as a base class for other windows."""

    def __init__(
        self,
        *args,
        title: str = None,
        window: tk.Toplevel = None,
        on_close: Callable = None,
        **kwargs,
    ):
        self.window = window
        if not window:
            raise ValueError('Missing required argument "window"')
        tk.Toplevel.__init__(self, *args, **kwargs)
        if title:
            self.title(title)
        self.on_close = on_close
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True, ipadx=10, ipady=10)
        self.grab_set()  # Set focus on this window
        self.transient(self.window)  # Force toplevel on top of window
        self.update_idletasks()

    def _on_close(self, event=None) -> None:
        if self.on_close:
            self.on_close()
        self.destroy()

    def _finish_setup(self) -> None:
        def finish_setup():
            """Call this when the setup process is done to properly center the window."""
            self.update_idletasks()
            self.resizable(False, False)
            center_window(self.window, self)

        self.after(100, finish_setup)
        self.after(200, self.focus_force)

    def destroy(self) -> None:
        try:
            if self.grab_current() is self:
                self.grab_release()
        except:
            pass
        super().destroy()


class NoticeWindow(FocusedToplevel):
    """Provides the user with a notice."""

    __desc__ = """`button_action` can call a function to help with determining acceptance vs. the user hitting the exit button."""

    def __init__(
        self,
        *args,
        text: str = None,
        button_text: str = "Continue",
        button_action: Callable = None,
        **kwargs,
    ):
        FocusedToplevel.__init__(self, *args, **kwargs)
        ttk.Label(self.frame, text=text, justify=tk.CENTER, anchor="n").pack(
            side=tk.TOP, fill="x", padx=10, pady=(5, 0)
        )
        self.button_action = button_action
        button = ttk.Button(self.frame, text=button_text, command=self._on_button)
        button.pack(side=tk.TOP, fill="x", padx=10, pady=(5, 0))
        button.focus_set()
        self._finish_setup()

    def _on_button(self, event=None) -> None:
        if self.button_action:
            self.button_action()
        self.destroy()


class YesNoCancelWindow(FocusedToplevel):
    """Provides the user with a yes/no/cancel option."""

    __desc__ = """`no_destroy` can be set to `True` to allow the window to remain open after a selection is made."""

    def __init__(
        self,
        *args,
        text: str = None,
        yes_enabled: bool = True,
        on_yes: Callable = None,
        yes_text: str = "Yes",
        no_enabled: bool = True,
        on_no: Callable = None,
        no_text: str = "No",
        cancel_enabled: bool = True,
        on_cancel: Callable = None,
        cancel_text: str = "Cancel",
        no_destroy: bool = False,
        focus: str = "",  # "yes", "no", "cancel"
        **kwargs,
    ):
        FocusedToplevel.__init__(self, *args, **kwargs)
        self.on_yes = on_yes
        self.on_no = on_no
        self.on_cancel = on_cancel
        self.no_destroy = no_destroy
        focused_button = None
        ttk.Label(self.frame, text=f"\n{text}\n", justify=tk.CENTER, anchor="n").pack(
            side=tk.TOP, fill="x", padx=10, pady=(5, 0)
        )
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(side=tk.TOP, fill="x", expand=True, padx=10)
        if cancel_enabled:
            button = ttk.Button(button_frame, text=cancel_text, command=self._on_cancel)
            button.pack(side=tk.LEFT, expand=True, fill="x")
            if focus.lower() == "cancel":
                focused_button = button
        if no_enabled:
            button = ttk.Button(button_frame, text=no_text, command=self._on_no)
            button.pack(side=tk.LEFT, expand=True, fill="x")
            if focus.lower() == "no":
                focused_button = button
        if yes_enabled:
            button = ttk.Button(button_frame, text=yes_text, command=self._on_yes)
            button.pack(side=tk.LEFT, expand=True, fill="x")
            if focus.lower() == "yes":
                focused_button = button
        self._finish_setup()
        if focused_button:
            self.after(100, focused_button.focus)

    def _on_yes(self, event=None) -> None:
        if self.on_yes:
            self.on_yes()
        if not self.no_destroy:
            self.destroy()

    def _on_no(self, event=None) -> None:
        if self.on_no:
            self.on_no()
        if not self.no_destroy:
            self.destroy()

    def _on_cancel(self, event=None) -> None:
        if self.on_cancel:
            self.on_cancel()
        if not self.no_destroy:
            self.destroy()


class PromptWindow(FocusedToplevel):
    """Prompts the user for a text input"""

    __desc__ = """`no_destroy` can be set to `True` to allow the window to remain open after a selection is made, useful for informing the user a string input was invalid via setting label_var. \
If the select_type kwarg is set to true the user will be prompted to select a data type (int / string) to return."""

    def __init__(
        self,
        *args,
        text: str = "Enter Text:",
        on_yes=None,
        yes_text: str = "Continue",
        on_cancel=None,
        cancel_text: str = "Cancel",
        bind_enter: bool = True,
        no_destroy: bool = False,
        select_type: bool = False,
        focus="",  # "yes", "cancel"
        **kwargs,
    ):
        FocusedToplevel.__init__(self, *args, **kwargs)
        self.on_yes = on_yes
        self.on_cancel = on_cancel
        self.no_destroy = no_destroy
        self.select_type = select_type
        self.label_var = tk.StringVar()
        self.label_var.set(text)
        ttk.Label(
            self.frame, textvariable=self.label_var, justify=tk.CENTER, anchor="n"
        ).pack(side=tk.TOP, fill="x", padx=10, pady=(5, 0))
        self.var = tk.StringVar()
        self.var.set("")
        entry = ttk.Entry(self.frame, textvariable=self.var)
        entry.pack(side=tk.TOP, fill="x", padx=10, pady=(0, 5))
        if bind_enter:
            entry.bind("<Return>", self._on_yes)

        self.typemap = {"String": str, "Integer": int, "Float": float}
        if select_type:
            self.types = LabeledRadioTable(
                self.frame, "Value Type", ("String", "Integer", "Float"), 0
            )
            default_pack(self.types)

        button_frame = ttk.Frame(self.frame)
        button_frame.pack(side=tk.TOP, fill="x", expand=True, padx=10)

        button = ttk.Button(button_frame, text=cancel_text, command=self._on_cancel)
        button.pack(side=tk.LEFT, fill="x", expand=True)
        if focus.lower() == "cancel":
            button.focus_set()

        button = ttk.Button(button_frame, text=yes_text, command=self._on_yes)
        button.pack(side=tk.LEFT, fill="x", expand=True)
        if focus.lower() == "yes":
            button.focus_set()

        self._finish_setup()

    def _on_yes(self, event=None) -> None:
        if self.on_yes:
            if self.select_type:
                t = self.typemap[self.types.get()]
                val = self.var.get()
                try:
                    val = t(val)
                except Exception as e:
                    NoticeWindow(
                        window=self,
                        text=f'Error interpreting provided value as type "{t.__name__}"',
                    )
                    return
                self.on_yes(val)
            else:
                self.on_yes(self.var.get())
        if not self.no_destroy:
            self.destroy()

    def _on_cancel(self, event=None) -> None:
        if self.on_cancel:
            self.on_cancel(self.var.get())
        if not self.no_destroy:
            self.destroy()


class ListWindow(FocusedToplevel):
    """Window to select an option from a Scrolled Listbox"""

    # __desc__ = """`no_destroy` can be set to `True` to allow the window to remain open after a selection is made, useful for informing the user a string input was invalid via setting label_var."""
    def __init__(
        self,
        *args,
        options: list,
        text: str = "Select Item:",
        on_yes=None,
        yes_text: str = "Continue",
        on_cancel=None,
        cancel_text: str = "Cancel",
        no_destroy: bool = False,
        select_mode: str = "single",
        **kwargs,
    ):
        FocusedToplevel.__init__(self, *args, **kwargs)
        self.on_yes = on_yes
        self.on_cancel = on_cancel
        self.no_destroy = no_destroy
        self.listbox = Table(self.frame)
        self.listbox.build({text: options})
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.update_idletasks()
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(side=tk.BOTTOM, fill="x", expand=True, padx=10)
        ttk.Button(button_frame, text=cancel_text, command=self._on_cancel).pack(
            side=tk.LEFT, fill="x", expand=True
        )
        ttk.Button(button_frame, text=yes_text, command=self._on_yes).pack(
            side=tk.LEFT, fill="x", expand=True
        )
        self._finish_setup()

    def _on_yes(self, event=None) -> None:
        val = self.listbox.get()
        print(f"Listbox val {val}")
        if self.on_yes:
            if val:
                val = val[0]
            self.on_yes(val)
        if not self.no_destroy:
            self.destroy()

    def _on_cancel(self, event=None) -> None:
        if self.on_cancel:
            self.on_cancel(self.var.get())
        if not self.no_destroy:
            self.destroy()


class TextWindow(FocusedToplevel):
    """Provides the user a cancelable Scrolled Text window"""

    __desc__ = """`no_destroy` can be set to `True` to allow the window to remain open after a submission is made. on_yes callback must take the text value as a String."""

    def __init__(
        self,
        *args,
        text: str = "Enter Text",
        on_yes: Callable = None,
        yes_text: str = "Submit",
        on_cancel: Callable = None,
        cancel_text: str = "Cancel",
        no_destroy: bool = False,
        focus: str = "",  # "yes", "cancel"
        default: str = "",
        height: int = 32,
        width: int = 88,
        **kwargs,
    ):
        FocusedToplevel.__init__(self, *args, **kwargs)
        self.on_yes = on_yes
        self.on_cancel = on_cancel
        self.no_destroy = no_destroy
        focused_button = None
        ttk.Label(
            self.frame,
            text=f"\n{text}\n",
            justify=tk.CENTER,
            anchor="n",
            style="XLargeBold.TLabel",
        ).pack(side=tk.TOP, fill="x", padx=10, pady=0)
        self.text = ScrolledText(self.frame, height=height, width=width)
        self.text.pack(fill="both", padx=10, pady=0)
        self.text.set(default)
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(side=tk.TOP, fill="x", expand=True, padx=10)
        self.cancel_button = ttk.Button(
            button_frame, text=cancel_text, command=self._on_cancel
        )
        self.cancel_button.pack(side=tk.LEFT, expand=True, fill="x")
        if focus.lower() == "cancel":
            self.after(100, self.cancel_button.focus)
        self.yes_button = ttk.Button(button_frame, text=yes_text, command=self._on_yes)
        self.yes_button.pack(side=tk.LEFT, expand=True, fill="x")
        if focus.lower() == "yes":
            self.after(100, self.yes_button.focus)
        self._finish_setup()

    def _on_yes(self, event=None) -> None:
        if self.on_yes:
            self.on_yes(self.text.get())
        if not self.no_destroy:
            self.destroy()

    def _on_no(self, event=None) -> None:
        if self.on_no:
            self.on_no()
        if not self.no_destroy:
            self.destroy()

    def _on_cancel(self, event=None) -> None:
        if self.on_cancel:
            self.on_cancel()
        if not self.no_destroy:
            self.destroy()


class PasswordWindow(FocusedToplevel):
    """Password Entry window."""

    __desc__ = """Demo Password Entry Window, you will want to copy the source for this widget and rewrite it."""

    def __init__(self, window=None, **kwargs):
        if not window:
            raise ValueError('Missing required argument "window"')
        FocusedToplevel.__init__(self, window=window)
        self.geometry("300x150")
        entry = PasswordEntry(self.frame, width=100, height=100, **kwargs)
        entry.pack(fill=None, expand=True, padx=10, pady=10)
        entry.username_entry.focus_set()
        self._finish_setup()
