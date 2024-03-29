import platform
import tkinter as tk
from tkinter import ttk
from typing import Callable
from .Labeler import Labeler
from .Scroller import Scroller, _create_container
from .SuperWidget import SuperWidgetMixin
from .WidgetsCore import default_pack
from .LabeledMultiWidget import LabeledMultiWidgetMixin
from .ButtonWidgets import ActiveButton
from .EntryWidgets import LabeledButtonEntry


class ScrolledListBox(Scroller, tk.Listbox, SuperWidgetMixin):
    """Scrolled Listbox with SuperWidget mixin"""

    __desc___ = """Used when you need a listbox with scrollwheel binding / automatic scrollbars."""

    @_create_container
    def __init__(self, parent: ttk.Frame, widgetargs: dict = {}, **kw):
        tk.Listbox.__init__(self, parent, **kw)
        Scroller.__init__(self, parent)
        SuperWidgetMixin.__init__(self, **widgetargs)

    def add(self, val: str) -> None:
        """Add an item to the end of the Listbox. `Returns None`"""
        self.insert("end", val)

    def add_list(self, items: list) -> None:
        """Add a list of items to the end of the Listbox. `Returns None`"""
        for i in items:
            self.insert("end", i)

    def clear(self) -> None:
        """Clear Listbox. `Returns None`"""
        self.delete(0, "end")

    def disable(self):
        """Disable Listbox. `Returns None`"""
        self.configure(state=tk.DISABLED)

    def enable(self):
        """Disable Listbox. `Returns None`"""
        self.configure(state=tk.NORMAL)


class OrderedListbox(ScrolledListBox):
    """A Scrolled Re-Orderable Listbox with SuperWidget mixin"""

    __desc__ = """Used when you need a re-orderable listbox for list arrangement etc. "selectmode" can only be "single" for this Widget."""

    def __init__(self, parent: ttk.Frame, **kw):
        if kw.get("selectmode") and not kw["selectmode"] == "single":
            raise ValueError('"selectmode" can only be "single"')
        ScrolledListBox.__init__(self, parent, selectmode="single", **kw)
        self.bind("<Button-1>", self._click, add="+")
        self.bind("<B1-Motion>", self._move, add="+")
        self._index = None

    def _click(self, event) -> None:
        self._index = self.nearest(event.y)

    def _move(self, event) -> None:
        if (index := self.nearest(event.y)) == self._index:
            return
        i = self.get(index)
        self.delete(index)
        self.insert(index + (1 if index < self._index else -1), i)
        self._index = index


class ListManipulator(ttk.Frame):
    def __init__(
        self,
        parent: ttk.Frame,
        disable_entry: bool = False,
        load_button_text: str = "Load",
        load_button_width: int = 6,
        clear_button_text="Clear",
        clear_button_width: int = 6,
        add_button_text: str = "Add>",
        add_button_width: int = 6,
        listbox_height: int = 7,
        entry_text: str = "Add item",
        **kwargs,
    ):
        ttk.Frame.__init__(self, parent, **kwargs)
        default_pack(entry_frame := ttk.Frame(self))
        self.load_button = ActiveButton(
            entry_frame, text=load_button_text, command=self.load, width=6
        )
        self.load_button.pack(side=tk.RIGHT)

        self.clear_button = ActiveButton(
            entry_frame, text=clear_button_text, command=self.clear, width=6
        )
        self.clear_button.pack(side=tk.RIGHT)

        self.entry = LabeledButtonEntry(
            entry_frame,
            labeltext=entry_text,
            button_text=add_button_text,
            command=self.add,
        )
        self.entry.button.configure(width=add_button_width)
        self.entry.pack(fill="x", expand=True)
        self.listbox = OrderedListbox(self, height=listbox_height)
        self.listbox.pack(fill="both", expand=True)
        default_pack(export_frame := ttk.Frame(self))

    def clear(self) -> None:
        """Clear Entry and Listbox. `Returns None`"""
        self.entry.clear()
        self.listbox.clear()

    def load(self) -> None:
        """Load file, clear Listbox, insert each line from file into listbox. `Returns None`"""
        file = tk.filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file:
            self.entry.clear()
            with open(file) as f:
                for l in f.readlines():
                    self.listbox.add(l)

    def add(self, val: str) -> None:
        """Add an item to the listbox. `Returns None`"""
        if not val:
            return
        self.entry.clear()
        self.listbox.add(val)

    def add_list(self, *args) -> None:
        """Add a list to the listbox. `Returns None`"""
        self.listbox.add_list(*args)

    def get(self) -> list:
        """Get the list of items in the listbox. `Returns a list`"""
        return self.listbox.get(0, "end")

    def enable(self) -> None:
        """Enable Listbox, Entry, and Buttons. `Returns None`"""
        self.entry.enable()
        self.listbox.enable()
        self.load_button.enable()
        self.clear_button.enable()

    def disable(self) -> None:
        """Disable Listbox, Entry, and Buttons. `Returns None`"""
        self.entry.disable()
        self.listbox.disable()
        self.load_button.disable()
        self.clear_button.disable()


