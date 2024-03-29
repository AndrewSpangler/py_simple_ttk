import io
import json
import os
import platform
import subprocess
import sys
import time
import tempfile
import webbrowser
import zipfile
from typing import Callable
import tkinter as tk
from tkinter import ttk

from .MultiWidget import MultiWidgetMixin

WINDOWS_SYMBOL = "⊞"
ROOT = os.path.dirname(os.path.dirname(__file__))
ASSETS_REL_PATH = "./assets"

if getattr(sys, "frozen", False):
    ASSETS_FOLDER = os.path.abspath(os.path.join(sys._MEIPASS, ASSETS_REL_PATH))
else:
    ASSETS_FOLDER = os.path.join(ROOT, ASSETS_REL_PATH)


def get_asset(path, folder: str = ASSETS_FOLDER) -> str:
    """Gets an asset from the included assets folder by relative path. Works with pyinstaller."""
    return os.path.abspath(os.path.join(folder, path))


def get_themes_folder() -> str:
    """Gets the absolute path to the included themes folder"""
    return os.path.abspath(os.path.join(ASSETS_FOLDER, "themes"))


def get_bundled_themes_list(verbose: bool = False) -> list:
    def determine_theme(fp: str):
        return fp.endswith(".tcl") and not fp.endswith("pkgIndex.tcl")

    themes = []
    for entry in os.scandir(get_themes_folder()):
        if entry.is_file():
            if determine_theme(entry.path):
                themes.append(entry.path)
        elif entry.is_dir():
            for subentry in os.scandir(entry.path):
                if determine_theme(subentry.path):
                    themes.append(subentry.path)
    if verbose:
        print(f"Found {len(themes)} bundled themes: {json.dumps(themes, indent=4)}")
    return themes


def make_temp_config_file(config: dict):
    """Make a one-time-use app config file from a dict in the same form as a normal config json. `Returns file path as String`"""
    (tp := tempfile.NamedTemporaryFile(delete=False)).write(
        bytes(
            json.dumps(config, indent=4),
            "utf-8",
        )
    )
    tp.flush()
    return tp.name


def force_aspect(
    inner_frame: ttk.Frame, outer_frame: ttk.Frame, ratio: float = (16 / 9)
) -> None:
    """Forces an inner frame to maintain an aspect ratio regardless of the outer frame's size"""

    def force_ratio(event):
        w = event.width
        h = int(event.width / ratio)
        if h > event.height:
            h = event.height
            w = int(event.height * ratio)
        inner_frame.place(
            in_=outer_frame,
            relx=0.5,
            rely=0.5,
            x=-0.5 * float(w),
            y=-0.5 * float(h),
            width=w,
            height=h,
        )

    outer_frame.bind("<Configure>", force_ratio)


def make_aspect_frames(parent: ttk.Frame, ratio: float = (16 / 9)) -> tuple:
    """Creates an outer and inner frame within a parent frame. Forces the inner frame to maintain an aspect ratio. Returns the outer and inner frames."""
    outer_frame = ttk.Frame(parent)
    inner_frame = ttk.Frame(outer_frame).place(relwidth=1, relheight=1)
    force_aspect(inner_frame, outer_frame, ratio)
    return outer_frame, inner_frame


def center_window(main_window: tk.Tk, spawn_window: tk.Toplevel) -> None:
    """Centers spawn window on main window. Call win.update_idletasks() on either window before calling this if said window is not yet shown."""
    pos_x, width = main_window.winfo_x(), main_window.winfo_width()
    pos_y, height = main_window.winfo_y(), main_window.winfo_height()
    width2, height2 = spawn_window.winfo_width(), spawn_window.winfo_height()
    spawn_window.geometry(
        "+%d+%d" % (pos_x + (width - width2) / 2, pos_y + (height - height2) / 2)
    )


def focus_next(event) -> object:
    """Forces focus to the widget after the one that triggered the event"""
    (widget := event.widget.tk_focusNext()).focus()
    return widget


def default_separator(
    f: ttk.Frame, padx: tuple = 35, pady: tuple = (10, 5)
) -> ttk.Separator:
    """Apply a consistent horizontal separator."""
    (separator := ttk.Separator(f, orient="horizontal")).pack(
        fill="x", padx=padx, pady=pady
    )
    return separator


