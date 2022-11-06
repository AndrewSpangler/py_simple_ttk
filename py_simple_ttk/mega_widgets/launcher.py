import os, sys, platform, subprocess, webbrowser
import tkinter as tk
from tkinter import ttk
from py_simple_ttk import Tab
from typing import Callable

from .. import (
    FocusedToplevel,
    LabeledCombobox,
    LabeledEntry,
    NoticeWindow,
    open_link,
    PromptWindow,
    ScrolledListBox,
    YesNoCancelWindow,
    OrderedListbox,
    Counter,
)


def _run_cl(path: str) -> None:
    if sys.platform == "win32":
        subprocess.Popen(["start", path], shell=True)
        return
    subprocess.Popen([path])


def _open_folder(path: str) -> None:
    subprocess.Popen(
        {
            "Windows": ["explorer", path],
            "Darwin": ["open", path],
        }.get(platform.system(), ["xdg-open", path]),
        shell=True,
    )


class _LauncherButtonEditorWindow(FocusedToplevel):
    types = ["URL", "Folder", "Command"]
    types_lower = [l.lower() for l in types]

    def __init__(
        self,
        window: tk.Toplevel,
        name: str,
        config: dict,
        on_submit: Callable,
    ):
        FocusedToplevel.__init__(self, window=window)
        self._finish_setup()
        self.on_submit = on_submit
        self.config = config
        self.name = LabeledEntry(self.frame, "Button Label", default=name)
        self.name.pack(fill="x", padx=20, pady=(20, 0))
        self.location = LabeledEntry(self.frame, "Location", default=config["location"])
        self.location.pack(fill="x", padx=20)
        self.type = LabeledCombobox(
            self.frame,
            "Type",
            values=self.types,
            default=self.types_lower.index(config["type"].lower()),
        )
        self.type.pack(fill="x", padx=20)
        ttk.Button(self.frame, text="Submit", command=self._exit).pack(
            fill="x", padx=20
        )
        self.protocol("WM_DELETE_WINDOW", self._exit)

    def _exit(self, *args, **kwargs) -> None:
        err = False
        if not (name := self.name.get()):
            err = "Name cannot be empty"
        elif not (location := self.location.get()):
            err = "Location cannot be blank"
        if err:
            NoticeWindow(window=self.window, text=err)
            return err
        self.config.update({"location": location, "type": self.type.get().lower()})
        self.on_submit(name, self.config)
        self.destroy()


