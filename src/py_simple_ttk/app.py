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

from .utils.scaling import enable_dpi_awareness, get_scaling
from .utils.tcl_commands import tcl_center_window
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
from .mega_widgets.launcher import LauncherTools


class App:
    """Main Application Object"""

    def __init__(self, ini_file: str):
        if isinstance(ini_file, str):
            with open(ini_file, encoding="utf-8") as f:
                self.ini_data = json.load(f)
        elif isinstance(ini_file, dict):
            self.ini_data = ini_file
        else:
            raise TypeError(f"Invalid ini_file argument type: {type(ini_file)}")
        self.app_name = self.ini_data.get("application")
        self.version = self.ini_data.get("version")
        self.version_name = "{} Version {}".format(self.app_name, self.version)
        self.os = platform.system()
        self.os_version = platform.version()
        print(self.version_name)
        print("Using Python {}.{}".format(*sys.version_info[:2]))
        print("Using tkinter version {}".format(tk.Tcl().eval("info patchlevel")))

        self.scaling = self.ini_data.get("scaling", 1.0)
        print(f"Application scaling factor - {self.scaling}")
        scale_minsize = self.ini_data.get("scale_minsize", False)
        minsize_factor = self.scaling if scale_minsize else 1
        self.window_min_width = int(self.ini_data.get("minwidth", 300) * minsize_factor)
        self.window_min_height = int(
            self.ini_data.get("minheight", 300) * minsize_factor
        )
        print(f"Window min size - {self.window_min_width} x {self.window_min_height}")
        scale_startsize = self.ini_data.get("scale_startsize", False)
        startsize_factor = self.scaling if scale_startsize else 1
        self.window_start_width = max(
            int(self.ini_data.get("width", 300) * startsize_factor) or 300,
            self.window_min_width,
        )
        self.window_start_height = max(
            int(self.ini_data.get("height", 300) * startsize_factor) or 300,
            self.window_min_height,
        )
        print(
            f"Window start size - {self.window_start_width} x {self.window_start_height}"
        )
        self.window = tk.Tk()  # Instantiate tk instance.
        self.focused_window = None  # Placeholder
        enable_dpi_awareness(self, self.scaling)  # Enable Windows DPI Scaling
        self.window.wait_visibility(self.window)
        self.window.tk.call("tk", "scaling", self.scaling)

        self.theme_textboxes = self.ini_data.get("theme_textboxes", True)

        # This toolkit is designed around the idea of "Tabs"
        # This is the highest level tab available.
        # Disable in config for non-tabular applications.
        if not self.ini_data.get("disable_notebook", False):
            self.notebook = ttk.Notebook(self.window)
            self.notebook.pack(fill=tk.BOTH, expand=tk.YES)

        # Add a shared menu
        self.menu = tk.Menu(self.window)
        self.window.configure(menu=self.menu)

        # Application Theming
        self.current_theme = self.ini_data.get("default_theme", "default")
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
        if self.ini_data.get("enable_users", False) or self.ini_data.get(
            "enable_profiles", False
        ):
            self.profiles_enabled = True
            self.profiles = ProfilesSystem()
            print("User profiles enabled")
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

        # Build application fonts
        self._build_fonts()

        # Application Menu
        if self.profiles_enabled:
            prof_menu = tk.Menu(self.menu, tearoff=0)
            prof_menu.add_command(label="New Profile", command=self.create_profile)
            prof_menu.add_command(label="Select Profile", command=self.select_profile)
            prof_menu.add_command(
                label="Profile Manager", command=lambda: ProfilesWindow(self)
            )
            self.menu.add_cascade(menu=prof_menu, label="Profiles")
            if self.ini_data.get("enable_launcher"):
                LauncherTools(self)

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
                f"Unable to find loaded user's selected theme {theme}. Using default theme."
            )
        self.use_theme(theme)
        self.update_default_title()

        if self.ini_data.get("start_centered"):
            self.window.after_idle(lambda: tcl_center_window(self.window))

    def create_profile(self, name: str = None) -> str | None:
        """Calling with no name brings up a popup, the popup calls this function \
        again with name kw which instead makes a new profile or asks again for a \
        name if the supplied name was invalid. `Returns the current theme as a \
        String on success or None`"""
        if self.focused_window:
            self.focused_window.destroy()
        if not name:
            self.focused_window = PromptWindow(
                window=self.window,
                text="Enter New Profile Name",
                on_yes=self.create_profile,  # Call again with name and do below
                yes_text="Make New Profile",
            )
        else:
            self.profiles.create_profile(name)
            self.update_default_title()
            self.apply_profile(self.profiles.current_profile)

    def select_profile(self, name: str = None) -> str:
        """Calling with no name brings up a popup, the popup calls this function \
        again with the name which instead calls the Profiles System to use a \
        certain profile. `Returns the current theme as a String`"""
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

    def _select_profile(self, profile: UserProfile) -> str:
        """Set the currently selected profile and update title. `Returns the current theme as a String`"""
        self.profiles.select_profile(profile)
        self.update_default_title()
        return self.apply_profile(profile)

    def apply_profile(self, profile: UserProfile) -> str:
        """Apply settings from the current profile. For more complicated profile systems \
override this function. `Returns the current theme as a String`"""
        theme = profile.get_preference("theme")
        if not theme or not theme in self.available_themes:
            print(f"User had invalid theme selected in profile - {theme}, repairing...")
            profile.set_preference("theme", "default")
        return self.use_theme(profile.get_preference("theme"))

    def toggle_maximized(self, event=None) -> None:
        """Toggles maximized window. Returns None`"""
        self.zoomed_screen_state = not self.zoomed_screen_state
        self.window.state("normal" if self.zoomed_screen_state else "zoomed")

    def toggle_full_screen(self, event=None) -> None:
        """Toggles full screen. Returns None`"""
        self.full_screen_state = not self.full_screen_state
        self.window.attributes("-fullscreen", self.full_screen_state)

    def _build_fonts(self) -> list:
        """Generates the app's font styles for a number of widgets. `Returns a List of style names`"""
        self.default_font = fnt = tkFont.nametofont("TkDefaultFont").actual()
        self.bold_font = (fnt["family"], fnt["size"], "bold")
        self.xxsmall_font = (fnt["family"], int(fnt["size"]) - 4, "normal")
        self.xxsmall_bold_font = (fnt["family"], int(fnt["size"]) - 4, "bold")
        self.xsmall_font = (fnt["family"], int(fnt["size"]) - 3, "normal")
        self.xsmall_bold_font = (fnt["family"], int(fnt["size"]) - 3, "bold")
        self.small_font = (fnt["family"], int(fnt["size"]) - 2, "normal")
        self.small_bold_font = (fnt["family"], int(fnt["size"]) - 2, "bold")
        self.large_font = (fnt["family"], int(fnt["size"]) + 2, "normal")
        self.large_bold_font = (fnt["family"], int(fnt["size"]) + 2, "bold")
        self.xlarge_font = (fnt["family"], int(fnt["size"]) + 6, "normal")
        self.xlarge_bold_font = (fnt["family"], int(fnt["size"]) + 6, "bold")
        self.xxlarge_font = (fnt["family"], int(fnt["size"]) + 12, "normal")
        self.xxlarge_bold_font = (fnt["family"], int(fnt["size"]) + 12, "bold")
        self.generated_styles = []
        for prefix, fg in zip(
            ("", "Good", "Great", "Warn", "Error", "Critical"),
            (
                self.style.lookup("TEntry", "foreground") or "#000000",
                "#339900",
                "#4091d7",
                "#ffcc00",
                "#dd6600",
                "#ff3311",
            ),
        ):
            for size, font in zip(
                (
                    "XXSmall",
                    "XXSmallBold",
                    "XSmall",
                    "XSmallBold",
                    "Small",
                    "SmallBold",
                    "",
                    "Bold",
                    "Large",
                    "LargeBold",
                    "XLarge",
                    "XLargeBold",
                    "XXLarge",
                    "XXLargeBold",
                ),
                (
                    self.xxsmall_font,
                    self.xxsmall_bold_font,
                    self.xsmall_font,
                    self.xsmall_bold_font,
                    self.small_font,
                    self.small_bold_font,
                    self.default_font,
                    self.bold_font,
                    self.large_font,
                    self.large_bold_font,
                    self.xlarge_font,
                    self.xlarge_bold_font,
                    self.xxlarge_font,
                    self.xxlarge_bold_font,
                ),
            ):
                if prefix or size:  # Don't need to configure base styles
                    for widget in ("TLabel", "TLabelframe.Label", "TButton"):
                        s = f"{prefix}{size}.{widget}"
                        self.generated_styles.append(s)
                        # print(s)
                        self.style.configure(s, font=font, foreground=fg)
        return self.generated_styles

    def use_theme(self, theme: str = None, verbose: bool = False) -> str:
        """Updates the app to use a certain theme. `Returns the current theme as a String`"""
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
        self._build_fonts()

        bg = self.style.lookup("TFrame", "background") or "#ffffff"
        text_fg = self.style.lookup("TEntry", "foreground") or "#000000"
        text_bg = self.style.lookup("TEntry", "fieldbackground") or "white"

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
        self.style.configure("Hamburger.TFrame", relief="solid", borderwidth=4)
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
        return theme

    def copy_to_user_clipboard(self, val: str) -> None:
        """Copys a text val to the user's keyboard. `Returns None`"""
        self.window.clipboard_clear()
        self.window.clipboard_append(str(val))

    def bell(self) -> None:
        """Largely redundant as all widgets have access to this method. `Returns None`"""
        self.window.bell()

    def update_default_title(self, indicate_profile=True) -> None:
        """Update the window title with the default string, optionally with a profile indicator. `Returns None`"""
        title = self.version_name
        if indicate_profile and self.profiles_enabled:
            if self.profiles.current_profile:
                title += f" - {self.profiles.current_profile.username}"
        self.window.title(title)

    def update_title(self, title) -> None:
        """Updates the window title. `Returns None`"""
        self.window.title(self.version_name)

    def get_scaling(self) -> None:
        return get_scaling(self.window)

    def mainloop(self) -> None:
        """Starts the application mainloop. `Never returns.`"""
        self.window.mainloop()

    def start(self) -> None:
        """Alias for App.mainloop(). `Never returns.`"""
        self.mainloop()
