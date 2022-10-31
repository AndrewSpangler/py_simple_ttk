#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

if sys.hexversion < 0x03060000:
    sys.exit("Python 3.6 or greater is required to run this program.")

import json
import os
import typing
import platform
import subprocess
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

from .utils.scaling import enable_dpi_awareness
from .utils.ProfilesSystem import ProfilesSystem, UserProfile
from .widgets import (
    complex_widget_search,
    EasySizegrip,
    enable_notebook_movement,
    get_bundled_themes_list,
    get_themes_folder,
    ListWindow,
    PromptWindow,
    ScrolledCanvas,
    ScrolledText,
    Table,
)
from .mega_widgets.profile_manager import ProfilesWindow


class App:
    """Main Application Object"""

    def __init__(self, ini_file: str):
        with open(ini_file) as f:
            self.ini_data = json.load(f)
        self.app_name = self.ini_data.get("application")
        self.version = self.ini_data.get("version")
        self.version_name = "{} Version {}".format(self.app_name, self.version)
        self.os = platform.system()
        self.os_version = platform.version()
        print(self.version_name)
        print("Using Python {}.{}".format(*sys.version_info[:2]))
        print("Using tkinter version {}".format(tk.Tcl().eval("info patchlevel")))

        self.scaling = self.ini_data["scaling"]
        print(f"Application scaling factor - {self.scaling}")
        scale_startsize = self.ini_data.get("scale_startsize", False)
        scale_factor = self.scaling if scale_startsize else 1
        self.window_start_width = int(self.ini_data["width"] * scale_factor) or 1
        self.window_start_height = int(self.ini_data["height"] * scale_factor) or 1
        print(
            f"Window start size - {self.window_start_width} x {self.window_start_height}"
        )
        scale_minsize = self.ini_data.get("scale_minsize", False)
        scale_factor = self.scaling if scale_minsize else 1
        self.window_min_width = int(self.ini_data.get("minwidth", 300) * scale_factor)
        self.window_min_height = int(self.ini_data.get("minheight", 300) * scale_factor)
        print(f"Window min size - {self.window_min_width} x {self.window_min_height}")
        self.window = tk.Tk()  # Instantiate tk instance.
        self.focused_window = None  # Placeholder
        enable_dpi_awareness(self, self.scaling)  # Enable Windows DPI Scaling
        self.window.wait_visibility(self.window)
        self.window.tk.call("tk", "scaling", self.scaling)

        self.theme_textboxes = self.ini_data.get("theme_textboxes", True)

        # This toolkit is designed around the idea of "Tabs"
        # This is the highest level tab available.
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill=tk.BOTH, expand=tk.YES)

        # Add a shared menu
        self.menu = tk.Menu(self.window)
        self.window.configure(menu=self.menu)

        # Application Theming
        self.current_theme = "winnative"
        print(f"Themes folder located at {get_themes_folder()}")
        self.themes = get_bundled_themes_list(verbose=True)
        print(f"Loading bundled themes...")
        for t in self.themes.copy():
            print(f"\tLoading {t}...")
            try:
                self.window.tk.call("source", t)
            except:
                self.themes.remove(t)
                continue
        print(f"Finished loading bundled themes...")
        self.style = ttk.Style()
        self.ignored_themes = self.ini_data.get("ignored_themes", [])
        self.available_themes = []
        for t in self.style.theme_names():
            if not t in self.ignored_themes:
                self.available_themes.append(t)
        ignored = json.dumps(self.ignored_themes, indent=4)
        print(f"Ignored themes: {ignored}")
        print(f"Available themes: {json.dumps(self.available_themes, indent=4)}")

        # User Profiles
        self.profiles_enabled = False
        if self.ini_data.get("enable_users", False):
            self.profiles_enabled = True
            self.profiles = ProfilesSystem()
            print("User profiles enabled")
            print(f"Found existing profiles")
            print(f"Loading most recently used profile")
            self._select_profile(self.profiles.get_last_used_profile())

        # Window Geometry and Bindings
        self.window.geometry(f"{self.window_start_width}x{self.window_start_height}")
        self.window.minsize(width=self.window_min_width, height=self.window_min_height)
        resizable_width = self.ini_data.get("resizable_width", True)
        resizable_height = self.ini_data.get("resizable_height", True)
        self.window.resizable(resizable_width, resizable_height)
        if resizable_width and resizable_height:
            if self.ini_data.get("start_maximized", False):
                self.window.state("zoomed")  # Maximize window
            self.window.bind("<F10>", self.toggle_maximized)
            print("F10 toggles maximized")
        if self.ini_data.get("enable_fullscreen", False):
            self.window.bind("<F11>", self.toggle_full_screen)
            print("F11 toggles fullscreen")
        if self.ini_data.get("enable_sizegrip", True):
            self.size_grip = EasySizegrip(self.window)
            print("Sizegrip enabled")
        if self.ini_data.get("movable_tabs", False):
            enable_notebook_movement(self)
            print("Notebook tab movement enabled")
        if self.ini_data.get("icon"):
            try:
                icon = os.path.abspath(self.ini_data.get("icon"))
                if not os.path.isfile(icon):
                    raise FileNotFoundError(f"Icon not found at {icon}")
                if icon:
                    print(f"Icon enabled, located at {icon}")
                if icon.endswith(".ico"):
                    self.window.iconbitmap(icon)
                    print("Set window bitmap icon")
                else:
                    self.icon = tk.PhotoImage(file=icon)
                    self.window.iconphoto(True, self.icon)
                    print("Set window icon")
            except Exception as e:
                print(f"Error setting window icon - {e}")
                raise e
        self.full_screen_state = False
        self.zoomed_screen_state = False
        self.default_font = fnt = tkFont.nametofont("TkDefaultFont").actual()
        self.bold_font = (fnt["family"], fnt["size"], "bold")
        self.small_font = (fnt["family"], int(fnt["size"]) - 2, "normal")
        self.small_bold_font = (fnt["family"], int(fnt["size"]) - 2, "bold")
        self.large_font = (fnt["family"], int(fnt["size"]) + 2, "normal")
        self.large_bold_font = (fnt["family"], int(fnt["size"]) + 2, "bold")

        # Application Menu
        if self.profiles_enabled:
            prof_menu = tk.Menu(self.menu, tearoff=0)
            prof_menu.add_command(label="New Profile", command=self.create_profile)
            prof_menu.add_command(label="Select Profile", command=self.select_profile)
            prof_menu.add_command(
                label="Profile Manager", command=lambda: ProfilesWindow(self)
            )
            self.menu.add_cascade(menu=prof_menu, label="Profiles")
        if self.ini_data.get("enable_themes_menu"):
            self.theme_menu = tk.Menu(self.menu, tearoff=tk.OFF)
            for t in self.available_themes:
                self.theme_menu.add_command(
                    label=t, command=lambda t=t: self.use_theme(t)
                )
            self.menu.add_cascade(label="Themes", menu=self.theme_menu)

        theme = self.current_theme
        if self.profiles_enabled:
            profile = self.profiles.current_profile
            theme = profile.get_preference("theme") if profile else theme
        if not theme in self.available_themes:
            print(
                f'Unable to find loaded user\'s selected theme {theme}. Defaulting to theme "Default"'
            )
        self.use_theme(theme)
        self.update_default_title()

    def create_profile(self, name: str = None):
        """Calling with no name brings up a popup, the popup calls this function \
again with name kw which instead makes a new profile or asks again for a name if \
the supplied name was invalid"""
        if self.focused_window:
            self.focused_window.destroy()
        if not name:
            self.focused_window = PromptWindow(
                window=self.window,
                text="Enter New Profile Name",
                on_yes=self.create_profile,
                yes_text="Make New Profile",
            )
        else:
            self.profiles.create_profile(name)
            self.update_default_title()
            self.apply_profile(self.profiles.current_profile)

    def select_profile(self, name: str = None):
        """Calling with no name brings up a popup, the popup calls this function \
again with the name which instead calls the Profiles System to use a certain profile"""
        if self.focused_window:
            self.focused_window.destroy()
        if not name:
            self.focused_window = ListWindow(
                window=self.window,
                title="Select Profile",
                text="Select Profile",
                on_yes=self.select_profile,
                options=reversed(list(u.username for u in self.profiles.profiles)),
            )
        else:
            self.profiles.select_profile_by_username(name)
            self.update_default_title()
            self.apply_profile(self.profiles.current_profile)

    def _select_profile(self, profile: UserProfile):
        self.profiles.select_profile(profile)
        self.update_default_title()
        self.apply_profile(profile)

    def apply_profile(self, profile: UserProfile):
        """Apply settings from the current profile. For more complicated profile systems \
override this function."""
        theme = profile.get_preference("theme")
        if not theme or not theme in self.available_themes:
            print(f"User had invalid theme selected in profile - {theme}, repairing...")
            profile.set_preference("theme", "default")
        self.use_theme(profile.get_preference("theme"))

    def toggle_maximized(self, event=None):
        """Toggles maximized window."""
        self.zoomed_screen_state = not self.zoomed_screen_state
        self.window.state("normal" if self.zoomed_screen_state else "zoomed")

    def toggle_full_screen(self, event=None):
        """Toggles full screen."""
        self.full_screen_state = not self.full_screen_state
        self.window.attributes("-fullscreen", self.full_screen_state)

    def use_theme(self, theme: str = None, verbose: bool = False):
        """Updates the app to use a certain theme."""
        if not theme:
            theme = self.current_theme
        if self.profiles_enabled:
            if self.profiles.current_profile:
                self.profiles.current_profile.set_preference("theme", theme)
                self.profiles.current_profile.save()
            else:
                print(
                    f"Profiles are enabled but no profile is selected. Themes will not be saved until a profile is created."
                )
        self.current_theme = theme
        self.style.theme_use(theme)
        self.default_font = fnt = tkFont.nametofont("TkDefaultFont").actual()
        self.bold_font = (fnt["family"], fnt["size"], "bold")
        self.small_font = (fnt["family"], int(fnt["size"]) - 2, "normal")
        self.small_bold_font = (fnt["family"], int(fnt["size"]) - 2, "bold")
        self.large_font = (fnt["family"], int(fnt["size"]) + 2, "normal")
        self.large_bold_font = (fnt["family"], int(fnt["size"]) + 2, "bold")
        bg = self.style.lookup("TFrame", "background") or "#ffffff"
        text_fg = self.style.lookup("TEntry", "foreground") or "#000000"
        text_bg = self.style.lookup("TEntry", "fieldbackground") or "white"
        self.style.configure("Bold.TLabel", font=self.bold_font)
        self.style.configure("LargeBold.TLabel", font=self.large_bold_font)
        self.style.configure(
            "NoPad.TButton",
            padding=0,
            ipadding=0,
            padx=0,
            pady=0,
            borderwidth=0,
            highlightthickness=0,
        )
        self.style.configure(
            "Treeview", background=bg, fieldbackground=bg, foreground=text_fg
        )
        self.style.configure("Treeview.Heading", relief="groove")
        # Search GUI tree towards branches, updating certain elements that otherwise don't work with ttk
        widgets = complex_widget_search(
            self.window, (ScrolledText, ScrolledCanvas, Table)
        )
        if self.theme_textboxes:
            for w in widgets[ScrolledText]:
                w.configure(bg=text_bg, fg=text_fg)
        for w in widgets[ScrolledCanvas]:
            w.use_style(self.style)
        for w in widgets[Table]:
            w.use_style(self.style)

    def copy_to_user_clipboard(self, val: str):
        self.window.clipboard_clear()
        self.window.clipboard_append(val)

    def bell(self):
        """Largely redundant as all widgets have access to this method"""
        self.window.bell()

    def update_default_title(self, indicate_profile=True):
        """Update the window title with the default string, optionally with a profile indicator."""
        title = self.version_name
        if indicate_profile and self.profiles_enabled:
            if self.profiles.current_profile:
                title += f" - {self.profiles.current_profile.username}"
        self.window.title(title)

    def update_title(self, title):
        """Updates the window title"""
        self.window.title(self.version_name)

    def mainloop(self):
        """Starts the application mainloop"""
        self.window.mainloop()