class _LauncherEditorWindow(FocusedToplevel):
    def __init__(self, app, preference_key: str, on_submit: Callable):
        FocusedToplevel.__init__(self, window=app.window)
        self._finish_setup()
        self.app, self.key, self.on_submit = app, preference_key, on_submit
        self.profile = app.profiles.current_profile
        self.title("Editing Launcher")
        self.data = self.profile.get_preference("launchers")[preference_key]
        self.child_window, self.listbox = None, None
        ttk.Button(self.frame, text="Add", command=self._add).pack(
            fill="x", padx=20, pady=(20, 0)
        )
        ttk.Label(
            self.frame,
            text="Click & drag to reorder\nDouble-click to edit\nDouble right-click to delete",
            anchor="n",
            justify="center",
        ).pack(fill="x", padx=20)
        self.body = ttk.Frame(self.frame)
        self.body.pack(fill="both", expand=True, padx=20)
        ttk.Button(self.frame, text="Submit", command=self._exit).pack(
            fill="x", padx=20, pady=(0, 20)
        )
        self._refresh()
        self.protocol("WM_DELETE_WINDOW", self._exit)

    def _exit(self, event=None) -> None:
        print("Exiting Launcher Editor")
        out = {}
        for i in self.listbox.get(0, "end"):
            out[i] = self.data[i]
        launchers = self.profile.get_preference("launchers")
        launchers[self.key] = out
        self.profile.set_preference("launchers", launchers)
        self.on_submit()
        self.destroy()

    def _handle_add(self, name: str, settings: dict) -> None:
        err = None
        if name in self.data:
            err = "Button must have a unique label."
        if err:
            self.child_window = _LauncherButtonEditorWindow(
                self.window, name, settings, self._handle_add
            )
            NoticeWindow(window=self.child_window, text=err)
            return
        self.data[name] = settings
        self.profile.set_preference(self.key, self.data)
        try:
            self.child_window.destroy()
        except:
            pass
        self.child_window = None
        self._refresh()

    def _add(self) -> None:
        _LauncherButtonEditorWindow(
            self, "", {"type": "url", "location": "", "columns": 1}, self._handle_add
        )

    def _edit(self, event=None) -> None:
        key = self.listbox.get((index := self.listbox.curselection()))

        def on_submit(name: str, settings: dict):
            data = {}
            for k in self.data:
                if not name == key:
                    # Name changed
                    if k == key:
                        data[name] = settings
                    else:
                        data[k] = self.data[k]
                else:
                    if k == name:
                        data[k] = settings
                    else:
                        data[k] = self.data[k]
            launchers = self.profile.get_preference("launchers")
            launchers[self.key] = data
            self.profile.set_preference("launchers", launchers)
            self.data = data
            self._refresh()

        _LauncherButtonEditorWindow(self, key, self.data[key], on_submit)

    def _delete(self, event=None) -> None:
        key = self.listbox.get(index := self.listbox.nearest(event.y))

        def delete():
            print(f"Deleting {key}...")
            self.data.pop(key)
            self.profile.set_preference(self.key, self.data)
            self._refresh()

        YesNoCancelWindow(
            window=self, no_enabled=False, text=f"Delete {key}?", on_yes=delete
        )

    def _refresh(self) -> None:
        for w in self.body.winfo_children():
            try:
                w.destroy()
            except:
                continue
        self.listbox = OrderedListbox(
            self.body,
            widgetargs={
                "on_double_left_click": self._edit,
                "on_double_right_click": self._delete,
            },
        )
        self.listbox.pack(fill="both", expand=True)
        for i in list(self.profile.get_preference("launchers")[self.key].keys()):
            self.listbox.insert("end", i)


