import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk
from py_simple_ttk import (
    App,
    Tab,
    LabeledEntry,
    OrderedListbox,
    default_pack,
    LabeledButtonEntry,
    ScrolledText,
    default_separator,
    ColumnFrame,
)


def export_txt(items: list):
    if path := asksaveasfilename(
        initialfile=".txt",
        filetypes=[("TXT", ".txt"), ("All Files", "*")],
    ):
        with open(path, "w+") as f:
            f.write("\n".join(items))


def export_json(items: list):
    if path := asksaveasfilename(
        initialfile=".json",
        filetypes=[("JSON", ".json"), ("All Files", "*")],
    ):
        with open(path, "w+") as f:
            json.dump(items, f)


def export_csv(items: list):
    if path := asksaveasfilename(
        initialfile=".csv",
        filetypes=[("CSV", ".csv"), ("All Files", "*")],
    ):
        with open(path, "w+") as f:
            f.write("\n".join([i + "," for i in items]))


def export_py(items: list):
    if path := asksaveasfilename(
        initialfile=".py",
        filetypes=[("PY", ".py"), ("All Files", "*")],
    ):
        out = f"items = [\n"
        for i in items:
            out += f'\t"{i}",\n'
        out += "]\n"
        with open(path, "w+") as f:
            f.write(out)


class ListManipulator(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, **kwargs)
        default_pack(entry_frame := ttk.Frame(self))
        ttk.Button(entry_frame, text="Load", command=self.add_list, width=6).pack(
            side=tk.RIGHT
        )
        ttk.Button(entry_frame, text="Clear", command=self.clear, width=6).pack(
            side=tk.RIGHT
        )
        self.entry = LabeledButtonEntry(
            entry_frame, labeltext="Add item", button_text="Add>", command=self.add
        )
        self.entry.button.configure(width=6)
        self.entry.pack(fill="x", expand=True)
        self.listbox = OrderedListbox(self, height=7)
        self.listbox.pack(fill="both", expand=True)
        # default_pack(self.listbox)
        default_pack(export_frame := ttk.Frame(self))
        for text, a in (
            ("Save .txt", export_txt),
            ("Save .json", export_json),
            ("Save .csv", export_csv),
            ("Save .py", export_py),
        ):
            ttk.Button(
                export_frame, text=text, width=9, command=lambda a=a: a(self.get())
            ).pack(side="left")

    def clear(self):
        self.listbox.delete(0, "end")

    def add_list(self):
        file = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file:
            self.entry.clear()
            with open(file) as f:
                for l in f.readlines():
                    self.listbox.insert("end", l)

    def add(self, val: str):
        if not val:
            return
        self.entry.clear()
        self.listbox.insert("end", val)

    def get(self):
        return self.listbox.get(0, "end")


class ListCompare(App):
    def __init__(self):
        App.__init__(self, "list_compare.json")
        self.notebook.destroy()

        (
            listframe := ttk.LabelFrame(
                self.window, text="List To Search", style="LargeBold.TLabelframe"
            )
        ).pack(fill="x", padx=20, pady=(5, 0))
        self.listbox = ListManipulator(listframe)
        self.listbox.pack(fill="both")

        (
            searchframe := ttk.LabelFrame(
                self.window, text="Search", style="LargeBold.TLabelframe"
            )
        ).pack(fill="x", padx=20, pady=5)

        self.check_entry = LabeledButtonEntry(
            searchframe,
            labeltext="Search list",
            button_text="Check>",
            command=self.check,
        )
        self.check_entry.pack(fill="x")

        font = tkFont.nametofont("TkDefaultFont").actual()
        self.text = ScrolledText(
            searchframe,
            font=(font["family"], int(font["size"]) + 4, "bold"),
            height=1,
            state="disabled",
        )
        self.text.pack(fill="x", padx=0, pady=5)
        (
            columns := ColumnFrame(self.window, ["Found", "Not Found"], labeled=True)
        ).pack(fill="both", expand=True, padx=20, pady=(0, 20))
        left, right = columns.frames

        self.found_listbox = ListManipulator(left)
        self.found_listbox.pack(fill="both", expand=True)

        self.not_found_listbox = ListManipulator(right)
        self.not_found_listbox.pack(fill="both", expand=True)

    def check(self, val: str):
        if not val:
            return
        self.check_entry.clear()
        self.text.enable()
        self.text.clear()
        self.text.tag_configure("center", justify="center")
        if val in self.listbox.get():
            self.text.configure(fg="#339933")
            val = f"{val} - Found"
            self.found_listbox.listbox.insert("end", val)
        else:
            self.text.configure(fg="#FF4444")
            val = f"{val} - Not Found"
            self.not_found_listbox.listbox.insert("end", val)
        self.text.insert("1.0", val)
        self.text.tag_add("center", "1.0", "end")
        self.text.disable()


if __name__ == "__main__":
    ListCompare().mainloop()