def default_pack(widget, bottom: bool = False, padx: tuple = 5) -> None:
    """Apply a consistent descending packing method."""
    widget.pack(fill="x", expand=False, side=tk.TOP, padx=padx, pady=(0, 5 * bottom))


def default_vertical_separator(
    frame: ttk.Frame, pady: tuple = 15, padx: tuple = 10
) -> ttk.Separator:
    """Apply a consistent vertical separator."""
    (separator := ttk.Separator(frame, orient="vertical")).pack(
        fill="y", padx=padx, pady=pady, expand=False, side=tk.LEFT
    )
    return separator


def default_vertical_pack(
    widget, expand: bool = False, fill: str = tk.BOTH, padx: tuple = 0
) -> None:
    """Apply a consistent packing method to vertically packed widgets."""
    widget.pack(fill=fill, expand=expand, side=tk.LEFT, padx=padx)


def copy_to_user_clipboard(widget, value: str) -> None:
    """Copies a string to the user's clipboard."""
    widget.clipboard_clear()
    widget.clipboard_append(value)


def check_in_bounds(pos: tuple, bounds: tuple) -> bool:
    """Checks if a position is within a given bounds. Pos is generally a mouse event position tuple, bounds is generally a canvas.bbox(), but a (left, top, right, bottom) tuple will work too."""
    x, y = pos
    lb, tb, rb, bb = bounds
    return all((x > lb, x < rb, y > tb, y < bb))


def get_generated_font_images_lookup(path: str = None) -> dict:
    """Makes a lookup for the pre-generated open-sans font monograms that ship with py_simple_ttk."""
    with zipfile.ZipFile(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "assets/generated.zip"
        ),
        "r",
    ) as z:
        with z.open("manifest.txt", "r") as f:
            manifest = f.read().decode().splitlines()
    fonts = {}
    for entry in manifest:
        # if entry.is_file():
        # if entry.path.endswith(".png"):
        char, size, color = entry[:-4].split("_")
        size = int(size)
        if not size in fonts:
            fonts[size] = {}
        if not color in fonts[size]:
            fonts[size][color] = {}
        fonts[size][color][char] = entry
    return fonts


def get_generated_font_image(file: str) -> bytes:
    with zipfile.ZipFile(
        os.path.join(ROOT, "assets/generated.zip"),
        "r",
    ) as z:
        with z.open(file, "r") as f:
            return f.read()


def get_generated_font_images(files: list) -> list:
    out = []
    with zipfile.ZipFile(
        os.path.join(ROOT, "assets/generated.zip"),
        "r",
    ) as z:
        for _f in files:
            with z.open(_f, "r") as f:
                out.append(f.read())
    return out


def bbox_to_width_and_height(bbox: tuple) -> tuple:
    """Takes a bbox and converts it to a width and height tuple."""
    return (bbox[2] - bbox[0], bbox[3] - bbox[1])


def recursive_widget_search(
    node_widget, widget_type_to_find: type, found_list: list = []
) -> list:
    """
    Adds widgets of a given type to a list as it travels up,
    away from the root of a widget tree. This method can be slow on
    large widget trees but is useful for retheming tk widgets with
    ttk formatting on theme changes. `Returns a list of widgets`
    """
    for w in node_widget.winfo_children():
        if isinstance(w, widget_type_to_find):
            found_list.append(w)
        else:
            recursive_widget_search(w, widget_type_to_find, found_list)
    return found_list  # Returns list at end of initial call


def complex_widget_search(
    node_widget, widget_types_to_find: list | tuple, found_lists: dict = {}
) -> dict:
    """A more robust version of the widget search with lists for multiple widget types found in one go"""
    if not found_lists:
        for w in widget_types_to_find:
            found_lists[w] = []
    for w in node_widget.winfo_children():
        for wt in widget_types_to_find:
            if isinstance(w, wt):
                if not found_lists.get(wt):
                    found_lists[wt] = []
                found_lists[wt].append(w)
        complex_widget_search(w, widget_types_to_find, found_lists)
    return found_lists  # The only time this return is ever used is at the end of the first call


def run_cl(commands: list) -> None:
    """Runs something via command line. `Returns None`"""
    subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def open_link(link: str) -> None:
    """Opens a link in the user's default web browser. `Returns None`"""
    print(f"Opening {link} in default web browser")
    webbrowser.open_new_tab(link)


def get_local_appdata_folder() -> str:
    """Opens user's Windows home folder. Only works on Windows for obvious reasons."""
    return os.path.expandvars("%LOCALAPPDATA%")


