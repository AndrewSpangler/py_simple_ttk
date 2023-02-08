import os
import shutil
import tkinter as tk


def tcl_center_window(window: tk.Tk | tk.Toplevel) -> None:
    """Centers a window on desktop. `Returns None`"""
    window.eval("tk::PlaceWindow . center")


def tcl_bell(window: tk.Tk | tk.Toplevel) -> None:
    """Plays system bell sound. `Returns None`"""
    window.eval("bell")


def tcl_choose_font(window: tk.Tk | tk.Toplevel) -> tuple | None:
    """Select a font using system font dialog. `Returns a tuple or None if no selection was made`"""

    selection_holder = []

    def callback(sel):
        # parse selection
        sel = sel.strip()
        font = sel[sel.index("{") + 2 : sel.index("}")]
        size = int(sel[sel.index("}") + 1 :].strip())
        selection_holder.append((font, size))

    # Register temporary command
    cmd_tag = window.register(callback)
    # Configure font window
    window.eval(f"tk::fontchooser configure -command {cmd_tag}")
    # Show font window and await input
    window.eval(f"tk::fontchooser show")
    # Undregister temporary command
    window.deletecommand(cmd_tag)

    if len(selection_holder):
        return selection_holder[0]


def tcl_download_file(
    window: tk.Tk | tk.Toplevel,
    url: str,
    filename: str,
    directory: str = None,
    makedirs: bool = False,
    loadafter: bool = False,
) -> None | bytes:
    """
    Uses tcl to download a file at a given url
    Will download the file to the current python cwd unless the `directory` argument is specified
    Set the `makedirs` flag to true to create the download directory if it doesn't exist
    If the loadafter flag is set to true the contents of the file will be loaded and returned in bytes form

    Limitations: The standard tcl http lib lacks tls support and therefor can only download over http (not https)
    """

    directory = str(directory or os.getcwd())
    directory = directory.replace("\\", "/")  # Make path compatible with tcl
    if not os.path.isdir(directory):
        if makedirs:
            os.makedirs(directory)
        else:
            raise FileNotFoundError(
                f"Failed to find download directory - {directory} doesn't exist"
            )

    # Build TCL script
    tcl_code = f"""
        package require http;
        set d [::http::geturl {url}];
        ::http::wait $d;
        set f [open {directory}/{filename} w];
        puts $f [::http::data $d];
        close $f;
    """
    window.eval(tcl_code)

    if loadafter:
        with open(os.path.join(directory, filename), "rb") as f:
            return f.read()