class ConfigurableLauncher(Tab):
    """Dynamic File/Folder/URL Launcher Tab"""

    __desc__ = """A profile-based, user-editable launcher tab. Uses a uniqe key for each element in profile["launchers"][key] to remember launcher contents between runs"""

    def __init__(
        self,
        app,
        notebook: ttk.Notebook,
        key: str,
        enable_delete: bool = False,
        min_columns: int = 1,
        max_columns: int = 6,
    ):
        if not hasattr(app, "profiles"):
            raise ValueError("Application profiles not enabled")
        profile = app.profiles.current_profile
        if not profile.get_preference("launchers"):
            profile.set_preference("launchers", {})
        if not profile.get_preference("launcher_widths"):
            profile.set_preference("launcher_widths", {})
        launchers = profile.get_preference("launchers")
        launcher_widths = profile.get_preference("launcher_widths")
        if not key in launcher_widths:
            launcher_widths[key] = 1
            profile.set_preference("launcher_widths", launcher_widths)
        if not launchers[key]:
            launchers[key] = {}
            profile.set_preference("launchers", launchers)
        self.app, self.key, self.enable_delete = (app, key, enable_delete)
        self.app.profiles.add_select_profile_action(self._refresh)
        self.actions = {
            "url": open_link,
            "command": _run_cl,
            "folder": _open_folder,
        }
        Tab.__init__(self, notebook, key)
        (header := ttk.Frame(self)).pack(side="top", fill="x")
        self.body = None  # ttk.Frame placeholder
        ttk.Button(header, text="Edit", command=self._edit).pack(side="left")
        self.columns = Counter(
            header,
            min_value=min_columns,
            max_value=max_columns,
            command=self._schedule_columns,
            default=launcher_widths[key],
        )
        if enable_delete:
            ttk.Button(header, text="Delete", command=self._delete).pack(side="right")
            self.columns.pack(side="top")
        else:
            self.columns.pack(side="right")

        self._scheduled = None  # Placeholder for scheduled column count save (Reduces number of writes to disk)
        self._refresh()

    def _refresh(self, event=None) -> None:
        if self.body:
            self.body.destroy()
        self.body = ttk.Frame(self)
        self.body.pack(fill="both", expand=True, side="top")
        cols = []
        for _ in range(self.columns.get()):
            (c := ttk.Frame(self.body)).pack(side="left", fill="both", expand=True)
            cols.append(c)

        data = self.app.profiles.current_profile.get_preference("launchers")[self.key]
        i = 0
        for k in data:
            button = ttk.Button(
                cols[i % len(cols)],
                text=k,
                command=lambda k=k: self.actions[data[k]["type"]](data[k]["location"]),
            )
            button.pack(fill="x", expand=False, side=tk.TOP)
            i += 1

    def _edit(self) -> None:
        _LauncherEditorWindow(self.app, self.key, self._refresh)

    def _delete(self) -> None:
        if not self.enable_delete:
            raise ValueError("Tab deletion is disabled")

        def on_delete() -> None:
            launchers = self.app.profiles.current_profile.get_preference("launchers")
            launchers.pop(self.key)
            self.app.profiles.current_profile.set_preference("launchers", launchers)
            launcher_widths = self.app.profiles.current_profile.get_preference(
                "launcher_widths"
            )
            launcher_widths.pop(self.key)
            self.app.profiles.current_profile.set_preference(
                "launcher_widths", launcher_widths
            )
            self.destroy()

        YesNoCancelWindow(
            window=self,
            no_enabled=False,
            text=f"Are you sure you want to delete launcher {self.key}?",
            on_yes=on_delete,
        )

    def _save_columns(self, event=None) -> None:
        print("Saving")
        self._unschedule_columns()
        launcher_widths = self.app.profiles.current_profile.get_preference(
            "launcher_widths"
        )
        launcher_widths[self.key] = self.columns.get()
        self.app.profiles.current_profile.set_preference(
            "launcher_widths", launcher_widths
        )

    def _unschedule_columns(self) -> None:
        if not self._scheduled is None:
            scheduled = self._scheduled
            self._scheduled = None
            if scheduled:
                self.after_cancel(scheduled)

    def _schedule_columns(self, event=None) -> None:
        self._refresh()
        self._unschedule_columns()
        self._scheduled = self.after(500, self._save_columns)


class LauncherTools:
    """Dynamically adds editable launcher tabs to a notebook."""

    __desc__ = """The main App object has one of these attached to the toplevel notebook if enable_launcher is enabled in the app config json."""

    def __init__(
        self,
        app,
        target_notebook: ttk.Notebook = None,
        add_menu=True,
        launcher_menu_text: str = "New Launcher",
        enable_reorder: bool = True,
    ):
        self.app = app
        self.target_notebook = target_notebook or app.notebook
        self.app.menu.add_command(label=launcher_menu_text, command=self.new_launcher)
        if not self.app.profiles.current_profile.get_preference("launchers"):
            self.app.profiles.current_profile.set_preference("launchers", {})
        if launchers := self.app.profiles.current_profile.get_preference("launchers"):
            for l in launchers:
                ConfigurableLauncher(
                    self.app, self.target_notebook, l, enable_delete=True
                )

    def new_launcher(self) -> None:
        def new_launcher(name: str) -> None:
            launchers = self.app.profiles.current_profile.get_preference("launchers")
            err = False
            if not name:
                err = "Launcher name cannot be empty"
            elif name in launchers:
                err = "Launcher name must be unique"
            if err:
                PromptWindow(
                    window=self.app.window,
                    text="Launcher name cannot be empty",
                    on_yes=new_launcher,
                )
                return
            launchers[name] = {}
            self.app.profiles.current_profile.set_preference("launchers", launchers)
            ConfigurableLauncher(
                self.app, self.target_notebook, name, enable_delete=True
            )

        PromptWindow(
            window=self.app.window, text="New Launcher Name:", on_yes=new_launcher
        )

    def reorder_launchers(self) -> None:
        """Do not use this function if tabs not added by this LauncherTools object are present in the target notebook"""
        pass