def set_desktop_background(file: str):
    if platform.system() == "Windows":
        import ctypes

        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(file), 0)
    else:
        raise NotImplemented


def enable_notebook_movement(app) -> None:
    """Copyright CJB 2010-07-31: https://wiki.tcl-lang.org/page/Drag+and+Drop+Notebook+Tabs Enables Tab dragging in subsequently created notebooks. Only run this function once."""
    tcl_configuration = """
    namespace eval tabdrag {}
    bind TNotebook <Destroy> {+tabdrag::destroy %W}
    bind TNotebook <Button-1> {+tabdrag::click %W %x %y}
    bind TNotebook <ButtonRelease-1> {+tabdrag::release %W %x %y}
    bind TNotebook <B1-Motion> {+tabdrag::move %W %x %y}

    proc ::tabdrag::destroy {win} {
      variable winstate;

      array unset winstate ?,$win
    }

    proc ::tabdrag::click {win x y} {
      variable winstate;

      set what [$win identify tab $x $y]
      if { $what eq "" || [$win index end] <= 1} {
           return;
         }

      set winstate(x,$win) $x
      set winstate(t,$win) [lindex [$win tabs] $what]
      set winstate(e,$win) 0
    }

    proc ::tabdrag::release {win x y} {
      variable winstate;

      array unset winstate ?,$win
    }

    proc ::tabdrag::move {win x y} {
      variable winstate;

      if { ![info exists winstate(x,$win)] || ![info exists winstate(t,$win)] || $winstate(t,$win) eq "" } {
           return;
         }

      set where [$win identify tab $x $y]
      if { [info exists winstate(a,$win)] } {
           if { $x < $winstate(a,$win) && $where < $winstate(i,$win) } {
                unset -nocomplain winstate(a,$win) winstate(i,$win) winstate(j,$win)
              } elseif { $x > $winstate(a,$win) && $where > $winstate(i,$win) } {
                unset -nocomplain winstate(a,$win) winstate(i,$win) winstate(j,$win)
              }
         }
      if { $where ne "" } {
           set what [lindex [$win tabs] $where]
         } else {
           set what ""
         }
      if { $what eq $winstate(t,$win) } {
           return;
         }
      if { $what eq "" } {
           # Not over a tab - check to see if we're before or after where we started
           if { $winstate(e,$win) } {
                return;
              }
           set winstate(e,$win) 1
           if { $x < $winstate(x,$win) } {
                $win insert 0 $winstate(t,$win)
              } else {
                $win insert end $winstate(t,$win)
              }
           #unset -nocomplain winstate(j,$win) winstate(a,$win) winstate(i,$win)
           set winstate(x,$win) $x
         } else {
           set winstate(e,$win) 0
           if { [info exists winstate(j,$win)] && $what eq $winstate(j,$win) } {
                if { (($x > $winstate(x,$win) && $x > $winstate(a,$win)) || ($x < $winstate(x,$win) && $x < $winstate(a,$win))) } {
                     return;# avoid stuttering when jumping a bigger tab
                   }
              }
           $win insert $what $winstate(t,$win)
           set winstate(j,$win) $what
           set winstate(a,$win) $x
           set winstate(i,$win) $where
         }
    }
    """
    app.window.tk.eval(tcl_configuration)


def create_round_rectangle(
    canvas,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    r: float = 20,
    fill: str = "",
    outline: str = "#000000",
    **kwargs,
):
    """Draws a rounded rectangle of a given radius on a tk.canvas"""
    x1r = x1 + r
    x2mr = x2 - r
    y1r = y1 + r
    y2mr = y2 - r

    # fmt: off
    points = (
        x1r,    y1,
        x1r,    y1,
        x2mr,   y1,
        x2mr,   y1,
        x2,     y1,
        x2,     y1r,
        x2,     y1r,
        x2,     y2mr,
        x2,     y2mr,
        x2,     y2,
        x2mr,   y2,
        x2mr,   y2,
        x1r,    y2,
        x1r,    y2,
        x1,     y2,
        x1,     y2mr,
        x1,     y2mr,
        x1,     y1r,
        x1,     y1r,
        x1,     y1
    )
    # fmt: on

    return canvas.create_polygon(
        points,
        **kwargs,
        smooth=True,
        outline=outline,
        fill=fill,
    )