class Table(ttk.Frame):
    """Listboxes bound to scroll in union. Additional bindings will be needed in order to handle clicking."""

    __desc__ = """Tested on Mac/Windows/Linux. In most cases a TreeTable widget will be superior to this."""

    def __init__(
        self,
        *args,
        min_column_width: int = 100,
        start_column_width: int = 100,
        on_selection: Callable = None,
        visible_rows=0,  # Set above 1 to limit table rows
        **kw,
    ):
        ttk.Frame.__init__(self, *args, **kw)
        self.scrollbar = ttk.Scrollbar(self)
        self.scrollbar.config(command=self._on_scroll_bar)
        self.scrollbar.pack(side=tk.RIGHT, expand=False, fill="y")
        self.listbox_frame = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.listbox_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.listboxes, self.categories, self.labels = {}, [], []
        self.min_column_width, self.start_column_width, self.visible_rows = (
            min_column_width,
            start_column_width,
            visible_rows,
        )
        self._on_selection = on_selection

    def clear(self) -> None:
        """Clears the table"""
        for lb in self.listboxes:
            self.listboxes[lb].destroy()
        for l in self.labels:
            l.destroy()
        self.listboxes, self.categories, self.labels = {}, [], []
        for w in self.listbox_frame.winfo_children():
            w.destroy()

    def build(self, contents: dict) -> None:
        """Rebuild the table"""
        self.clear()
        self.categories = [k for k in contents.keys()]
        ratio = 1 / len(self.categories)
        i = 0
        for title in contents:
            pane_frame = ttk.Frame(self.listbox_frame)
            pane_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            l = ttk.Label(pane_frame, text=title, style="Bold.TLabel", anchor="w")
            l.pack(side=tk.TOP, expand=False, fill="x")
            self.labels.append(l)
            lb = self.listboxes[title] = tk.Listbox(
                pane_frame,
                borderwidth=1,
                highlightthickness=0,
                exportselection=0,
                yscrollcommand=self.scrollbar.set,
            )
            lb.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, ipadx=(40))
            if self.visible_rows:
                lb.configure(height=self.visible_rows)
            self.listbox_frame.add(pane_frame)
            self.listbox_frame.paneconfigure(
                pane_frame, minsize=self.min_column_width, width=self.start_column_width
            )
            lb.bind("<ButtonPress-1>", self._on_press, add="+")
            for item in contents[title]:
                lb.insert("end", item)

            if platform.system() in ["Windows", "Darwin"]:
                lb.bind("<MouseWheel>", self._on_mouse_wheel)
            else:
                for k in ["<Button-4>", "<Button-5>"]:
                    lb.bind(k, self._on_mouse_wheel)
            i += 1

    def _on_press(self, event) -> None:
        if event:
            root = self.winfo_toplevel()
            cursor_y = root.winfo_pointery()
            l = event.widget
            cursor_y -= l.winfo_rooty()
            index = l.nearest(cursor_y)
            l.select_set(index)
            l.activate(index)
            for lb in self.listboxes:
                self.listboxes[lb].selection_clear(0, tk.END)
                self.listboxes[lb].yview_moveto(l.yview()[0])
                self.listboxes[lb].select_set(index)
                self.listboxes[lb].activate(index)
            if self._on_selection:
                self._on_selection(self.listboxes.get(index))

    def _on_mouse_wheel(self, event) -> str:
        l = self.listboxes[self.categories[0]]
        if platform.system() in ["Windows" or "Darwin"]:
            delta = event.delta
            if platform.system() == "Windows":
                delta = int(-1 * (event.delta / 120))
            l.yview("scroll", delta, "units")
        elif platform.system() == "Linux":
            if event.num == 5:
                l.yview("scroll", 1, "units")
            elif event.num == 4:
                l.yview("scroll", -1, "units")
        for listbox in self.listboxes:
            self.listboxes[listbox].yview_moveto(l.yview()[0])
        return "break"

    def _on_scroll_bar(self, move_type, move_units, __=None) -> None:
        if move_type == "moveto":
            for lb in self.listboxes:
                self.listboxes[lb].yview_moveto(move_units)

    def use_style(self, style: ttk.Style) -> None:
        """Update to match supplied ttk.Style object. `Returns None`"""
        self.tile_fill = style.lookup("TEntry", "fieldbackground") or style.lookup(
            "TCombobox", "fieldbackground"
        )
        bg = style.lookup("TFrame", "background") or "#ffffff"
        fg = style.lookup("TEntry", "foreground") or "#000000"
        for lb in self.listboxes:
            self.listboxes[lb].config(bg=bg)
            self.listboxes[lb].config(fg=fg)

        self.listbox_frame.configure(bg=bg)

    def get(self) -> list:
        """Gets the currently selected items from the table. `Returns a List of Strings`"""
        out = []
        for lb in self.listboxes:
            b = self.listboxes[lb]
            sel = b.curselection()
            if sel:
                out.append(b.get(sel))
            else:
                return None
        return out
